# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:31:08 2026

@author: heera
"""

import pandas as pd
import numpy as np

# Create sample dataset
np.random.seed(42)
data = pd.DataFrame({
    "Height": np.random.normal(loc=170, scale=10, size=1000)
})


mu = data["Height"].mean()
sigma = data["Height"].std()

print("Mean (μ):", round(mu,2))
print("Standard Deviation (σ):", round(sigma,2))

data["z_score"] = (data["Height"] - mu) / sigma


outliers = data[np.abs(data["z_score"]) > 3]

print("\nNumber of Outliers:", len(outliers))
print(outliers.head())