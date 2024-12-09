import numpy as np
import astropy.units as u
import astropy.constants as const
from astropy.cosmology import Planck18
import os

# Constants
abs_path = "/Users/audrey/Documents/PHYS521/HW6/" if (os.path.isdir('/Users/audrey')) else ""
H0 = Planck18.H0 # * u.km /u.s /u.Mpc  # Hubble constant in km s^-1 Mpc^-1

# Functions
def hubble_law(d, H0=H0):
    return H0 * d

# Part A
print("Part A")
# Open files
galaxy_files = {}
for i in range(4):
    galaxy_files[f"galaxy_{i}"] = np.load(abs_path + f"data/galaxy_{i}.npy")
# shape of each galaxy file: (2, n)
# 1st row = wavelength in Å
# 2nd row = flux in 1e-17 erg cm-2 s-1 Å-1

# Magnitudes
gal_app_mag = np.array([12.7, 14.9, 16.5, 20.4])
abs_mag = -21

# Distance to each galaxy
print('i)')
def distance(m, M):
    return 10 * 10**((m - M) / 5)  # in pc

for i,app_mag in enumerate(gal_app_mag):
    d = distance(app_mag, abs_mag) * u.pc
    print(f"Distance to galaxy_{i}: {d.to(u.Mpc):.2f}")

# 
print('ii)')
lambda0 = [3933, 3968] * u.Angstrom
