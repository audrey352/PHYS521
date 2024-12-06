import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as si

kappa = 1.e-4          #opacity in m^2/kg
rho0 = 1.225          #surface density in kg/m^3
H = 8e3              #scale height in m
Rp = 6371.e3          #Earth radius in m
limit = 1.e7           #limit of integration in m; should theoretically be infinity but there is essentially no atmosphere at this altitude 


# Calculates the vertical optical depth between altitudes 'lower' and 'upper'
def vertical(lower=0, upper=limit):         #calculates the vertical optical depth, integrating from lower to upper
    def integrand(z):                             #function we want to integrate
        return np.exp(-z/H)
    tau = rho0*kappa*si.quad(integrand, lower, upper)[0]        #integrates from far above the surface to 
    return tau

def slant(b=Rp, lower=-1e7, upper=limit):
    def integrand(x):
        return np.exp(-(np.sqrt(b**2 + x**2)-Rp)/H)
    tau = rho0*kappa*si.quad(integrand, lower, upper)[0]
    return tau

# Question 1
# d)
ratio = slant()/vertical()
print(ratio)

# e)
def altitude(type, step=10):
    lower = 0
    
    while True:
        # calculate tau for the current altitude
        tau = vertical(lower=lower) if type=='vertical' else slant(lower=lower)
        # tau at lower=0 is large, and decreasing as lower increases altitude
        # so stop when we cross 2/3
        if tau <= 2/3:
            break
        # increment altitude
        lower += step

    return lower, tau

lower_vertical, tau_vertical = altitude('vertical')
print(f'Altitude for vertical optical depth = {tau_vertical}: {lower_vertical} m')
lower_slant, tau_slant = altitude('slant')
print(f'Altitude for slant optical depth = {tau_slant}: {lower_slant} m')
print('Difference in altitude: ', lower_slant-lower_vertical)

# f) 
def find_impact_parameter(step=10):
    b = Rp
    while True:
        tau = slant(b)
        if tau <= 2/3:
            break
        b += step
    return b, tau

b, tau = find_impact_parameter()
print(f'Impact parameter at tau = {tau}: {b} m')

