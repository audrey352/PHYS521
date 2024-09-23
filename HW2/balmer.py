#!/usr/bin/python

from matplotlib import pyplot as plt
from numpy import *
import pylab

import numpy as np
import math

# balmer formula

R = 1. / 91.17636          # inverse rydberg in nm

high = 10                  # highest energy level to plot
n = np.arange(3, high, 1)  # energy levels from 3 to high
last = high - 2            # skip ground state

level2 = (1. / 2.) ** 2    # (1/2)^2
leveln = (1. / n) ** 2     # (1/n)^2

invlam = R * (level2 - leveln)  # balmer formula, inverse wavelength nm-1
lam = 1. / invlam               # convert to wavelength nm
#histo = np.histogram(lam,bins=500) # use small bin size to keep lines separate

plt.hist(lam, 500)
plt.xlabel('lambda (nm)')
plt.ylabel('Energy Level')
plt.title('Rydberg Balmer Formula')
#plt.show()

# save the figure to a file
plt.savefig('phys521_hw2_1.pdf')
plt.close()
