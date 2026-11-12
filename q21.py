import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))
features = df.drop(columns=["target", "species"])

fig, axes = plt.subplots(2, 3, figsize=(16, 9))

# 1. Bar chart (Matplotlib)
subjects = ["Python", "Maths", "English", "DBMS"]
marks = [88, 76, 81, 69]
axes[0, 0].bar(subjects, marks, color="skyblue", edgecolor="black")
axes[0, 0].set_title("Bar Chart")
axes[0, 0].set_ylabel("Marks")

# 2. Line chart (Matplotlib)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 135, 128, 150, 170, 165]
axes[0, 1].plot(months, sales, marker="o", color="green")
axes[0, 1].set_title("Line Chart")
axes[0, 1].set_ylabel("Sales")

# 3. Count plot (Seaborn)
sns.countplot(x="species", data=df, ax=axes[0, 2])
axes[0, 2].set_title("Count Plot")

# 4. Histogram (Seaborn)
sns.histplot(df["sepal length (cm)"], bins=15, kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Histogram")

# 5. Box plot by species (Seaborn)
sns.boxplot(x="species", y="petal length (cm)", data=df, ax=axes[1, 1])
axes[1, 1].set_title("Box Plot")

# 6. Box plot of all features (Seaborn)
sns.boxplot(data=features, ax=axes[1, 2])
axes[1, 2].set_title("Box Plot of All Features")
axes[1, 2].tick_params(axis="x", labelrotation=20)

plt.tight_layout()
plt.show()
