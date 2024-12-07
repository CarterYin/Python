import matplotlib.pyplot as plt

# Example concentration data for 13 beverages (replace with actual data)
beverages = [
    'HEYTEA Coconut Mango', 'MIXUE taro round grapes', 'HEYTEA Blackberry Mulberry', 'MIXUE Pineapple Orange', 'AUNTEA JENNY Strawberry Peach Tea',
    'AUNTEA JENNY Rose Grape', 'ChaPanda GrapeJasmine', 'ChaPanda Wheat Grass', 'Lemon black tea', 'pomegranate',
     'sour plum soup', 'kumquat lemon tea'
]

concentrations = [
    3.398, 20.57, 12.01, 3.077, 9.032,
    13.94, 8.059, 23.14, 5.401, 5.197, 32.82, 4.706
]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
bars=plt.bar(beverages, concentrations, color='skyblue')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Adding labels and title
plt.xlabel('Beverage')
plt.ylabel(r'Concentration ($10^{-6}$ mol/L)')
plt.title('Concentration of 12 Different Beverages')

# Add text labels above each bar with the concentration value
for bar in bars:
    height = bar.get_height()  # Get the height of each bar
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', 
             ha='center', va='bottom', fontsize=10)  # Display value above the bar

# Display the plot
plt.tight_layout()
plt.show()
