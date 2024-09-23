import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Constants
h = sp.constants.Planck  # 6.626e-34 Js
c = sp.constants.c  # 3.0e8 m/s
k = sp.constants.Boltzmann  # 1.38e-23 J/K
sigma = sp.constants.Stefan_Boltzmann  # 5.67e-8 W/m^2/K^4

# Functions
def planck_fxn(wavelengths, T):
    # Convert wavelengths from nm to m
    wavelengths = wavelengths * 1e-9  # meters
    # Formula: I_lambda = 2*h*c^2/lambda^5 * 1/(exp(h*c/(lambda*k*T)) - 1)
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
    plt.savefig('planck_function_plot.png')
    plt.show()

def integ_planck(T):
    # ** need factor of pi to integrate over solid angle (ie remove the sr^-1) **
    result, error = sp.integrate.quad(planck_fxn, 10, 1e5, args=(T))  # wavelength limits in nm
    return  np.pi * result  # in cgs units (erg cm^-2 s^-1)


# Question 1
# Plot the Planck function for different T values
T = [2500, 3000, 3500, 4000, 4500, 5000]
plot_planck(T)

# Question 3
T = 6000  # K
I_6000 = integ_planck(T)  # erg cm^-2 s^-1
stef_bolt_law = sigma * T**4 *1e3  # erg cm^-2 s^-1
percent_err = np.abs((I_6000 - stef_bolt_law) / stef_bolt_law) * 100
print(f'Integrated Planck function at {T} K: {I_6000:.6e} erg cm^-2 s^-1')
print(f'Stefan-Boltzmann Law at {T} K: {stef_bolt_law:.6e} erg cm^-2 s^-1')
print(f'Percent error: {percent_err:.3e}%')