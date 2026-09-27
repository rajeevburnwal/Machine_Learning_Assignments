import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create synthetic dataset
data = {
    'Age': [22, 25, 28, 30, 35, 40, 45, 29, 32, 38],
    'Salary': [25000, 32000, 40000, 45000, 55000, 65000, 75000, 42000, 50000, 60000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance'],
    'Years_of_Experience': [1, 2, 4, 5, 8, 12, 15, 4, 7, 10]
}
df = pd.DataFrame(data)

# Inject missing values deliberately
df.loc[2, 'Salary'] = np.nan
df.loc[5, 'Age'] = np.nan
df.loc[7, 'Department'] = np.nan
df.loc[9, 'Years_of_Experience'] = np.nan

print("Dataset with Missing Values:")
print(df)

# Fill numerical missing values with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Years_of_Experience'] = df['Years_of_Experience'].fillna(
df['Years_of_Experience'].mean()
)
# Fill categorical missing value with mode
df['Department'] = df['Department'].fillna(
    df['Department'].mode()[0]
)
print("\nPreprocessed Dataset:")
print(df)

# Apply MinMaxScaler
scaler = MinMaxScaler()

df[['Age', 'Salary', 'Years_of_Experience']] = scaler.fit_transform(
    df[['Age', 'Salary', 'Years_of_Experience']]
)
print("\nDataset after MinMax Scaling:")
print(df)
