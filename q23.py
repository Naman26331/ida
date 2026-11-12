import numpy as np
from scipy import stats

# Marks of 20 randomly selected students
marks = np.array([62, 65, 70, 58, 66, 72, 68, 63, 71, 67,
                  64, 69, 73, 61, 66, 70, 65, 68, 74, 60])

# Hypothesis
# H0 : The mean marks of students is 60  (mu = 60)
# H1 : The mean marks of students is not 60 (mu != 60)
mu0 = 60
alpha = 0.05

print("Sample size :", len(marks))
print("Sample mean :", marks.mean())
print("Sample std  :", round(marks.std(ddof=1), 3))

t_stat, p_value = stats.ttest_1samp(marks, mu0)
print("\nt-statistic :", round(t_stat, 4))
print("p-value     :", p_value)
print("Significance level (alpha):", alpha)

if p_value < alpha:
    print("\nResult: Reject H0. The mean marks differ significantly from", mu0)
else:
    print("\nResult: Fail to reject H0. No significant difference from", mu0)
