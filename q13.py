import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Name":  ["Amit", "Riya", "Karan", "Sara", "Neha", "Raj"],
    "Age":   [20, 21, np.nan, 22, np.nan, 20],
    "Marks": [85, np.nan, 78, 92, 66, np.nan],
    "City":  ["Delhi", "Mumbai", None, "Delhi", "Pune", "Delhi"],
})
print("Original data:\n", df)

# Detecting missing values
print("\nMissing values per column:\n", df.isnull().sum())
print("Percentage missing:\n", (df.isnull().mean() * 100).round(1))

# Deletion
print("\nRows removed using dropna():\n", df.dropna())
print("\nColumns removed using dropna(axis=1):\n", df.dropna(axis=1))
print("\nRows with missing Marks removed:\n", df.dropna(subset=["Marks"]))

# Imputation
imp = df.copy()
imp["Age"] = imp["Age"].fillna(imp["Age"].median())          # median
imp["Marks"] = imp["Marks"].fillna(imp["Marks"].mean())      # mean
imp["City"] = imp["City"].fillna(imp["City"].mode()[0])      # mode
print("\nAfter imputation (median / mean / mode):\n", imp)

# Other techniques
print("\nForward fill:\n", df.ffill())
print("\nInterpolation of Marks:\n", df["Marks"].interpolate())
print("\nFilled with a constant value:\n", df.fillna({"Age": 0, "Marks": 0, "City": "Unknown"}))
