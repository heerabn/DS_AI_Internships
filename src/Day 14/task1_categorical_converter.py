# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:59:56 2026

@author: heera
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual'],
    'Color': ['Red', 'Blue', 'Green', 'Red']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# -----------------------------
# Step 2: Label Encoding (Binary)
# -----------------------------
le = LabelEncoder()
df['Transmission'] = le.fit_transform(df['Transmission'])

print("\nAfter Label Encoding (Transmission):")
print(df)

# -----------------------------
# Step 3: One-Hot Encoding (Nominal)
# -----------------------------
df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print("\nAfter One-Hot Encoding (Color with drop_first=True):")
print(df)