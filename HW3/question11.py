import numpy as np
import astropy.constants as const
import astropy.units as u

R_sun = 6.96e10 *u.cm  # Solar radius
M_sun = 1.989e33 *u.g  # Solar mass

term1 = R_sun-2/3 * 0.07 * R_sun
term2 = (0.07 * R_sun)**2
rho_o = M_sun/(4*np.pi*term1*term2)
print(f'Central density of the Sun: {rho_o:.2e}')