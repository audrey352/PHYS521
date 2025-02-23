import numpy as np
import matplotlib.pyplot as plt

# Calculate values
magn_diff = np.array([1,2,3,4,5,6,10,20,30])
flux_ratios = 100**(magn_diff/5)  # Formula: F2/F1 = 100^{(m1-m2)/5}

# Plot
plt.scatter(magn_diff, flux_ratios, color='k')
plt.yscale('log')
plt.title("Magnitude Difference as a Function of Flux Ratio")
plt.xlabel("Magnitude Difference")
plt.ylabel("Flux Ratios")
plt.savefig("Users/audrey/Documents/PHYS521/HW1/magnitude_plot.pdf")
plt.show()

# Brightness ratio
bright_ratio = 100**((30-16)/5)
print(f"Brightness ratio: {bright_ratio:.3e}")