#!/usr/bin/env python3
"""function that show a line"""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """plt show"""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    plt.hist(student_grades, 10, facecolor='#228bc2', edgecolor='black')
    plt.title("Project A2)
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.show()
