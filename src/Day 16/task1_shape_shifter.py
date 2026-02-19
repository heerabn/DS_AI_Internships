# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:23:36 2026

@author: heera
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


np.random.seed(42)

# Generate datasets
heights = np.random.normal(loc=170, scale=10, size=1000)
incomes = np.random.lognormal(mean=10, sigma=0.8, size=1000)     
scores = 100 - np.random.lognormal(mean=2, sigma=0.4, size=1000) 

data = {
    "Human Heights (Normal)": heights,
    "Household Incomes (Right-Skewed)": incomes,
    "Easy Exam Scores (Left-Skewed)": scores
}

# Plot histograms with KDE and mean/median
plt.figure(figsize=(15,4))

for i, (title, values) in enumerate(data.items(), 1):
    plt.subplot(1, 3, i)
    sns.histplot(values, kde=True)
    plt.axvline(np.mean(values), linestyle='--', label='Mean')
    plt.axvline(np.median(values), linestyle=':', label='Median')
    plt.title(title)
    plt.legend()

plt.tight_layout()
plt.show()


for title, values in data.items():
    print(title)
    print("Mean   :", np.mean(values))
    print("Median :", np.median(values))
    print("-" * 35)
