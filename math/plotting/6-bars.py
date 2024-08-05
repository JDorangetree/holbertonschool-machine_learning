#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))
labels = ['Farrah', 'Fred', 'Felicia']
width = 0.35
l_fruit = ['apples', 'bananas', 'oranges', 'peaches']
c = ['r', '#FFFF00', '#FF8000', '#FFE5b4']

y_offset = np.zeros(len(labels))

for row in range(len(fruit)):
    plt.bar(labels, fruit[row], bottom=y_offset,
            label=l_fruit[row], color=c[row])
    y_offset = y_offset + fruit[row]


plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()

plt.show()
