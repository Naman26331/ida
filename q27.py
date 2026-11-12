import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

# Finding a suitable number of clusters (elbow method)
print("Inertia for different values of K:")
for k in range(1, 7):
    print("K =", k, ": inertia =", round(KMeans(n_clusters=k, n_init=10, random_state=1).fit(X).inertia_, 2))

kmeans = KMeans(n_clusters=3, n_init=10, random_state=1)
labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

print("\nCluster sizes:", [int((labels == c).sum()) for c in range(3)])
print("Centroids:\n", centroids.round(2))

# Visualisation using petal length and petal width
plt.figure(figsize=(7, 5))
plt.scatter(X[:, 2], X[:, 3], c=labels, cmap="viridis", s=40)
plt.scatter(centroids[:, 2], centroids[:, 3], c="red", marker="X", s=250,
            edgecolor="black", label="Centroids")
plt.title("K-Means Clustering (K = 3)")
plt.xlabel("Petal length (cm)")
plt.ylabel("Petal width (cm)")
plt.legend()
plt.show()
