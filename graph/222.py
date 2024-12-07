import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Example data (replace with your actual data)
wavelengths = np.array([470,530,580])
beverages = {
    #'Beverage 1': np.array([1.4599,1.4835,1.2934]),
    #'Beverage 2': np.array([0.8674,1.0599,0.5865]),
    #'Beverage 3': np.array([1.3350,1.0575,1.0987]),
    #'Beverage 4': np.array([0.4218,0.3808,0.4077]),
    #'Beverage 5': np.array([0.7185,0.6474,0.5333]),
    #'Beverage 6': np.array([0.6668,0.1941,0.2993]),
    #'Beverage 7': np.array([0.4937,0.3170,0.3855]),
    #'Beverage 8': np.array([1.4539,1.0453,1.1070]),
    'Lemon black tea': np.array([0.5617,0.5185,0.3104]),
    'pomegranate': np.array([0.4510,0.7684,0.2393]),
    #'Beverage 11': np.array([-0.5092,-0.4109,-0.2935]),
    'sour plum soup': np.array([0.7820,0.7881,0.5251]),
    'kumquat lemon tea': np.array([0.2696,0.0346,0.0416]),
}

# Function to find absorption peaks
def find_peaks(wavelengths, absorbance):
    peaks = []
    for i in range(1, len(absorbance)-1):
        if absorbance[i-1] < absorbance[i] and absorbance[i] > absorbance[i+1]:
            peaks.append((wavelengths[i], absorbance[i]))
    return peaks

# Plot the absorbance vs wavelength curves for each beverage
plt.figure(figsize=(11, 11))

# Iterate through each beverage
for beverage, absorbance in beverages.items():
    # Perform cubic spline interpolation for smooth curves
    cs = CubicSpline(wavelengths, absorbance)

    # Create finer wavelength values for smooth curve
    wavelength_fine = np.linspace(wavelengths.min(), wavelengths.max(), 500)

    # Plot the smooth curve
    plt.plot(wavelength_fine, cs(wavelength_fine), label=beverage)

    # Find the peaks for this beverage
    peaks = find_peaks(wavelengths, absorbance)

    # Highlight the peaks
    for peak in peaks:
        plt.scatter(peak[0], peak[1], zorder=5)
        plt.text(peak[0], peak[1], f'({peak[0]}, {peak[1]:.2f})', fontsize=8, ha='left')

# Add labels and title
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance')
plt.title('Absorbance vs. Wavelength for Beverages in the Yuquan Road Canteen')

# Show the legend
plt.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()
