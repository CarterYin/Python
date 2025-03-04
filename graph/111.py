import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Example data (replace with your actual data)
wavelengths = np.array([470,530,580])
beverages = {
    'HEYTEA Coconut Mango': np.array([1.4599,1.4835,1.2934]),
    'MIXUE taro round grapes': np.array([0.8674,1.0599,0.5865]),
    'HEYTEA Blackberry Mulberry': np.array([1.3350,1.0575,1.0987]),
    'MIXUE Pineapple Orange': np.array([0.4218,0.3808,0.4077]),
    'AUNTEA JENNY Strawberry Peach Tea': np.array([0.7185,0.6474,0.5333]),
    'AUNTEA JENNY Rose Grape': np.array([0.6668,0.1941,0.2993]),
    'ChaPanda GrapeJasmine': np.array([0.4937,0.3170,0.3855]),
    'ChaPanda Wheat Grass': np.array([1.4539,1.0453,1.1070]),
    #'Beverage 9': np.array([0.5617,0.5185,0.3104]),
    #'Beverage 10': np.array([0.4510,0.7684,0.2393]),
    #'Beverage 11': np.array([-0.5092,-0.4109,-0.2935]),
    #'Beverage 12': np.array([0.7820,0.7881,0.5251]),
    #'Beverage 13': np.array([0.2696,0.0346,0.0416]),
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
plt.title('Absorbance vs. Wavelength for Beverages From External Milk Tea Vendors')

# Show the legend
plt.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()
