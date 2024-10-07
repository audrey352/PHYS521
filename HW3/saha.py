from matplotlib import pyplot as plt
import numpy as np
import scipy.constants as const

# Constants
k = 1.380658*1e-16  # Boltzmann constant [erg/K]
h = 6.6261*1e-27  # Planck constant [erg s]
m_e =  9.11*1e-28  # mass electron (gm)
ev_to_erg = 1.6*1e-12  # ev to erg
dir_path = '/Users/audrey/Documents/PHYS521/HW3/'

# Energy levels
E_1 = -13.54  # ground state energy in eV, Xr
E_2 = E_1 / 2**2  # 1st excited state in eV, Xr+1
Xi = -E_1 * ev_to_erg  # ionization from ground, in erg

# Statistical weights
# g1 = 2
# g2 = 6
# g3 = 10
g_ii = 2  # for H II
g_i  = 1  # for H I


# Functions
def saha(T, P_e, g_r, g_r1, Xi=Xi, m_r=m_e, k=k, h=h):
    """
    Saha Equation
    term1 = 2kT g_{r+1}/P_e g_r
    term2 = (2pi m_r kT / h^2)^3/2
    term3 = exp(-Xi/kT)
    --> saha = term1 * term2 * term3
    """
    term_2_cst = (2*np.pi*m_r*k / h**2)**(3/2)
    
    first_term = 2*k*T*g_r1 / (P_e*g_r)
    second_term = term_2_cst * T**(1.5)
    third_term = np.exp(-Xi/(k*T))
    
    return first_term * second_term * third_term

def Ntotal_ratio(r):
    """
    Calculate the ratio of the total number of atoms to the number of ionized and neutral atoms
    r = N_ionized / N_neutral
    """
    return r / (1+r)

def plot_saha(fig_num, P_e_arr, T, ratio_arr, q_num=4):
    """
    Plot the Saha ratio for a range of temperatures T
    """
    plt.figure(dpi=150)
    # Data
    for ratio, P_e in zip(ratio_arr,P_e_arr):
        plt.plot(T, ratio, linewidth=2, label=rf'P$_e$ = {P_e}')
    # Labels & other
    plt.xlabel('T [K]')
    ylabel = r'H II / H$_{total}$' if fig_num==3 else 'H II / H I'
    plt.ylabel(ylabel)
    yscale = 'linear' if fig_num==3 else 'log'
    plt.yscale(yscale)
    plt.legend(title=r'P$_e$ [dynes/cm$^2$]')
    plt.title(f'HW #3, Prob {q_num}: Saha Ionization for Hydrogen')
    # Save
    plt.savefig(dir_path+f'/figures/q{q_num}_fig{fig_num}.png')
    plt.show()


def get_ratio(T, T_arr, ratio_arr):
    """
    Find the ratio of H II / H I at a given temperature T
    """
    index = np.argmin(np.abs(T_arr - T))
    return ratio_arr[index]

def get_temp(ratio, T_arr, ratio_arr):
    """
    Find the temperature at which the ratio of H II / H I is equal to a given ratio
    """
    index = np.argmin(np.abs(ratio_arr - ratio))
    return T_arr[index]


# Question 4
# a)
print(f'Ionization energy of hydrogen: {-E_1} eV, {Xi:.3e} erg')

# b)
T = np.linspace(2000, 20000, 100000)
P_e = [200] # electron pressure in dynes/cm2 for MS star, n_e = P_e ./ (k .* T)
# Calculate the Saha ratio
saha_ratio_1 = saha(T, P_e, g_i, g_ii)
plot_saha(fig_num=1, P_e_arr=P_e, T=T, ratio_arr=[saha_ratio_1])
# Finding ratios at different temperatures
ratio_T2000 = get_ratio(2000, T, saha_ratio_1)
print(f'Ratio 2000K: {ratio_T2000}')
ratio_T6000 = get_ratio(6000, T, saha_ratio_1)
print(f'Ratio 6000K: {ratio_T6000}')
ratio_T10000 = get_ratio(10000, T, saha_ratio_1)
print(f'Ratio 10000K: {ratio_T10000}')
# Find the temperature at which the ratio is 10
T_ratio10 = get_temp(10, T, saha_ratio_1)
print(f'Temperature at which the ratio is 10: {T_ratio10} K')

# c)
P_e_arr = [20,200,2000]  # in dynes/cm2
# Calculate the Saha ratios for each input P_e
saha_ratio_2 = np.array([saha(T, P_e, g_i, g_ii) for P_e in P_e_arr])
# Plot
plot_saha(fig_num=2, P_e_arr=P_e_arr, T=T, ratio_arr=saha_ratio_2)


# Question 6
# Calculate ratio for p_E = 200
ratio_total = Ntotal_ratio(saha_ratio_1)
# Plot
plot_saha(fig_num=3, P_e_arr=P_e, T=T, ratio_arr=[ratio_total], q_num=6)
# Get ratio at T=8000 K
