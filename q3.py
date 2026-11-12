import pandas as pd

n = int(input("Enter number of students: "))
records = []

for i in range(n):
    print("\nEnter details of student", i + 1)
    roll = int(input("Roll No : "))
    name = input("Name    : ")
    course = input("Course  : ")
    marks = float(input("Marks   : "))
    records.append({"RollNo": roll, "Name": name, "Course": course, "Marks": marks})

df = pd.DataFrame(records)
print("\nDataFrame created:")
print(df)

df.to_csv("students_dataset.csv", index=False)
print("\nDataset saved as students_dataset.csv")

# Reading the saved file to verify
check = pd.read_csv("students_dataset.csv")
print("\nData read back from the CSV file:")
print(check)
