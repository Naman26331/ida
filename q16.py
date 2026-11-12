import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Name":   ["Amit", "Riya", "Karan", "Sara"],
    "Gender": ["Male", "Female", "Male", "Female"],
    "Course": ["BCA", "BBA", "BCom", "BCA"],
    "Grade":  ["B", "A", "C", "A"],
})
print("Original data:\n", df)

# Label encoding
le = LabelEncoder()
df["Course_Label"] = le.fit_transform(df["Course"])
print("\nLabel encoding of Course:\n", df[["Course", "Course_Label"]])
print("Classes:", list(le.classes_))

# Ordinal encoding (when the categories have an order)
df["Grade_Ordinal"] = df["Grade"].map({"C": 1, "B": 2, "A": 3})
print("\nOrdinal encoding of Grade:\n", df[["Grade", "Grade_Ordinal"]])

# One-hot encoding
onehot = pd.get_dummies(df[["Gender", "Course"]], dtype=int)
print("\nOne-hot encoding:\n", onehot)

# One-hot encoding with drop_first to avoid the dummy variable trap
print("\nOne-hot encoding with drop_first=True:\n",
      pd.get_dummies(df["Course"], prefix="Course", drop_first=True, dtype=int))
