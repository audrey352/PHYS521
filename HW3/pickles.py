import os
from matplotlib import pyplot as plt
# from numpy import *
# from pylab import *
# from scipy import *

import math
import pylab
import numpy as np
import scipy.constants as const


# Read in Pickles Spectra into arrays
lambda_dict = {}
flux_dict = {}
dir_path = '/Users/audrey/Documents/PHYS521/HW3/'

for file in os.scandir(dir_path+'Pickles'):
    if file.is_file():
        # Get the specteal type from the file name
        name = file.name.split('_')[0]
        if name in ['B5V', 'B8V', 'O9V']:
            continue
        # Read the data into dicts
        l,f = np.loadtxt(file, delimiter=' ', unpack=True)
        lambda_dict[name] = l
        flux_dict[name] = f


# Plots
spectral_types = ['O5V', 'B3V', 'A0', 'F0', 'G0', 'K0', 'M0']
scaling_arr = [2, 1, 10, 100, 1000, 10000, 1000000]

# Figure 1
fig = plt.figure(num=1, figsize=(10, 6), dpi=150)
# plt.subplots_adjust(hspace=.5)
# plt.subplot(211)
for type in spectral_types:
    plt.plot(lambda_dict[type],flux_dict[type], linewidth=2, label=type)
# Labels & axes
plt.xlabel(r'$\lambda$ [nm]')
plt.ylabel(r'Flux$_{\lambda}$')
plt.yscale('log')
plt.title('HW #3, Prob 1, Fig 1: Spectral Types')
plt.legend(loc='upper right')
# Save
plt.savefig(dir_path+'fig1.png')
# plt.show()
plt.close()

# Figure 2
fig = plt.figure(num=2, figsize=(10, 6), dpi=150)
# plt.subplot(212)
for type, scaling in zip(spectral_types, scaling_arr):
    plt.plot(lambda_dict[type],flux_dict[type]/scaling, linewidth=2, label=type)
# Labels & axes
plt.xlabel(r'$\lambda$ [nm]')
plt.ylabel(r'Flux$_{\lambda}$')
plt.yscale('log')
plt.title('HW #3, Prob 1, Fig 2: Spectral Types')
plt.legend(loc='upper right')
# Save
plt.savefig(dir_path+'fig2.png')
# plt.show()
plt.close()




