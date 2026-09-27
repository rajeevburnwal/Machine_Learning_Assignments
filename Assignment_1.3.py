import pandas as pd

# Create student data
data = {
    "Student_Name": ["Rajeev", "Rahul", "Sourav", "Neha", "Aman", "Priya", "Arjun", "Sneha", "Karan", "Anjali"],
    "Roll_Number": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Marks": [72, 85, 68, 91, 77, 88, 55, 95, 81, 59],
    "Attendance": [88, 92, 76, 95, 81, 89, 72, 96, 84, 90]
}
df = pd.DataFrame(data)

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

#add grade column
df["Grade"] = df["Marks"].apply(calculate_grade)

print("--- Students Data with Grade ---")
print(df)