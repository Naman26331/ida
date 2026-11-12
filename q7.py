import pandas as pd
students = {
    "Name":       ["Aman", "Bhavna", "Chetan", "Divya", "Esha", "Farhan"],
    "Course":     ["BCA", "BBA", "BCA", "BBA", "BCA", "BCom"],
    "Marks":      [78, 85, 62, 91, 55, 70],
    "Attendance": [92, 88, 75, 96, 68, 80],
}
df = pd.DataFrame(students)

print("Original DataFrame:\n", df)

print("\n--- Selecting columns ---")
print(df["Name"])
print(df[["Name", "Marks"]])

print("\n--- Selecting rows ---")
print("df.loc[2]:\n", df.loc[2])
print("df.iloc[1:4]:\n", df.iloc[1:4])
print("df.loc[0:2, ['Name', 'Marks']]:\n", df.loc[0:2, ["Name", "Marks"]])

print("\n--- Filtering rows ---")
print("Marks > 80:\n", df[df["Marks"] > 80])
print("Course is BCA and Marks >= 65:\n", df[(df["Course"] == "BCA") & (df["Marks"] >= 65)])
print("Course is BBA or BCom:\n", df[df["Course"].isin(["BBA", "BCom"])])
print("Using query():\n", df.query("Attendance < 75"))

print("\n--- Sorting ---")
print("Sorted by Marks (ascending):\n", df.sort_values("Marks"))
print("Sorted by Marks (descending):\n", df.sort_values("Marks", ascending=False))
print("Sorted by Course, then Marks:\n", df.sort_values(["Course", "Marks"], ascending=[True, False]))
