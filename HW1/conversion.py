import numpy as np
import matplotlib as plt

# Values for Johnson UBVRI+ photometric system
bands = np.array(['U','B','V','R','I','J','H','K','L','M','N','O'])
flux_density = np.array([4.22e-8, 6.7e-8, 3.75e-8, 1.8e-8, 9.76e-9, 3.08e-9, 1.26e-9, 4.06e-10, 6.89e-11, 2.21e-11])  # in W m^-2 micron^-1
eff_wavelength = np.array([0.36, 0.43, 0.55, 0.7, 0.9, 1.25, 1.6, 2.22, 3.54, 4.8])  # in microns
magnitude = np.array([-2.38e-5, 1.49e-4, -7.18e-5, 3.69e-4, -8.24e-5, -7.9e-4, -2.02e-4, 3.78e-5, 7.2e-4, 1.74e-3])

# Print values
for b,f,w,m in zip(bands, flux_density, eff_wavelength, magnitude):
    print(f"{b} {f} {w} {m}")


# Plots
fig, axes = plt.subplots(1, 2, figsize=(10,4), dpi=250)
for ax in axes:
    ax.set_xlabel("Wavelength [microns]")
    ax.text()

# Fig 1 (left panel) - The magnitude of each filter UBVRIJHK versus wavelength
axes[0].scatter(magnitude, eff_wavelength, color='k')
axes[0].set_ylabel("Magnitude")
axes[0].set_title("The magnitude of each filter UBVRIJHK versus wavelength")

# Fig 2 (right panel) - Monochromatic Flux density at each filter versus wavelength
axes[1].scatter(magnitude, eff_wavelength, color='k')
axes[1].set_ylabel("Magnitude")
axes[1].set_title("The magnitude of each filter UBVRIJHK versus wavelength")