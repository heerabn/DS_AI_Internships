import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# Create non-linear data (y = x^2 + noise)
np.random.seed(42)
X = np.arange(1, 11).reshape(-1, 1)
y = X.flatten()**2 + np.random.randn(10) * 5

# -------------------------------
# 1️⃣ Linear Regression (Original Feature)
# -------------------------------
lr = LinearRegression()
lr.fit(X, y)
y_pred_linear = lr.predict(X)

r2_linear = r2_score(y, y_pred_linear)

# -------------------------------
# 2️⃣ Polynomial Features (degree = 2)
# -------------------------------
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

lr_poly = LinearRegression()
lr_poly.fit(X_poly, y)
y_pred_poly = lr_poly.predict(X_poly)

r2_poly = r2_score(y, y_pred_poly)

# Print R² scores
print("R² Score with Original Feature:", r2_linear)
print("R² Score with Polynomial Features:", r2_poly)
