# from pyspark import SparkContext, SparkConf
#
#
# def process_row(row, header):
#     """
#     Converts a CSV row into a tuple with ID and a set of binary features.
#     """
#     features = {
#         f"{header[i]}:{value}" for i, value in enumerate(row[1:], start=1)
#     }
#     return row[0], features
#
# def main(input_file, hospital_pks):
#     conf = SparkConf().setAppName("BinaryFeaturesExtraction").setMaster("local[*]")
#     sc = SparkContext(conf=conf)
#
#     # Read the CSV file
#     rdd = sc.textFile(input_file).mapPartitions(lambda x: csv.reader(x))
#
#     # Extract the header
#     header = rdd.first()
#     header_broadcast = sc.broadcast(header)
#
#     # Process each row to extract binary features
#     features_rdd = rdd.filter(lambda row: row != header).map(
#         lambda row: process_row(row, header_broadcast.value)
#     )
#
#     # Combine multiple rows for the same hospital_pk
#     combined_features = features_rdd.reduceByKey(lambda a, b: a.union(b))
#
#     # Filter for the specified hospital_pks and collect the results
#     filtered_features = combined_features.filter(lambda x: x[0] in hospital_pks).collect()
#
#     for hospital_id, features in filtered_features:
#         print(f"({hospital_id}, {features})")
#
#     sc.stop()
#
# if __name__ == "__main__":
#     input_file = "trial_COVID-19_Hospital_Impact.csv"
#     hospital_pks = ["150034", "050739", "330231", "241326", "070008"]
#     main(input_file, hospital_pks)


# import csv
# from typing import List, Dict, Set
#
#
# def extract_binary_features(file_path: str) -> Dict[str, Set[str]]:
#     """
#     Extracts binary features from a CSV file and represents them in a sparse format.
#
#     Args:
#         file_path (str): Path to the input CSV file.
#
#     Returns:
#         Dict[str, Set[str]]: A dictionary where keys are record IDs, and values are sets of features.
#     """
#     sparse_representation = {}
#
#     with open(file_path, mode='r') as file:
#         reader = csv.reader(file)
#         header = next(reader)  # Extract column names
#
#         for row in reader:
#             record_id = row[0]
#             features = {
#                 f"{header[i]}:{value}" for i, value in enumerate(row[1:], start=1)
#             }
#             sparse_representation[record_id] = features
#
#     return sparse_representation
#
# file_path = "test_COVID-19_Hospital_Impact.csv"
# sparse_data = extract_binary_features(file_path)
#
# # Print a sample record's sparse representation
# for record_id, features in sparse_data.items():
#     print(f"Record ID: {record_id}, set({features})")
    # break

from pyspark.sql import SparkSession
import csv

# we create a SparkSession
spark = SparkSession.builder.appName("Hospital Features Extraction").getOrCreate()

# the data
data_path = "trial_COVID-19_Hospital_Impact.csv"

def process_row(row, header):
    """
    Converts a CSV row into a tuple with ID and a set of binary features.
    """
    features = {
        f"{header[i]}:{value}" for i, value in enumerate(row[1:])
    }
    return row[0], features

# Read the file
raw_rdd = spark.sparkContext.textFile(data_path)

# Extract header
header = next(raw_rdd.mapPartitions(lambda x: csv.reader(x)).toLocalIterator())
header_broadcast = spark.sparkContext.broadcast(header)

# Process data
hospitals_rdd = raw_rdd.mapPartitions(lambda x: csv.reader(x)) \
    .filter(lambda row: row != header) \
    .map(lambda row: process_row(row, header_broadcast.value))

# Combine features for each hospital_pk
features_by_hospital = hospitals_rdd.reduceByKey(lambda a, b: a.union(b))

hospital_pks = ["150034", "050739", "330231", "241326", "070008"]

for hospital_id, features in features_by_hospital.filter(lambda x: x[0] in hospital_pks).collect():
    print(f"({hospital_id}, set({features}))")

# Stop SparkSession
spark.stop()