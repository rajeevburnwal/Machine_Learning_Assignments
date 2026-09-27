import pandas as pd

# Create student data
data = {
    "Student_Name": ["Rajeev", "Abir", "Souvik", "suman", "Rahul", "Priya", "Arjun", "Sneha", "Karan", "Anjali"],
    "Roll_Number": [101, 102, 103, 104, 105,106, 107, 108, 109, 110],
    "Marks": [72, 85, 68, 91, 77, 88, 65, 95, 81, 74],
    "Attendance": [88, 92, 76, 95, 81, 89, 72, 96, 84, 90]
}
# Create DataFrame
df = pd.DataFrame(data)

# Display complete DataFrame
print("--- Student Data ---")
print(df)

result = df[df["Marks"] > 80]

print("\n--- Students Scoring  above 80 ---")
print(result)