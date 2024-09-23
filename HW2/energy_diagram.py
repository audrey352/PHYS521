import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 1./91.17636  # Rydberg constant in nm^-1  

# Functions
def binding_energy(n):
    return -13.6/n**2  # in eV

def transition_energy(n_start, n_end):
    return binding_energy(n_end) - binding_energy(n_start)  # in eV

def emit_wavelength(tr_start, tr_end):
    invlam = R * (1/tr_start**2 - 1/tr_end**2)  # nm^-1
    return np.abs(1/invlam)  # in nm

def energy_diagram(n, tr_start, tr_end):
    plt.figure(figsize=(6,8), dpi=250)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    
    # Binding energy
    energy_n = binding_energy(n)
    for i,E_n in enumerate(energy_n):
        plt.axhline(E_n,0,1,color='grey')
        label = r'n=$\infty$, $E_n$=0 eV' if n[i]>1e4 else rf'n={n[i]:.0f}, $E_n$={E_n:.1f} eV'
        plt.text(1.01, E_n, label)

    # Energy transitions
    tr_energy = np.abs(transition_energy(tr_start, tr_end))
    # Emitted wavelengths
    wavelengths = emit_wavelength(tr_start, tr_end)
    # vertical line positions
    x = np.linspace(0.1, 0.9, len(tr_energy))
    # Plot transitions
    for i, (tr_E,lam) in enumerate(zip(tr_energy,wavelengths)):
        start_energy = binding_energy(tr_start[i])
        end_energy = binding_energy(tr_end[i])
        # plot the vertical line for the transition
        plt.plot([x[i], x[i]], [start_energy, end_energy], color='k')
        # label transition energy
        plt.text(x[i] + 0.01, (start_energy + end_energy)/2, f'{tr_E:.1f} eV', color='k', 
                 weight="bold", rotation='vertical', verticalalignment='center')
        # label emitted wavelength
        plt.text(x[i] - 0.036, (start_energy + end_energy)/2, f'{lam:.1f} nm', color='r', 
                 weight="bold", rotation='vertical', verticalalignment='center')

    # Plot labels
    plt.xticks([])  # Hide x axis
    plt.ylabel('Energy [eV]')
    plt.title('Energy Diagram for Hydrogen Atom')

    plt.tight_layout()
    plt.savefig('energy_diagram_plot.png')
    plt.show()


# using 1e6 as infinity for the computations since it's much bigegr than the other levels
n = np.array([1,2,3,4,5,1e6])
tr_start = np.array([2,3,4,5,4,1e6,1e6])
tr_end = np.array([1,2,2,2,3,1,2])
energy_diagram(n, tr_start, tr_end)