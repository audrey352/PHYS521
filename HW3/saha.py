#!/usr/bin/python

#
#The Saha Equation for Hydrogen
#

from matplotlib import pyplot as plt
from numpy import *
from pylab import *
from scipy import *

import math
import pylab
import numpy as np
import scipy.constants as const

k      = 1.380658*1e-16        # Boltzmann constant [erg/K]
h      = 6.6261*1e-27          # Planck constant [erg s]
m_e    =  9.11*1e-28           # mass electron (gm)
ev     = 1.6*1e-12             # ev to erg


E_1 = -13.54                   # ground state energy in ev
E_2 = E_1 / 2**2
X = -E_1 * ev                  # ionization from ground in erg

g1 = 2                         # statistical weight n = 1
g2 = 6
g3 = 10
g_ii = 1                       # partition
g_i  = 1

T = np.arange(2000., 20000., 1000.)

# Saha

constant = 2* pi * m_e * k / h**2

P_e = 200     # electron pressure in dynes/cm2 for MS star
              # n_e = P_e ./ (k .* T)

one = 4 * k*T / P_e  # i.e., 4 = 2 * g_{r+1} / g_r = 2 * 2 / 1
two = (constant*T)**(1.5)
three = exp (-X/(k*T))
ratio = one * two * three              # Saha

plt.figure(1)
plt.yscale('log')
plt.plot(T,ratio, linewidth=2)
#legend(loc='upper right')
plt.grid

plt.xlabel('T (K)')
plt.ylabel('H II / H I')
plt.title('HW #3, Prob 4: Saha Ionization for Hydrogen')

# Save the figure to a file
plt.savefig('phys521_hw3_p4b.pdf')
plt.close()

