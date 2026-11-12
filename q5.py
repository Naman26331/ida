import numpy as np
import time

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print("--- Arithmetic operations ---")
print("a + b  :", a + b)
print("a - b  :", a - b)
print("a * b  :", a * b)
print("a / b  :", a / b)
print("a ** 2 :", a ** 2)
print("a % 3  :", a % 3)

print("\n--- Vectorised operations ---")
big = np.arange(1_000_000)

start = time.time()
loop_result = [x * 2 for x in big]
loop_time = time.time() - start

start = time.time()
vec_result = big * 2
vec_time = time.time() - start

print("Python loop time :", round(loop_time, 4), "seconds")
print("Vectorised time  :", round(vec_time, 4), "seconds")
print("sqrt(a)          :", np.round(np.sqrt(a), 2))
print("exp(b)           :", np.round(np.exp(b), 2))

print("\n--- Aggregation operations ---")
m = np.array([[4, 8, 6], [2, 10, 12], [7, 3, 9]])
print("Matrix:\n", m)
print("Sum  (all)  :", m.sum())
print("Sum  axis=0 :", m.sum(axis=0))
print("Sum  axis=1 :", m.sum(axis=1))
print("Min / Max   :", m.min(), m.max())
print("Cumulative sum of a:", np.cumsum(a))

print("\n--- Statistical operations ---")
data = np.array([12, 15, 11, 18, 20, 15, 14, 19])
print("Data     :", data)
print("Mean     :", np.mean(data))
print("Median   :", np.median(data))
print("Std dev  :", round(np.std(data), 3))
print("Variance :", round(np.var(data), 3))
print("25th, 75th percentile:", np.percentile(data, [25, 75]))
print("Correlation coefficient:", round(np.corrcoef(a, data[:5])[0, 1], 3))
