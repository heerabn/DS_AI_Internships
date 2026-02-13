# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 11:55:39 2026

@author: heera
"""

import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

# Create scatter plot
plt.scatter(study_hours, scores)

# Add title and axis labels
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")

# Show plot
plt.show()
