import pandas as pd
students = {
    "Name":       ["Aman", "Bhavna", "Chetan", "Divya", "Esha", "Farhan", "Gauri", "Harsh"],
    "Course":     ["BCA", "BBA", "BCA", "BBA", "BCA", "BCom", "BBA", "BCA"],
    "Marks":      [78, 85, 62, 91, 55, 70, 88, 67],
    "Attendance": [92, 88, 75, 96, 68, 80, 94, 72],
}
df = pd.DataFrame(students)

print("Original DataFrame:\n", df)

# Adding a column
df["Result"] = ["Pass" if m >= 60 else "Fail" for m in df["Marks"]]
df["Bonus"] = df["Marks"] * 0.05
print("\nAfter adding columns 'Result' and 'Bonus':\n", df)

# Adding a row
df.loc[len(df)] = ["Ishan", "BCA", 74, 85, "Pass", 3.7]
print("\nAfter adding a row:\n", df)

# Modifying values
df.loc[2, "Marks"] = 66
df["Attendance"] = df["Attendance"] + 2
df.loc[df["Name"] == "Esha", "Result"] = "Pass"
print("\nAfter modifying values:\n", df)

# Renaming columns and index
df = df.rename(columns={"Name": "Student_Name", "Marks": "Total_Marks"})
print("\nAfter renaming columns:\n", df.columns.tolist())

# Deleting a column
df = df.drop(columns=["Bonus"])
print("\nAfter deleting column 'Bonus':\n", df)

# Deleting rows
df = df.drop(index=[0, 1])
print("\nAfter deleting rows 0 and 1:\n", df)

df = df.reset_index(drop=True)
print("\nAfter resetting the index:\n", df)
