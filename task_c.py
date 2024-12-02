from __future__ import division
from __future__ import print_function

import random
from datetime import datetime

from pyspark import SparkConf, SparkContext

APP_NAME = 'LSH'
SPLITTER = ','
BANDS = 5
ROWS = 4
NUM_HASHES = BANDS * ROWS  # Total number of hashes (100 in this case)
HOSPITAL_PKS_TO_CHECK = ["150034", "050739", "330231", "241326", "070008"]

USE_UNICODE = False
DEBUG = 0
PRINT_TIME = True

INPUT_FILE = 'trial_COVID-19_Hospital_Impact.csv'
OUTPUT_FILE = None

conf = SparkConf().setAppName(APP_NAME)
sc = SparkContext(conf=conf)

def getInputData(sc, filename):
    #Efficiently reads data using Spark
    raw_rdd = sc.textFile(filename)
    header = raw_rdd.first()
    hospitals_rdd = raw_rdd.filter(lambda line: line != header).map(lambda line: line.split(SPLITTER))
    return hospitals_rdd


def customized_hash(data, a, b):
    #Improved hash function using two random coefficients
    try:
        return (a * int(data) + b) % 100
    except ValueError:
        return float('inf') #Handle non-numeric values


def create_hash_functions(num_hashes):
    #Generates a list of hash functions (tuples of (a,b))
    return [(random.randint(1, 100), random.randint(1, 100)) for _ in range(num_hashes)]


def minhash_signature(hospital_data, hash_functions):
    #Computes the MinHash signature for a single hospital
    hospital_pk, features = hospital_data
    if not features:
        return hospital_pk, [float('inf')] * NUM_HASHES

    signatures = []
    for i in range(NUM_HASHES):
        min_hash_val = float('inf')
        for feature in features:
            min_hash_val = min(min_hash_val, customized_hash(feature, hash_functions[i][0], hash_functions[i][1]))
        signatures.append(min_hash_val)
    return hospital_pk, signatures

def lsh_find_similar(signature_rdd, bands, rows, target_hospitals):

    def band_hash(signatures, band_index):
        # Hash each band's rows into buckets
        return hash(tuple(signatures[band_index * rows:(band_index + 1) * rows]))

    # Create buckets for each band
    buckets = []
    for b in range(bands):
        band_buckets = signature_rdd.map(lambda x: (band_hash(x[1], b), x[0])).groupByKey()
        buckets.append(band_buckets)

    # Find candidate pairs
    candidates = sc.union(buckets).groupByKey().mapValues(list).filter(lambda x: len(x[1]) > 1)

    # Calculate Jaccard similarity for candidate pairs
    def calculate_jaccard(target_signature, candidate_signature):
        intersection = sum(1 for a, b in zip(target_signature, candidate_signature) if a == b)
        union = len(target_signature)
        return intersection / union

    similar_hospitals = []
    for hospital_pk in target_hospitals:
        target_signature = signature_rdd.filter(lambda x: x[0] == hospital_pk).collect()[0][1]
        for _, candidates_list in candidates.collect():
            for candidate_pk in candidates_list:
                if candidate_pk != hospital_pk:
                    candidate_signature = signature_rdd.filter(lambda x: x[0] == candidate_pk).collect()[0][1]
                    jaccard_sim = calculate_jaccard(target_signature, candidate_signature)
                    similar_hospitals.append((hospital_pk, candidate_pk, jaccard_sim, target_signature[:10]))
    return similar_hospitals


def main():

    if PRINT_TIME:
        print('LSH=>Start=>%s' % str(datetime.now()))

    hospitals_rdd = getInputData(sc, INPUT_FILE)

    #Extract hospital_pk and features, handling potential errors
    hospital_features_rdd = hospitals_rdd.map(lambda row: (row[0], [x for x in row[1:] if x.isdigit()]))

    #Broadcast hash functions
    hash_functions = create_hash_functions(NUM_HASHES)
    hash_functions_broadcast = sc.broadcast(hash_functions)

    #Compute MinHash signatures
    signature_rdd = hospital_features_rdd.map(lambda x: minhash_signature(x, hash_functions_broadcast.value))

    #Collect and print signatures for specified hospitals
    signatures_to_print = signature_rdd.filter(lambda x: x[0] in HOSPITAL_PKS_TO_CHECK).collect()
    for pk, signature in signatures_to_print:
        print(f"Hospital PK: {pk}, Signature: {signature}")

    # LSH Parameters
    BANDS = 5
    ROWS = 20

    # Apply LSH to find similar hospitals
    similar_hospitals = lsh_find_similar(signature_rdd, BANDS, ROWS, HOSPITAL_PKS_TO_CHECK)

    # Print results
    for target, candidate, similarity, signature in similar_hospitals:
        print(f"Target Hospital: {target}, Candidate: {candidate}, Jaccard Similarity: {similarity:.2f}, Signature: {signature}")


    sc.stop()
    if PRINT_TIME:
        print('LSH=>Finish=>%s' % str(datetime.now()))




if __name__ == "__main__":
    main()