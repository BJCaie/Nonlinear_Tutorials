# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:03:33 2020

@author: bcaie
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2)

def normalForm(r, x):
    return r + x**2



x_hat = normalForm(-2,x)

fig, ax = plt.subplots(1,1)
ax.plot(x, x_hat, 'k')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


stable = plt.Circle((-np.sqrt(2),0), 0.08, color='r')
ax.add_artist(stable)

unstable = plt.Circle((np.sqrt(2),0), 0.08, color='r', fill=False)
ax.add_artist(unstable)

## Question 1: use normalForm to make a graph with no fixed points

## Question 2: What happens when r = 0?

