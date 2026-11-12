import numpy as np
import pandas as pd

np.random.seed(7)
population = pd.DataFrame({
    "RollNo": range(1, 201),
    "Course": np.random.choice(["BCA", "BBA", "BCom"], size=200, p=[0.5, 0.3, 0.2]),
    "Marks": np.random.randint(40, 100, 200),
})

# Stratified sample: 10% from every course (stratum)
stratified = population.groupby("Course").sample(frac=0.10, random_state=1)

# Simple random sample of the same size for comparison
simple = population.sample(n=len(stratified), random_state=1)

comparison = pd.DataFrame({
    "Population %": population["Course"].value_counts(normalize=True) * 100,
    "Stratified %": stratified["Course"].value_counts(normalize=True) * 100,
    "Simple Random %": simple["Course"].value_counts(normalize=True) * 100,
}).round(2)

print("Population size :", len(population))
print("Sample size     :", len(stratified))
print("\nComposition of Course (in percent):")
print(comparison)

print("\nStratified sample (first 5 rows):")
print(stratified.head())
