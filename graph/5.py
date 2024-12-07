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

# Plot the data points for each beverage (scatter plot)
plt.scatter(wavelengths, absorbance_beverage1, color='red', label="Beverage 1", zorder=5)
plt.scatter(wavelengths, absorbance_beverage2, color='green', label="Beverage 2", zorder=5)

# Highlight the peaks using shaded vertical areas
for peak in peaks_beverage1:
    x_peak = peak[0]
    y_peak = peak[1]
    # Shaded area around the peak (Gaussian-like shape)
    plt.axvspan(x_peak-5, x_peak+5, color='red', alpha=0.3, zorder=1)  # Shaded region
    
for peak in peaks_beverage2:
    x_peak = peak[0]
    y_peak = peak[1]
    # Shaded area around the peak (Gaussian-like shape)
    plt.axvspan(x_peak-5, x_peak+5, color='green', alpha=0.3, zorder=1)  # Shaded region

# Add labels and title
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance')
plt.title('Absorbance vs. Wavelength with Highlighted Absorption Peaks')

# Show the legend
plt.legend()

# Display the plot
plt.show()
