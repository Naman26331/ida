import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Name":  [" amit ", "RIYA", "karan", "Riya", "  Sara", "amit"],
    "Age":   ["21", "20", "-5", "20", "abc", "21"],
    "City":  ["delhi", "DELHI ", "Pune", "Delhi", "mumbai", "Delhi"],
    "Marks": ["85", "92", "78", "92", "67", "85"],
})
print("Original data:\n", df)
print("\nData types:\n", df.dtypes)

# 1. Correct inconsistent text
df["Name"] = df["Name"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
print("\nAfter correcting text:\n", df)

# 2. Correct data types (invalid text becomes NaN)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# 3. Handle invalid values (age must be between 1 and 100)
df.loc[(df["Age"] <= 0) | (df["Age"] > 100), "Age"] = np.nan
df["Age"] = df["Age"].fillna(df["Age"].median()).astype(int)
df["Marks"] = df["Marks"].astype(int)
print("\nAfter fixing invalid values and data types:\n", df)
print(df.dtypes)

# 4. Remove duplicate records
print("\nNumber of duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)
print("\nCleaned data:\n", df)
