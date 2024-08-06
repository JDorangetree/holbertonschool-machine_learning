#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """plt show"""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    labels = ['Farrah', 'Fred', 'Felicia']
    width = 0.35
    l_fruit = ['apples', 'bananas', 'oranges', 'peaches']
    c = ['red', 'yellow', '#ff8000', '#ffe5b4']

    y_offset = np.zeros(len(labels))

    for row in range(len(fruit)):
        plt.bar(labels, fruit[row], bottom=y_offset,
                label=l_fruit[row], color=c[row], width=0.5)
        y_offset = y_offset + fruit[row]

    plt.ylim(0, 80)
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.legend()

    plt.show()
