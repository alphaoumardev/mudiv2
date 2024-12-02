# To complete this project and evaluate vacation preferences using the dataset, here's a step-by-step guide for implementing the tasks and justifying the methodology:
#
# ---
#
# ### **Step 1: Choosing Classifiers**
# Select three classifiers based on their strengths and explain why they are suitable for this classification task. For example:
#
# 1. **Decision Trees**:
# - Strengths: Easy to interpret, handles categorical and numerical data well, and captures feature interactions effectively.
# - Suitability: Useful for understanding the important factors influencing preferences (e.g., weather, location proximity).
#
# 2. **K-Nearest Neighbors (K-NN)**:
# - Strengths: Non-parametric, simple, and effective for smaller datasets with clear boundaries.
# - Suitability: Likely effective if the vacation preferences show clear separations based on certain features.
#
# 3. **Support Vector Machine (SVM)**:
# - Strengths: Performs well with small datasets, effective for linear and non-linear boundaries using kernels.
# - Suitability: Helps handle complex patterns between features influencing beach vs. mountain preferences.
#
# Justification for the choice should include diverse methodologies (e.g., tree-based, distance-based, and kernel-based classifiers) to compare results effectively.
#
# ---

import matplotlib.pyplot as plt
### **Step 2: Data Preparation and Exploration**
# 1. **Load and Explore Data**:
# Use pandas and matplotlib/seaborn to load and visualize the data.
# ```python
import pandas as pd
import seaborn as sns

# Load dataset
data = pd.read_csv("mountains_vs_beaches.csv")
print(data.head())

# Visualize target distribution
sns.countplot(x="Preference", data=data)
plt.show()
# ```
#
# 2. **Feature Analysis**:
# Analyze relationships between features and preferences using correlation matrices and pairplots.
#
# 3. **Preprocessing**:
# - Handle missing values.
# - Convert categorical data to numerical using one-hot encoding or label encoding.
# - Normalize or scale numerical features for SVM and K-NN.
#
# 4. **Split Data**:
# Split the dataset into training and test sets (e.g., 80/20 split) to evaluate performance.
# ```python
from sklearn.model_selection import train_test_split

X = data.drop("Preference", axis=1)
y = data["Preference"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# ```
#
# ---
#
# ### **Step 3: Model Implementation**
# Implement the chosen classifiers using `scikit-learn`.
#
# 1. **Decision Tree**:
# ```python
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)
tree_score = tree.score(X_test, y_test)
print(f"Decision Tree Accuracy: {tree_score}")
# ```
#
# 2. **K-Nearest Neighbors**:
# ```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)
print(f"K-NN Accuracy: {knn_score}")
# ```
#
# 3. **Support Vector Machine**:
# ```python
from sklearn.svm import SVC

svm = SVC(kernel='rbf', random_state=42)
svm.fit(X_train, y_train)
svm_score = svm.score(X_test, y_test)
print(f"SVM Accuracy: {svm_score}")
# ```
#
# ---
#
# ### **Step 4: Model Validation and Evaluation**
# 1. **Cross-Validation**:
# Use cross-validation to evaluate each classifier and prevent overfitting.
# ```python
from sklearn.model_selection import cross_val_score

cv_tree = cross_val_score(tree, X, y, cv=5)
print(f"Decision Tree CV Score: {cv_tree.mean()}")

cv_knn = cross_val_score(knn, X, y, cv=5)
print(f"K-NN CV Score: {cv_knn.mean()}")

cv_svm = cross_val_score(svm, X, y, cv=5)
print(f"SVM CV Score: {cv_svm.mean()}")
# ```
#
# 2. **Confusion Matrix and Classification Report**:
# Evaluate the models' precision, recall, and F1-score.
# ```python
from sklearn.metrics import classification_report

y_pred_tree = tree.predict(X_test)
print("Decision Tree Classification Report:")
print(classification_report(y_test, y_pred_tree))
# ```
#
# 3. **ROC Curve and AUC**:
# Analyze the ROC curve for a better understanding of the classifiers’ performance.
# ```python
from sklearn.metrics import roc_curve, auc

y_prob_tree = tree.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob_tree, pos_label=1)
roc_auc = auc(fpr, tpr)
# ```
#
# ---
#
# ### **Step 5: Results and Discussion**
# - **Compare Classifiers**:
# Present results (e.g., accuracy, precision, recall, F1-score, AUC) in a tabular or graphical format.
# - **Feature Importance**:
# For decision trees, plot feature importance to understand influential factors.
# ```python
importances = tree.feature_importances_
plt.barh(X.columns, importances)
plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.show()
# ```
#
# - **Address Overfitting**:
# Discuss techniques like pruning (Decision Trees), regularization (SVM), or parameter tuning (K-NN).
# Use grid search or randomized search for hyperparameter tuning.
#
# ---
#
# This structure ensures a comprehensive approach to implementing, validating, and analyzing the classifiers for predicting vacation preferences.
#