import io
import pandas as pd
import matplotlib.pyplot as plt

# Phase 1: Problem definition
print("Phase 1: Objective - find the average sales of each region\n")

# Phase 2: Data collection / import
raw = """Region,Product,Sales
North,Laptop,45000
South,Laptop,52000
East,Mobile,
West,Mobile,31000
North,Mobile,28000
South,Mobile,35000
East,Laptop,48000
East,Laptop,48000
West,Laptop,50000
"""
df = pd.read_csv(io.StringIO(raw))
print("Phase 2: Data imported")
print(df.head())

# Phase 3: Data inspection
print("\nPhase 3: Data inspection")
print("Shape            :", df.shape)
print("Missing values   :\n", df.isnull().sum())
print("Duplicate rows   :", df.duplicated().sum())
print(df.describe())

# Phase 4: Data cleaning
df = df.drop_duplicates()
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
print("\nPhase 4: Data cleaned, shape =", df.shape)

# Phase 5: Data analysis
result = df.groupby("Region")["Sales"].mean()
print("\nPhase 5: Average sales by region")
print(result)

# Phase 6: Presentation of results
result.plot(kind="bar", color="steelblue", edgecolor="black")
plt.title("Average Sales by Region")
plt.xlabel("Region")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.show()
