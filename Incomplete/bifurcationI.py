
# -*- coding: utf-8 -*-
"""
Plotting the bifurcation diagram of a chaotic disscretedynamical system
"""

import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1-x)

x = np.linspace(0,1)
fig, ax = plt.subplots(1,1)
ax.plot(x, logistic(2,x), 'k')

def plot_system(r, x0, n, ax=None):
    # Plot the function and the
    # y=x diagonal line.
    t = np.linspace(0, 1)
    ax.plot(t, logistic(r, t), 'k', lw=2)
    ax.plot([0, 1], [0, 1], 'k', lw=2)

    # Recursively apply y=f(x) and plot two lines:
    # (x, x) -> (x, y)
    # (x, y) -> (y, y)
    x = x0
    for i in range(n):
        # generate value for y given x and r
        
        
        # Plot the two lines.

        # Set x to new y

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f"$r={r:.1f}, \, x_0={x0:.1f}$")


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6),
                               sharey=True)
plot_system(__, ___, ___, ax=ax1)
plot_system(___, ___, ___,ax=ax2)



## Bifurcation Diagram
n = 10000
r = np.linspace(2.5, 4.0, n)
iterations = 1000
last = 100
x = 1e-5 * np.ones(n)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 9),
                               sharex=True)

for i in range(iterations):
    x = logistic(r, x)
    
    # Throw out line: 
    if i >= 
        ax1.plot(r, x, ',k', alpha=.25)
ax1.set_xlim(2.5, 4)
ax1.set_title("Bifurcation diagram")


## Plot Lyapunov Exponent
lyapunov = np.zeros(n)

for i in range(iterations):
        x = logistic(r, x)
        # Add lyapunov exponent to iteration
        # Derivative of lgotisc function is r-2rx
        lyapunov += 
    
# We display the Lyapunov exponent.
# Horizontal line.
ax2.axhline(0, color='k', lw=.5, alpha=.5)
# Negative Lyapunov exponent.
ax2.plot(r[lyapunov < 0],
         lyapunov[lyapunov < 0] / iterations,
         '.k', alpha=.5, ms=.5)
# Positive Lyapunov exponent.
ax2.plot(r[lyapunov >= 0],
         lyapunov[lyapunov >= 0] / iterations,
         '.r', alpha=.5, ms=.5)
ax2.set_xlim(2.5, 4)
ax2.set_ylim(-2, 1)
ax2.set_title("Lyapunov exponent")
plt.tight_layout()