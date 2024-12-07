import matplotlib.pyplot as plt

# Example data (replace with your actual data)
wavelengths = [400, 450, 500, 550, 600, 650, 700]
absorbance_beverage1 = [0.1, 0.2, 0.4, 0.5, 0.3, 0.2, 0.1]
absorbance_beverage2 = [0.2, 0.3, 0.5, 0.6, 0.4, 0.3, 0.2]

# Plot Absorbance vs. Wavelength for each beverage
plt.plot(wavelengths, absorbance_beverage1, 'r-', label="Beverage 1")
plt.plot(wavelengths, absorbance_beverage2, 'g-', label="Beverage 2")

# Add labels and title
plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance')
plt.title('Absorbance vs. Wavelength for Various Beverages')

# Show the legend
plt.legend()

# Display the plot
plt.show()
