# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:43:13 2026

@author: heera
"""

import pandas as pd

# Sample dataset with messy Location values
data = {
    "Location": [" New York", "new york", "NEW YORK ", "New York", " Chicago "]
}

df = pd.DataFrame(data)

# STEP 1 — Remove leading and trailing spaces
df["Location"] = df["Location"].str.strip()

# STEP 2 — Standardize text casing (use lower or title)
df["Location"] = df["Location"].str.title()
# alternatively: df["Location"] = df["Location"].str.lower()

# STEP 3 — Verify normalization
print("Unique Location values:")
print(df["Location"].unique())
