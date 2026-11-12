import pandas as pd

marks = pd.Series([45, 52, 48, 50, 55, 47, 53, 49, 51, 120, 5, 46], name="Marks")
print("Data:", marks.tolist())

Q1 = marks.quantile(0.25)
Q3 = marks.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("\nQ1 =", Q1, ", Q3 =", Q3, ", IQR =", IQR)
print("Lower bound =", lower, ", Upper bound =", upper)

# Detection
outliers = marks[(marks < lower) | (marks > upper)]
print("\nOutliers detected:", outliers.tolist())

# Treatment 1: removal
removed = marks[(marks >= lower) & (marks <= upper)]
print("\nAfter removing outliers:", removed.tolist())
print("Mean before =", round(marks.mean(), 2), ", after =", round(removed.mean(), 2))

# Treatment 2: capping (winsorisation)
capped = marks.clip(lower=lower, upper=upper)
print("\nAfter capping outliers:", capped.tolist())

# Treatment 3: replacing with the median
replaced = marks.where((marks >= lower) & (marks <= upper), marks.median())
print("After replacing with median:", replaced.tolist())
