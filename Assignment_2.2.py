import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

# Load Wine Dataset
wine = load_wine()

# Create DataFrame
df = pd.DataFrame(wine.data, columns=wine.feature_names)

# Create Boxplots
plt.figure(figsize=(14, 8))

sns.boxplot(data=df)

plt.title("Boxplots of Wine Dataset Features")
plt.xticks(rotation=45)

plt.show()