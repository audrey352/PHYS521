import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as const
import astropy.units as u

dir_path = '/Users/audrey/Documents/PHYS521/HW3/'

# Constants
M_sun = 1.989e33 *u.g  # Solar mass
R_sun = 6.96e10 *u.cm  # Solar radius
k = const.k_B.cgs  # Boltzmann constant in erg/K
G = const.G.cgs  # Gravitational constant in cm^3 g^-1 s^-2
m_p = const.m_p.cgs  # mass of proton in g
m = 0.6*m_p  # reduced mass in g

# Functions
def core_temp(M, R, m=m, G=G, k=k):
    """
    Calculate the core temperature of a star
    """
    return G*m*M/(k*R)


# Data from Appendix G
star_mass = np.array(
    [
        60, 37, 23,  # O type
        17.5, 7.6, 5.9, 3.8,  # B type
        2.9, 2.0,  # A type
        1.6, 1.4, # F type
        1.05, 1.00,  # G type
        0.79, 0.67,  # K type
        0.51, 0.40, 0.21  # M type
    ]
) * M_sun  # [g]
star_radius = np.array(
    [
        13.4, 12.2, 10.0,  # O type
        6.7, 3.8, 3.2, 2.5,  # B type
        2.2, 1.8,  # A type
        1.4, 1.2,  # F type
        1.06, 1.00,  # G type
        0.93, 0.80,  # K type
        0.63, 0.48, 0.29  # M type
    ]
)  * R_sun  # [cm]


# Question 9
print('Question 9')
# Densities
star_density = star_mass / (4*np.pi/3 * star_radius**3)  # [g/cm^3]
air_density = 1.2e-3 *u.g/(u.cm)**3  # [g/cm^3]
water_density = 1.0 *u.g/(u.cm)**3  # [g/cm^3]
lead_density = 11.34 *u.g/(u.cm)**3  # [g/cm^3]
# Sources:
# https://chem.libretexts.org/Courses/Cleveland_State_University/CHM_151%3A_Chemistry_Around_Us/01%3A_Properties_and_Measurement_of_Matter/1.05%3A_Density
# https://kg-m3.com/material/lead

# Plot
plt.figure(dpi=200)
plt.plot(star_mass, star_density, marker='o', color='k', linestyle='-', label='MS Stars')
plt.axhline(np.mean(star_density.value), color='grey', linestyle='--', label='Average MS Star')
plt.axhline(air_density.value, color='r', linestyle='--', label='Air')
plt.axhline(water_density.value, color='b', linestyle='--', label='Water')
plt.axhline(lead_density.value, color='g', linestyle='--', label='Lead')
plt.xlabel('Mass [g]')
plt.ylabel(r'$\rho_{avg}$ [g/cm${^3}$]')
plt.yscale('log')
plt.title('HW #3, Prob 9, Fig 1: Density vs Mass for Main Sequence Stars')
plt.legend()
plt.savefig(dir_path+'figures/q9_fig1.png')
plt.show()

print(f'Average density of Main Sequence Stars: {np.mean(star_density):.2f}')


# Question 10 
print('\nQuestion 10')
# b)
# Core temperatures
core_temps = core_temp(star_mass, star_radius).to(u.K)
# Plot
plt.figure(dpi=200)
plt.plot(star_mass/M_sun, core_temps, marker='o', color='k', linestyle='-', label='MS Stars')
plt.plot(1, core_temp(M_sun, R_sun).to(u.K), marker='o', color='r', label='Sun')
plt.xlabel(r'Mass [M$_\odot$]')
plt.xscale('log')
plt.ylabel('Core Temperature [K]')
plt.title('HW #3, Prob 10, Fig 1: Core Temperature vs Mass \nfor Main Sequence Stars')
plt.legend()
plt.savefig(dir_path+'figures/q10_fig1.png')
plt.show()

# c)
T_find = 17e6 *u.K
index = np.argmin(np.abs(core_temps - T_find))
mass_find = star_mass[index]/M_sun
print(f'Mass of star with core temperature of {T_find:.2e}: {mass_find:.2f} M_sun')
print('Stellar Type: F5')