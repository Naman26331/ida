import pandas as pd
df = pd.DataFrame({
    "Name":   ["Aman", "Bhavna", "Chetan", "Divya", "Esha", "Farhan", "Gauri", "Harsh"],
    "Gender": ["M", "F", "M", "F", "F", "M", "F", "M"],
    "Course": ["BCA", "BBA", "BCA", "BBA", "BCA", "BCom", "BBA", "BCA"],
    "Marks":  [78, 85, 62, 91, 55, 70, 88, 67],
})
print("DataFrame:\n", df)

# Grouping and aggregation
print("\nAverage marks by Course:\n", df.groupby("Course")["Marks"].mean())
print("\nMultiple aggregations:\n", df.groupby("Course")["Marks"].agg(["count", "min", "max", "mean"]))
print("\nGroup by Course and Gender:\n", df.groupby(["Course", "Gender"])["Marks"].sum())

# Merging
info = pd.DataFrame({
    "Course": ["BCA", "BBA", "BCom"],
    "Department": ["Computer Applications", "Management", "Commerce"],
})
merged = pd.merge(df, info, on="Course", how="left")
print("\nMerged DataFrame:\n", merged)

# Concatenation
new_students = pd.DataFrame({
    "Name": ["Ishan", "Jiya"], "Gender": ["M", "F"],
    "Course": ["BCA", "BBA"], "Marks": [74, 81],
})
combined = pd.concat([df, new_students], ignore_index=True)
print("\nConcatenated rows (axis=0):\n", combined)

extra = pd.DataFrame({"Hostel": ["Yes", "No", "Yes", "No", "No", "Yes", "No", "Yes"]})
print("\nConcatenated columns (axis=1):\n", pd.concat([df, extra], axis=1).head())

# Pivot table
pivot = pd.pivot_table(df, values="Marks", index="Course", columns="Gender",
                       aggfunc="mean", margins=True)
print("\nPivot table (average marks):\n", pivot)
