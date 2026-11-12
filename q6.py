import pandas as pd
# Series from a list and from a dictionary
s1 = pd.Series([85, 90, 78, 92], index=["Maths", "Physics", "Chemistry", "English"])
s2 = pd.Series({"a": 1, "b": 2, "c": 3})
print("Series from list:\n", s1)
print("\nSeries from dictionary:\n", s2)
print("\ns1['Physics'] =", s1["Physics"])
print("Series mean   =", s1.mean())

# DataFrame from a dictionary
data = {
    "Name": ["Amit", "Riya", "Karan", "Sara"],
    "Age": [20, 21, 19, 22],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi"],
}
df1 = pd.DataFrame(data)
print("\nDataFrame from dictionary:\n", df1)

# DataFrame from a list of lists
rows = [["Amit", 85], ["Riya", 92], ["Karan", 78]]
df2 = pd.DataFrame(rows, columns=["Name", "Marks"])
print("\nDataFrame from list:\n", df2)

# Examining the DataFrame
print("\nShape   :", df1.shape)
print("Columns :", list(df1.columns))
print("Index   :", list(df1.index))
print("Data types:\n", df1.dtypes)
print("\nFirst 2 rows:\n", df1.head(2))
print("\nLast 2 rows:\n", df1.tail(2))
print("\nInfo:")
df1.info()
print("\nSummary statistics:\n", df1.describe())
