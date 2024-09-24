import numpy as np
import matplotlib.pyplot as plt

def get_period(M,n):
    return (M **((n-1)/(n+3) - 1/3)) **(3/2)

def plot_period(n_arr):
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
    m = (n-1)/(n+3) - 1/3  # calculaitng part of the exponent
    return P **(2/3 * 1/m)

# Question 6c
n_arr = np.array([4,19])
plot_period(n_arr)

# Question 6d
P = 15/24  # days
mass_range = get_mass(P,n_arr)
print(f'Mass range: {mass_range} solar masses')