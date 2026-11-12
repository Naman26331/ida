import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.DataFrame({
    "Name":   ["Amit", "Riya", "Karan", "Sara", "Neha", "Raj"],
    "Age":    [18, 22, 20, 25, 19, 30],
    "Marks":  [45, 88, 62, 95, 70, 52],
})
print("Original data:\n", df)

# Normalization (Min-Max scaling to the range 0-1)
df["Marks_MinMax"] = (df["Marks"] - df["Marks"].min()) / (df["Marks"].max() - df["Marks"].min())
scaler = MinMaxScaler()
df["Age_MinMax"] = scaler.fit_transform(df[["Age"]])

# Standardization (Z-score: mean = 0, standard deviation = 1)
df["Marks_Z"] = (df["Marks"] - df["Marks"].mean()) / df["Marks"].std(ddof=0)
std = StandardScaler()
df["Age_Z"] = std.fit_transform(df[["Age"]])

print("\nAfter normalization and standardization:\n", df.round(3))
print("\nMean of Marks_Z =", round(df["Marks_Z"].mean(), 3),
      ", Std of Marks_Z =", round(df["Marks_Z"].std(ddof=0), 3))

# Discretization
df["Grade"] = pd.cut(df["Marks"], bins=[0, 50, 70, 85, 100],
                     labels=["D", "C", "B", "A"])
df["Marks_Quartile"] = pd.qcut(df["Marks"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])
print("\nAfter discretization:\n", df[["Name", "Marks", "Grade", "Marks_Quartile"]])
