import numpy as np
import matplotlib.pyplot as plt

# Example data (replace with your actual data)
wavelengths = np.array([400, 450, 500, 550, 600, 650, 700])
absorbance_beverage1 = np.array([0.1, 0.2, 0.4, 0.5, 0.3, 0.2, 0.1])
absorbance_beverage2 = np.array([0.2, 0.3, 0.5, 0.6, 0.4, 0.3, 0.2])

# Function to find absorption peaks
def find_peaks(wavelengths, absorbance):
    peaks = []
    for i in range(1, len(absorbance)-1):
        if absorbance[i-1] < absorbance[i] and absorbance[i] > absorbance[i+1]:
            peaks.append((wavelengths[i], absorbance[i]))
    return peaks

# Find the peaks for each beverage
peaks_beverage1 = find_peaks(wavelengths, absorbance_beverage1)
peaks_beverage2 = find_peaks(wavelengths, absorbance_beverage2)

# Plot the absorbance vs wavelength curve for each beverage
plt.plot(wavelengths, absorbance_beverage1, 'r-', label="Beverage 1")
plt.plot(wavelengths, absorbance_beverage2, 'g-', label="Beverage 2")

# Highlight the peaks
for peak in peaks_beverage1:
    plt.scatter(peak[0], peak[1], color='red', zorder=5)
    plt.text(peak[0], peak[1], f'({peak[0]}, {peak[1]:.2f})', color='red', fontsize=12, ha='left')
    
for peak in peaks_beverage2:
    plt.scatter(peak[0], peak[1], color='green', zorder=5)
    plt.text(peak[0], peak[1], f'({peak[0]}, {peak[1]:.2f})', color='green', fontsize=12, ha='left')

# Add labels and title
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance')
plt.title('Absorbance vs. Wavelength with Absorption Peaks')

# Show the legend
plt.legend()

# Display the plot
plt.show()
