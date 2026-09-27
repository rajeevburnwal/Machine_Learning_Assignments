import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

# Load Wine Dataset
wine = load_wine()

# Create DataFrame
df = pd.DataFrame(wine.data, columns=wine.feature_names)

correlation = df.corr()
print("--- Correlation Matrix ---")
print(correlation)

plt.figure(figsize=(12, 9))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap of Wine Dataset")
plt.show()

# Find Strongest Positive Correlation
correlation_matrix = correlation.copy()

# Remove self-correlation values
correlation_matrix = correlation_matrix.where(
    ~correlation_matrix.eq(1)
)
# Find feature pair with highest correlation
strongest_pair = correlation_matrix.stack().idxmax()

# Find correlation value
highest_correlation = correlation_matrix.stack().max()

# Display Result
print("\n--- Strongest Positive Correlation ---")
print("Feature 1:", strongest_pair[0])
print("Feature 2:", strongest_pair[1])
print("Correlation Value:", highest_correlation)