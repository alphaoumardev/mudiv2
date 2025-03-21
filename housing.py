# house-price-ridge.ipynb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

# Load data
df = pd.read_csv('house-price.csv')
X = df.iloc[:, 1:7].values  # X1-X6
y = df.iloc[:, 7].values    # Y

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Custom Ridge Regression
X_train_aug = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
X_test_aug = np.hstack([np.ones((X_test.shape[0], 1)), X_test])
m = X_train_aug.shape[1]
I = np.eye(m)
lambdas = [0, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

train_mses, test_mses = [], []
for lam in lambdas:
    XTX = X_train_aug.T @ X_train_aug
    w = np.linalg.inv(XTX + lam * I) @ X_train_aug.T @ y_train
    train_mse = mean_squared_error(y_train, X_train_aug @ w)
    test_mse = mean_squared_error(y_test, X_test_aug @ w)
    train_mses.append(train_mse)
    test_mses.append(test_mse)

# Plot
plt.figure()
plt.plot(lambdas, train_mses, label='Train MSE')
plt.plot(lambdas, test_mses, label='Test MSE')
plt.xscale('log')
plt.xlabel('λ (log scale)')
plt.ylabel('MSE')
plt.legend()
plt.title('Custom Ridge Regression')
plt.show()

# Sklearn Ridge Comparison
sk_train, sk_test = [], []
for lam in lambdas:
    model = Ridge(alpha=lam, fit_intercept=True).fit(X_train, y_train)
    sk_train.append(mean_squared_error(y_train, model.predict(X_train)))
    sk_test.append(mean_squared_error(y_test, model.predict(X_test)))

# Table
selected = [0, 10, 200, 5000]
results = pd.DataFrame({
    'λ': selected,
    'Custom Train': [train_mses[lambdas.index(λ)] for λ in selected],
    'Custom Test': [test_mses[lambdas.index(λ)] for λ in selected],
    'Sklearn Train': [sk_train[lambdas.index(λ)] for λ in selected],
    'Sklearn Test': [sk_test[lambdas.index(λ)] for λ in selected]
})
print(results)
