import numpy as np
import matplotlib.pyplot as plt

# Values for Johnson UBVRI+ photometric system
bands = np.array(['U','B','V','R','I','J','H','K','L','M'])
flux_density = np.array([4.22e-8, 6.7e-8, 3.75e-8, 1.8e-8, 9.76e-9, 3.08e-9, 1.26e-9, 4.06e-10, 6.89e-11, 2.21e-11])  # in W m^-2 micron^-1
eff_wavelength = np.array([0.36, 0.43, 0.55, 0.70, 0.90, 1.25, 1.60, 2.22, 3.54, 4.80])  # in microns
magnitude = np.zeros(bands.size)

# Print values
for b,f,w in zip(bands, flux_density, eff_wavelength):
    print(f"{b}     {f:.2e}     {w:.2}")


# Plot
fig, axes = plt.subplots(1, 2, figsize=(13,4), dpi=150)
for i,ax in enumerate(axes):
    ax.set_xlabel("Wavelength [microns]")
    # Adding band labels
    for x,y,label in zip(eff_wavelength, [magnitude,flux_density][i], bands):
        ax.text(x+0.035,y+0.002,label)

# Fig 1 (left panel) - The magnitude of each filter UBVRIJHK versus wavelength
axes[0].scatter(eff_wavelength, magnitude, color='k', s=12)
axes[0].set_ylabel("Magnitude")
axes[0].set_title("Magnitude of Vega in Different Johnson Bands")

# Fig 2 (right panel) - Monochromatic Flux density at each filter versus wavelength
axes[1].scatter(eff_wavelength, flux_density, color='k', s=12)
axes[1].set_ylabel(r"Flux density [$W m^{-2} micron^{-1}$]")
axes[1].set_title("Monochromatic Flux Density of Vega\nin Different Johnson Bands")

# Other plot parameters
plt.savefig("Users/audrey/Documents/PHYS521/HW1/conversion_plot.pdf")
plt.show()