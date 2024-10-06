import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

# Variables & Constants
R = 1. / 91.17636  # Rydberg constant in nm^-1
wien_cst = 2.8977729e6  # Wien's constant in nm*K
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
# Plot
plt.legend(loc='upper right')
# Save
plt.savefig(dir_path+f'q2_fig1.png')
# plt.show()


# a) wavelength of peak intensity
peak_predict = wien_cst/T_A0  # Wien's displacement law
print(f'Predicted Location of Peak Intensity: {peak_predict} nm')

# b)
def emit_wavelength(n_start, n_end):
    """
    Calculate the wavelength associated with the transition between two energy levels.
    """
    inv_lam = R * (1/n_start**2 - 1/n_end**2)  # nm^-1
    return np.abs(1/inv_lam)  # in nm

lam_ionize = emit_wavelength(2, 1e9)  # nm, approximating infinity as 1e9
print(f'Wavelength of the photon needed to ionize the hydrogen atom: {lam_ionize} nm')
plt.axvline(lam_ionize, color='r', linestyle='--', label='Ionization Wavelength')  # add line to plot

# Plot
plt.title(f'HW #3, Prob 2, Fig 2: Spectrum of the A0 Star with \nRydberg Balmer Formula up to n={n_max}', fontsize=15)
plt.legend(loc='upper right')
# Save
plt.savefig(dir_path+f'q2_fig2.png')
plt.show()