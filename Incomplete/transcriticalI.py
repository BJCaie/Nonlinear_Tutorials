# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:28:41 2020

@author: bcaie
"""


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4)

def normalForm(r, x):
    return

def getZeros(r):
    if r < 0:
        return np.array([r, 0])
    else:
        return np.array([0,r])
    


r = -3
x_hat = normalForm(r,x)
zeros = getZeros(r)

fig, ax = plt.subplots(1,1)
ax.plot(x, x_hat, 'k')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)



unstable = plt.Circle([zeros[0], 0], 0.5, color='r', fill=False)
ax.add_artist(unstable)

stable = plt.Circle([zeros[1], 0], 0.5, color='r')
ax.add_artist(stable)


## Question 1: Plot the fixed points for r = 0 and r>0

## Jump ahead? Do the same analysis for the normal forms: 
## x_hat = r*x - x^3
## x_hat = r*x + x^3


