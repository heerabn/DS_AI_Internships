# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 11:59:41 2026

@author: heera
"""

import matplotlib.pyplot as plt

# -------- Subplot 1: Bar Chart (Categorical Comparison) --------
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

plt.subplot(1, 2, 1)   # 1 row, 2 columns, 1st plot
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

# -------- Subplot 2: Line Plot (Trend) --------
months = [1, 2, 3, 4, 5]
revenue = [200, 350, 300, 500, 650]

plt.subplot(1, 2, 2)   # 1 row, 2 columns, 2nd plot
plt.plot(months, revenue)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

# Adjust layout to avoid overlapping
plt.tight_layout()

# Show dashboard
plt.show()
