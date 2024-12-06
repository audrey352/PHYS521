import numpy as np
import astropy.units as u
import scipy.constants as sc

h = sc.h * u.J * u.s
c = sc.c * u.m / u.s
E = 13.6 * u.eV

# a)
lam = h * c / E
print(lam.to(u.nm))

# b)
print(51/0.0033)

# c)
def Rss(N, n, alpha):
    return (3/(4*np.pi*alpha))**(1/3) * N**(1/3) * n**(-2/3)

n = 1e4 * u.cm**(-3)
alpha = 2e-13 * u.cm**3 / u.s
N_O5 = 51e48 * u.s**(-1)
N_B1 = 0.0033e48 * u.s**(-1)

Rss_O5 = Rss(N_O5, n, alpha)
Rss_B1 = Rss(N_B1, n, alpha)
print(f'O5: {Rss_O5}, {Rss_O5.to(u.au)}\nB1: {Rss_B1}, {Rss_B1.to(u.au)}')

# d)
print(f'Ratio: {Rss_O5/Rss_B1}')

