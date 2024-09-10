# import matplotlib
# matplotlib.use('Qt5Agg')  # Use the TkAgg backend for interactive plotting

# Ensure tkinter is imported for the TkAgg backend
import matplotlib.pyplot as plt
import numpy as np

# Data for vertical bar chart
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# Create vertical bar chart
plt.bar(x, y)
plt.title('Vertical Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Data for horizontal bar chart
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# Create horizontal bar chart
plt.barh(x, y, color="red")
plt.title('Horizontal Bar Chart')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.show()
