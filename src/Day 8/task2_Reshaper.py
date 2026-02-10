# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:59:46 2026

@author: heera
"""

import numpy as np

# Step 1: Create a 1D array with values 0 to 23
data = np.arange(24)
print("Original 1D array:")
print(data)

# Step 2: Reshape into (4, 3, 2)
reshaped_data = data.reshape(4, 3, 2)
print("\nAfter Reshape (4, 3, 2):")
print(reshaped_data)

# Step 3: Transpose to (4, 2, 3)
transposed_data = reshaped_data.transpose(0, 2, 1)

print("\nFinal Shape:", transposed_data.shape)
print("Final Array:")
print(transposed_data)
