#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure(figsize=(6, 6))
fig.suptitle("All in one")
grid = plt.GridSpec(3, 2, wspace=0.4, hspace=0.5)

ax1 = fig.add_subplot(grid[0, 0])
plt.xlim(0, 10)
plt.plot(y0, color='r')


ax2 = fig.add_subplot(grid[0, 1])
plt.scatter(x1, y1, color='m')
plt.title('Men\'s Height vs Weight')
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")

ax3 = fig.add_subplot(grid[1, 0])
plt.plot(x2, y2)
plt.xlim(0, 28650)
plt.yscale('log')
plt.title('Exponential Decay of C-14')
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")

ax4 = fig.add_subplot(grid[1, 1])
plt.plot(x3, y31, 'r--', label='C-14')
plt.plot(x3, y32, 'g', label='Ra-226')
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.title('Exponential Decay of Radioactive Elements')
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.legend()

ax5 = fig.add_subplot(grid[-1:, :])
plt.hist(student_grades, 10, facecolor='#228bc2', edgecolor='black')
plt.title('Project A')
plt.xlabel("Grades")
plt.ylabel("Number of Students")

plt.show()
