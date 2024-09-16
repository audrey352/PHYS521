import numpy as np
import matplotlib.pyplot as plt
import scipy

# constants
h = scipy.constants.Planck  # 6.626e-34 Js
c = scipy.constants.c  # 3.0e8 m/s
k = scipy.constants.Boltzmann  # 1.38e-23 J/K

# Vega
eff_wavelength = np.array([0.36, 0.43, 0.55, 0.70, 0.90, 1.25, 1.60, 2.22, 3.54, 4.80])*1e3  # in nm
flux_density = np.array([4.22e-8, 6.7e-8, 3.75e-8, 1.8e-8, 9.76e-9, 3.08e-9, 1.26e-9, 4.06e-10, 6.89e-11, 2.21e-11])*1e-3  # in W m^-2 nm^-1

# Planck Function
def planck_fxn(T, wavelengths):
    # Convert wavelengths from nm to m
    wavelengths = wavelengths * 1e-9  # meters
    # Formula: I_l = 2*h*c^2/lambda^5 * 1/(exp(h*c/(lambda*k*T)) - 1)
    I = 2*h*c**2/wavelengths**5 * 1/(np.exp(h*c/(wavelengths*k*T)) - 1)  # in SI units
    # Converting I from SI units to cgs units
    return I * 1e-6  # erg cm^-2 s^-1 nm^-1 sr^-1

# Planck
wavelengths = np.linspace(eff_wavelength[0], eff_wavelength[-1], 3000)  # nm
T = [2000, 3000, 4000, 5000, 6000, 10000]  # K


# Plot
fig, axes = plt.subplots(1, 2, figsize=(13,4), dpi=150)
# Left panel - Vega's flux density
axes[0].scatter(eff_wavelength, flux_density, color='k', label='Vega')
axes[0].set_title("Vega's Flux Density in Different Bands")
axes[0].set_ylabel(r"Flux density [$W m^{-2} nm^{-1}$]")
# Right panel - Planck's Law
for temp in T:
    I_lambda = planck_fxn(temp, wavelengths)  # in erg cm^-2 s^-1 nm^-1 sr^-1  
    axes[1].plot(wavelengths, I_lambda, label=f'T = {temp} K')
axes[1].set_title("Planck's Law at a Given Temperatures")
axes[1].set_ylabel(r'$I_\lambda$ [$erg\ cm^{-2} s^{-1} nm^{-1} sr^{-1}$]')
# Common parameters
fig.supxlabel('Wavelength [nm]')
for ax in axes:
    ax.legend()
plt.tight_layout()
plt.savefig('/Users/audrey/Documents/PHYS521/HW2/flux_density.png')
plt.show()