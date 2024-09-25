import numpy as np
import matplotlib.pyplot as plt

# Functions
def get_period(M,n):
    """
    calculate period for values of M and a given value of n
    """
    return 2.1**(-3/2) * (M **((n-1)/(n+3) - 1/3)) **(3/2)

def plot_period(n_arr):
    """
    plot period as a function of mass for a given n value
    """
    # Calculate values
    M = np.linspace(0.1, 200, 100)  # in solar mass units
    P = np.array([get_period(M,n) for n in n_arr])  # in days

    # Plot
    plt.figure(figsize=(6,4), dpi=250)
    for i,n in enumerate(n_arr):
        plt.plot(M, P[i], label=f'n = {n}')
    plt.yscale('log')
    plt.xscale('log')

    # Labels
    plt.xlabel('Mass [Solar Masses]')
    plt.ylabel('Period [days]')
    plt.title('Period vs. Mass for Stellar Binary Systems')
    plt.legend()

    plt.savefig('stellar_binary_plot.png')
    plt.show()

def get_mass(P,n):
    """
    calculate mass for a given period and n value
    """
    m = (n-1)/(n+3) - 1/3  # calculaitng part of the exponent
    print(2/3 * 1/m)
    return (P * 2.1**(3/2)) **(2/3 * 1/m)


# Question 6c
n_arr = np.array([4,19])
plot_period(n_arr)

# Question 6d
P = 15/24  # days
mass_range = get_mass(P,n_arr)
print(f'Mass range: {mass_range} solar masses')