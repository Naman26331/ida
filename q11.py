import numpy as np
import pandas as pd

np.random.seed(42)
population = pd.DataFrame({
    "RollNo": range(1, 101),
    "Marks": np.random.randint(40, 100, 100),
})
print("Population size:", len(population))
print("Population mean marks:", population["Marks"].mean())

# Simple random sampling
n = 10
srs = population.sample(n=n, random_state=1)
print("\n--- Simple Random Sampling (n = 10) ---")
print(srs)
print("Sample mean marks:", srs["Marks"].mean())

# Systematic sampling
N = len(population)
k = N // n                         # sampling interval
start = np.random.randint(0, k)    # random starting point
systematic = population.iloc[start::k]
print("\n--- Systematic Sampling ---")
print("Sampling interval k =", k, ", starting index =", start)
print(systematic)
print("Sample mean marks:", systematic["Marks"].mean())
