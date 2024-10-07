import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

# Constants
k = const.k  # Boltzmann constant in J/K
dir_path = '/Users/audrey/Documents/PHYS521/HW3/'


# Functions
def binding_energy(n):
    return -13.6/n**2 * const.e  # in J

def get_g(n):
    """statistical weight that specify the number of sublevels in energy level n
    """
    # g_n = 2n^2
    return 2 * n**2

def boltz_excite(ni, nj, Tk, k=k):
    """Calculate the ratio of the number of atoms of the same element 
    with electrons in any two energy levels, i (lower) and j (upper)
    """
    # Statistical weights
    gi = get_g(ni)
    gj = get_g(nj)
    # Binding energy
    Ei = binding_energy(ni)
    Ej = binding_energy(nj)
    # Ratio nj/ni
    return gj/gi * np.exp(-(Ej - Ei)/(k*Tk))

def plot_ratio(ni, nj, Tk, k=k):
    """Plot the ratio nj/ni for a range of temperatures Tk
    """
    # Boltzmann ratio
    ratio = boltz_excite(ni, nj, Tk, k)
    # Plot
    plt.figure(dpi=150)
    plt.plot(Tk, ratio)
    plt.xlabel('Temperature [K]')
    plt.ylabel(r'$n_j/n_i$')
    plt.title(f'Ratio of the number of atoms for a 2-level \nhydrogen atom, with n={ni} and n={nj}')
    plt.savefig(dir_path+f'figures/q3_boltz_ratio_{ni}_{nj}_{Tk[-1]:.0e}.png')
    plt.show()

    return ratio

# a)
ni = 1
nj = 2
T = np.linspace(2000, 1e5, 10000)
nj_ni_ratio = plot_ratio(ni, nj, T)

# c)
index_eq = np.argmin(np.abs(nj_ni_ratio-1))
T_eq = T[index_eq]
print(f'Temperature at which the ratio n_j/n_i = 1: {T_eq} K')

# d)
index_10_percent = np.argmin(np.abs(nj_ni_ratio-0.1))
T_10_percent = T[index_10_percent]
print(f'Temperature at which the ratio n_j/n_i = 0.1: {T_10_percent} K')

# e)
ni = 1
nj = 2
T = np.linspace(2000, 1e9, 10000)
nj_ni_ratio = plot_ratio(ni, nj, T)