import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as const
import astropy.units as u

# Constants
dir_path = '/Users/audrey/Documents/PHYS521/HW3/'
m_H = 1.6726e-24 *u.g  # H mass in grams
m_He = 6.6447e-24 *u.g  # He mass in grams
L_sun = 3.846e33 *u.erg/u.s  # Solar luminosity
M_sun = 1.989e33 *u.g  # Solar mass

# Functions
def binding_energy(dm):
    """
    Calculate the binding energy for a mass difference dm
    dm should have astropy units
    """
    return dm * const.c**2

def fusion_rate(L, E):
    """
    Rate of fusion reactions per second
    """
    # rate of reaction = luminosity/energy released per nuclei
    return L / E  # [num fusion rxn / s]

def lifetime(rate, mass, M_sun=M_sun):
    """
    Calculate the lifetime of a star
    Mass needs to be in solar masses
    """
    # Number of H nuclei in core
    num_H_sun = 1.2e56  # sun
    num_H_star = num_H_sun * mass / M_sun  # star
    # Lifetime = (number of H nuclei that can fuse)/(rate of fusion)
    return (num_H_star / rate).to(u.year)  # [yr]


# Question 7
print('Question 7')
# a)
mass_diff = 4*m_H - m_He
print(f'Mass difference between 4H and He: {mass_diff:.2e} g')
# b)
mass_ratio = mass_diff/(4*m_H)
print(f'Ratio of mass diff and 4H: {mass_ratio:.2e} g')
# c)
E_bind_erg = binding_energy(mass_diff).to(u.erg)
E_bind_ev = E_bind_erg.to(u.eV)
print(f'Binding energy of 4H - He: {E_bind_erg:.2e}; {E_bind_ev:.2e}')
# d)
fusion_rate_sun = fusion_rate(L_sun, E_bind_erg)
print(f'Fusion rate in the Sun: {fusion_rate_sun:.2e}')


# Question 8
print('\nQuestion 8')
star_lum = np.array(
    [
        4.99e5, 3.24e5, 1.47e5,  # O type
        3.25e4, 1580, 480, 96.7,  # B type
        39.4, 12.3,  # A type
        5.21, 2.56  # F type
    ]
) * L_sun  # [erg/s]
star_mass = np.array(
    [
        60, 37, 23,  # O type
        17.5, 7.6, 5.9, 3.8,  # B type
        2.9, 2.0,  # A type
        1.6, 1.4 # F type
    ]
) * M_sun  # [g]

# a)
# Calculate rates
star_fusion_rate = fusion_rate(star_lum, binding_energy(star_mass).to(u.erg))
# Plot
plt.figure(dpi=150)
plt.plot(star_mass/M_sun, star_fusion_rate, marker='o', linestyle='-', color='k')
plt.xlabel(r'Stellar Mass [M$_\odot$]')
plt.ylabel(r'Fusion Rate [s$^1$]')
plt.yscale('log')
plt.title('HW #3, Prob 8, Fig 1: Fusion Rate vs \nStellar Mass for Main Sequence Stars')
plt.savefig(dir_path+'/figures/q8_fig1.png')
plt.show()

# b)
max_rate = np.max(rxn_rate)
print(f'Maximum fusion rate: {max_rate:.2e}')
min_rate = np.min(rxn_rate)
print(f'Minimum fusion rate: {min_rate:.2e}')
range_rate = max_rate - min_rate
print(f'Range of fusion rates: {range_rate:.2e}')

# c)
