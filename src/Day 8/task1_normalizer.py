# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:54:16 2026

@author: heera
"""

import numpy as np
np.random.seed(42)
scores = np.random.randint(50, 101, size=(5, 3))
print("Original Scores:\n", scores)
subject_mean = np.mean(scores, axis=0)
print("\nSubject-wise Mean:\n", subject_mean)
centered_scores = scores - subject_mean
print("\nCentered Scores:\n", centered_scores)
