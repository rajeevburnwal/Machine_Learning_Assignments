import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Create sample data
data = np.array([
    [20, 20000],
    [25, 30000],
    [30, 40000],
    [35, 50000],
    [40, 60000]
])

# Apply StandardScaler
standard_scaler = StandardScaler()
standard_result = standard_scaler.fit_transform(data)

print("StandardScaler Output:")
print(standard_result)

print("Minimum:", standard_result.min())
print("Maximum:", standard_result.max())

# Apply MinMaxScaler
minmax_scaler = MinMaxScaler()
minmax_result = minmax_scaler.fit_transform(data)

print("\nMinMaxScaler Output:")
print(minmax_result)

print("Minimum:", minmax_result.min())
print("Maximum:", minmax_result.max())