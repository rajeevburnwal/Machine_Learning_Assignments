import pandas as pd
from sklearn.datasets import load_wine

# Load Wine Dataset
wine = load_wine()

# Create DataFrame
df = pd.DataFrame(wine.data, columns=wine.feature_names)

# Add target column
df["target"] = wine.target

print("--- First Five Rows ---")
print(df.head())

print("\n--- Dataset Information ---")
df.info()

print("\n---Statistical Summary---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())
