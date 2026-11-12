import statistics as st
import numpy as np
import pandas as pd

data = [12, 15, 11, 18, 20, 15, 14, 19, 15, 22]
print("Data:", data)

print("\nMean                     :", st.mean(data))
print("Median                   :", st.median(data))
print("Mode                     :", st.mode(data))
print("Range                    :", max(data) - min(data))
print("Variance (sample)        :", round(st.variance(data), 3))
print("Variance (population)    :", round(st.pvariance(data), 3))
print("Std. deviation (sample)  :", round(st.stdev(data), 3))
print("Std. deviation (population):", round(st.pstdev(data), 3))

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
print("\nQ1 (25th percentile)     :", q1)
print("Q2 (50th percentile)     :", q2)
print("Q3 (75th percentile)     :", q3)
print("IQR (Q3 - Q1)            :", q3 - q1)

# Verification with Pandas
s = pd.Series(data)
print("\nUsing Pandas describe():\n", s.describe())
