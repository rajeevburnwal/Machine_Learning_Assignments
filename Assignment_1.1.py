import numpy as np

# Internal marks of 10 students
marks = np.array([72, 85, 91, 68, 77, 88, 65, 95, 81, 74])

# Display marks
print("Internal Marks:", marks)

# Calculate and display statistical values
print("Mean: ", np.mean(marks))
print("Median: ", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))