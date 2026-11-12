import pandas as pd
df = pd.DataFrame({
    "RollNo": [1, 2, 3, 4],
    "Name": ["Amit", "Riya", "Karan", "Sara"],
    "Marks": [85, 92, 78, 88],
})
print("Original DataFrame:\n", df)

# Export
df.to_csv("student.csv", index=False)
df.to_excel("student.xlsx", index=False, sheet_name="Marks")
df.to_json("student.json", orient="records", indent=2)
print("\nData exported to student.csv, student.xlsx and student.json")

# Import
csv_data = pd.read_csv("student.csv")
excel_data = pd.read_excel("student.xlsx", sheet_name="Marks")
json_data = pd.read_json("student.json")

print("\nData imported from CSV:\n", csv_data)
print("\nData imported from Excel:\n", excel_data)
print("\nData imported from JSON:\n", json_data)

# Checking that all three are identical
print("\nAll formats identical:",
      csv_data.equals(excel_data) and csv_data.equals(json_data))
