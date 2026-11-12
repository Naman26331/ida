import pandas as pd
data = {
    "RollNo":     [101, 102, 103, 104, 105, 106, 107, 108],
    "Name":       ["Aman", "Bhavna", "Chetan", "Divya", "Esha", "Farhan", "Gauri", "Harsh"],
    "Gender":     ["Male", "Female", "Male", "Female", "Female", "Male", "Female", "Male"],
    "Course":     ["BCA", "BBA", "BCA", "BBA", "BCA", "BCom", "BBA", "BCA"],
    "Grade":      ["B", "A", "C", "A", "C", "B", "A", "C"],
    "Age":        [18, 19, 18, 20, 19, 18, 19, 20],
    "Siblings":   [1, 2, 0, 1, 3, 1, 2, 0],
    "Marks":      [78.5, 85.0, 62.25, 91.5, 55.0, 70.75, 88.0, 67.5],
    "Attendance": [92.4, 88.0, 75.5, 96.2, 68.0, 80.3, 94.1, 72.8],
}
df = pd.DataFrame(data)
print("Student Dataset:")
print(df)
print("\nData types of the columns:")
print(df.dtypes)

# Numerical and categorical columns
numerical = df.select_dtypes(include="number").columns.tolist()
categorical = [c for c in df.columns if c not in numerical]
print("\nNumerical columns  :", numerical)
print("Categorical columns:", categorical)

# Discrete (countable, whole numbers) and continuous (measured, any value)
discrete = [c for c in numerical if df[c].dtype == "int64"]
continuous = [c for c in numerical if df[c].dtype == "float64"]
print("\nDiscrete columns   :", discrete)
print("Continuous columns :", continuous)

# Nominal and ordinal categorical data
print("\nNominal categorical (no order)   : Name, Gender, Course")
print("Ordinal categorical (has order)  : Grade (A > B > C)")
