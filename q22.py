import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame.drop(columns="target")
df["species"] = iris.frame["target"].map(dict(enumerate(iris.target_names)))

# Scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x="petal length (cm)", y="petal width (cm)", hue="species", data=df)
plt.title("Scatter Plot: Petal Length vs Petal Width")
plt.show()

# Correlation coefficients
x = df["petal length (cm)"]
y = df["petal width (cm)"]
r, p = pearsonr(x, y)
print("Pearson correlation (petal length, petal width) =", round(r, 4))
print("p-value =", p)
print("Correlation using Pandas =", round(x.corr(y), 4))

corr = df.drop(columns="species").corr()
print("\nCorrelation matrix:\n", corr.round(2))

# Correlation heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
