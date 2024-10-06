import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

# Variables & Constants
R = 1. / 91.17636  # Rydberg constant in nm^-1
# sigma = const.Stefan_Boltzmann  # 5.67e-8 W/m^2/K^4
T_A0 = 9549.93  # K
dir_path = '/Users/audrey/Documents/PHYS521/HW3/'

# Load Data for A0
filename = dir_path+'Pickles/A0_v2.txt'
lambda_A0, flux_A0 = np.genfromtxt(filename, delimiter=' ', unpack=True)

# Energy levels
n_max = 20  # highest energy level to plot
n = np.arange(3, n_max, 1)  # energy levels from 3 to high
level2 = (1. / 2.) ** 2  # (1/2)^2
leveln = (1. / n) ** 2  # (1/n)^2

# Balmer formula
invlam = R * (level2 - leveln)  # balmer formula, inverse wavelength nm-1
lamda_balmer = 1. / invlam  # convert to wavelength nm



# Figure
fig = plt.figure(figsize=(10, 6), dpi=150)

# Data
for lam in lamda_balmer:
    label = 'Balmer Lines' if lam == lamda_balmer[0] else None
    plt.axvline(lam, color='darkorange', linewidth=0.8, label=label)
plt.plot(lambda_A0,flux_A0/np.mean(flux_A0), linewidth=1.8, label='A0 Spectrum')  # Plot the normalized flux (using avg flux)

# Labels & Axes
plt.xlabel(r'$\lambda$ [nm]')
plt.xlim(350,700)
plt.ylabel(r'Flux$_{\lambda}$')
plt.yscale('linear')
plt.title(f'HW #3, Prob 2, Fig 1: Spectrum of the A0 Star with \nRydberg Balmer Formula up to n={n_max}', fontsize=15)
plt.legend(loc='upper right')

# Save
plt.savefig(dir_path+f'q2_fig1.png')
plt.show()

# peak_predict = 
# print(f'Predicted Location of Peak Temperature: {peak_predict} nm')