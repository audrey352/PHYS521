import os
from matplotlib import pyplot as plt
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
        l,f = np.genfromtxt(file, delimiter=' ', unpack=True)
        lambda_dict[name] = l
        flux_dict[name] = f

# Plots
spectral_types = ['O5V', 'B3V', 'A0', 'F0', 'G0', 'K0', 'M0']

def plot_lambda_flux(fig_num, spectral_types=spectral_types, lambda_dict=lambda_dict,
                     flux_dict=flux_dict, scaling_arr=np.ones(100), yscale='log'):
    plt.figure(figsize=(10, 6), dpi=150)

    # Extra things for figure 3
    if fig_num == 3:
        # Axes
        plt.xlim(350,800)
        plt.ylim(0,8)
        yscale = 'linear'
        # Normalizing by the average flux
        scaling_arr = np.array([np.mean(flux_dict[type]) for type in spectral_types])
        # Adding H alpha line
        plt.axvline(656.28, linestyle=':', color='k', label=r'H$\alpha$')

    # Plot Data
    for type, scaling in zip(spectral_types, scaling_arr):
        plt.plot(lambda_dict[type],flux_dict[type]/scaling, linewidth=2, label=type)

    # Labels & axes
    plt.xlabel(r'$\lambda$ [nm]')
    plt.ylabel(r'Flux$_{\lambda}$')
    plt.yscale(yscale)
    plt.title(f'HW #3, Prob 1, Fig {fig_num}: Spectral Types', fontsize=15)
    plt.legend(loc='upper right')

    # Save
    plt.savefig(dir_path+f'figures/q1_fig{fig_num}.png')
    plt.show()


# Figure 1
# scaling_arr_1 = np.ones(len(spectral_types))
plot_lambda_flux(fig_num=1)

# Figure 2
scaling_arr_2 = [2, 1, 10, 100, 1000, 10000, 1000000]
plot_lambda_flux(fig_num=2, scaling_arr=scaling_arr_2)


# Question 1
# a)
eff_temps = [39810.7, 19054.6, 9549.93, 7211.08, 5807.64, 5188.00, 3801.89]  # in Kelvins
eff_temp_dict = {key: t for key, t in zip(spectral_types, eff_temps)}
print(r'Spectral Type |   T_eff [K]')
print('-----------------------------')
for type in eff_temp_dict:
    print(f'      {type[:2]}      |    {eff_temp_dict[type]}')

# c)
# Figure 3
scaling_arr_3 = scaling_arr_2
plot_lambda_flux(fig_num=3, scaling_arr=scaling_arr_3)