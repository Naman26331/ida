import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))
df = df.drop(columns="target")

print("--- Dataset structure ---")
print("Shape   :", df.shape)
print("Columns :", list(df.columns))
print(df.head())
print("\nData types:\n", df.dtypes)
df.info()

print("\n--- Data quality ---")
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

print("\n--- Summary statistics ---")
print(df.describe())
print("\nMean of each feature by species:\n", df.groupby("species").mean().round(2))

print("\n--- Frequency distributions ---")
print("Species counts:\n", df["species"].value_counts())
print("\nSpecies percentages:\n", (df["species"].value_counts(normalize=True) * 100).round(1))
bins = pd.cut(df["sepal length (cm)"], bins=[4, 5, 6, 7, 8])
print("\nSepal length frequency distribution:\n", bins.value_counts().sort_index())

print("\n--- Correlation ---")
print(df.drop(columns="species").corr().round(2))
