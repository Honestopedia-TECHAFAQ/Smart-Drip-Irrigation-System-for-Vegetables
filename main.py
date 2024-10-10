import matplotlib.pyplot as plt

# Sample representation of the watering system plot based on available data

# Create a figure for the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the boundaries of the field using sample coordinates and dimensions
# Assuming a simple rectangular plot for demonstration
x_coords = [0, 501.23, 501.23, 0, 0]  # Example x coordinates
y_coords = [0, 0, 1056.14, 1056.14, 0]  # Example y coordinates

ax.plot(x_coords, y_coords, 'b-', linewidth=2, label='Plot Boundary')

# Adding components to the watering system
# Representing pumps, valves, and pipelines with simple symbols
ax.plot(250, 500, 'ro', label='Water Pump (Central)', markersize=8)
ax.plot([250, 501.23], [500, 500], 'g--', linewidth=1.5, label='Main Pipeline')
ax.plot([250, 250], [0, 1056.14], 'g--', linewidth=1.5, label='Secondary Pipeline')

# Adding labels for better visualization
ax.text(250, 500, 'Water Pump', fontsize=10, ha='right')
ax.text(400, 510, 'Main Pipeline', fontsize=10, ha='left')
ax.text(260, 800, 'Secondary Pipeline', fontsize=10, ha='left', rotation=90)

# Set plot title and labels
ax.set_title('Watering System Plan Scheme')
ax.set_xlabel('X Coordinates (m)')
ax.set_ylabel('Y Coordinates (m)')

# Set limits for better visualization
ax.set_xlim(-50, 600)
ax.set_ylim(-50, 1100)

# Add a legend
ax.legend()

# Display the plot
plt.grid()
plt.show()
