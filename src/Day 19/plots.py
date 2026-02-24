# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:35:23 2026

@author: heera
"""

import matplotlib.pyplot as plt

# Sample data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1500, 1800, 1700, 2000, 2200]

# Create line plot
plt.plot(months, sales)

# Add labels and title
plt.title("Monthly Sales Visualization")
plt.xlabel("Months")
plt.ylabel("Sales Amount")

# Show the graph
plt.show()