#!/usr/bin/python

from matplotlib import pyplot as plt
from numpy import *
import pylab
import numpy as np
import math

# Constants
R = 1. / 91.17636  # Rydberg constant in nm^-1

# Energy levels
n_max = 10                  # highest energy level to plot
n = np.arange(3, n_max, 1)  # energy levels from 3 to high
n_last = n_max - 2          # skip ground state

level2 = (1. / 2.) ** 2    # (1/2)^2
leveln = (1. / n) ** 2     # (1/n)^2

# Balmer formula
invlam = R * (level2 - leveln)  # balmer formula, inverse wavelength nm-1
lam = 1. / invlam               # convert to wavelength nm
# histo = np.histogram(lam,bins=500) # use small bin size to keep lines separate

plt.figure(dpi=350)
plt.hist(lam, 1000)
# Labels
plt.xlabel(r'$\lambda$ [nm]')
plt.ylabel('Energy Level')
plt.title(f'Rydberg Balmer Formula up to n={n_max}')

plt.savefig(f'balmer_plot_{n_max}.png')
plt.show()