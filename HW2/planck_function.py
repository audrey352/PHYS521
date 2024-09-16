import numpy as np
import matplotlib.pyplot as plt
import scipy

# constants
h = scipy.constants.Planck  # 6.626e-34 Js
c = scipy.constants.c  # 3.0e8 m/s
k = scipy.constants.Boltzmann  # 1.38e-23 J/K


def planck_fxn(T, wavelengths):
    # Convert wavelengths from nm to m
    wavelengths = wavelengths * 1e-9  # meters
    # Formula: I_l = 2*h*c^2/lambda^5 * 1/(exp(h*c/(lambda*k*T)) - 1)
    I = 2*h*c**2/wavelengths**5 * 1/(np.exp(h*c/(wavelengths*k*T)) - 1)  # in SI units
    # Converting I from SI units to cgs units
    return I * 1e-6  # erg cm^-2 s^-1 nm^-1 sr^-1

def plot_planck(T):
    wavelengths = np.linspace(300, 5000, 3000)  # nm
    plt.figure(dpi=250)
    for temp in T:
        plt.plot(wavelengths, planck_fxn(temp, wavelengths), label=f'T = {temp} K')
    plt.title("Planck's Law at Different Temperatures")
    plt.xlabel('Wavelength [nm]')
    plt.ylabel(r'$I_\lambda$ [$erg\ cm^{-2} s^{-1} nm^{-1} sr^{-1}$]')
    plt.legend()
    plt.savefig('/Users/audrey/Documents/PHYS521/HW2/planck_function.png')
    plt.show()


# Plot the Planck function for different T values
T = [2500, 3000, 3500, 4000, 4500, 5000]
plot_planck(T)