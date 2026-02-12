# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:19:41 2026

@author: heera
"""

import pandas as pd

# Load the dataset
df = pd.read_csv("customer_orders.csv")

# Shape before cleaning
print("Shape before cleaning:", df.shape)

# Missing values report
print("\nMissing values report:")
print(df.isna().sum())

# Fill missing numeric values with median
numeric_cols = df.select_dtypes(include="number").columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Remove duplicate rows
df = df.drop_duplicates()

# Shape after cleaning
print("\nShape after cleaning:", df.shape)