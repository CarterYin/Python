import matplotlib.pyplot as plt

# Example data (replace with your actual data)
wavelengths = [400, 450, 500, 550, 600, 650, 700]
absorbance_beverage1 = [0.1, 0.2, 0.4, 0.5, 0.3, 0.2, 0.1]
transmittance_beverage1 = [0.9, 0.8, 0.6, 0.5, 0.7, 0.8, 0.9]

absorbance_beverage2 = [0.2, 0.3, 0.5, 0.6, 0.4, 0.3, 0.2]
transmittance_beverage2 = [0.8, 0.7, 0.5, 0.4, 0.6, 0.7, 0.8]

# Create a figure and axis
fig, ax1 = plt.subplots()

# Plot absorbance on the left y-axis
ax1.plot(wavelengths, absorbance_beverage1, 'r-', label="Beverage 1 (Absorbance)")
ax1.plot(wavelengths, absorbance_beverage2, 'g-', label="Beverage 2 (Absorbance)")
ax1.set_xlabel('Wavelength (nm)')
ax1.set_ylabel('Absorbance', color='r')
ax1.tick_params(axis='y', labelcolor='r')

# Create a second y-axis for transmittance
ax2 = ax1.twinx()
ax2.plot(wavelengths, transmittance_beverage1, 'r--', label="Beverage 1 (Transmittance)")
ax2.plot(wavelengths, transmittance_beverage2, 'g--', label="Beverage 2 (Transmittance)")
ax2.set_ylabel('Transmittance', color='g')
ax2.tick_params(axis='y', labelcolor='g')

# Add title and legend
plt.title('Absorbance and Transmittance Curves for Beverages')
fig.tight_layout()
plt.legend(loc="upper left")
plt.show()
