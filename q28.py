import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data[::5]                                     # every 5th row (30 samples)
names = [iris.target_names[t][:3] for t in iris.target[::5]]

# Agglomerative clustering using Ward linkage
Z = linkage(X, method="ward")

plt.figure(figsize=(12, 5))
dendrogram(Z, labels=names, leaf_rotation=90, leaf_font_size=9)
plt.title("Hierarchical Clustering Dendrogram (Ward linkage)")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()

# Cutting the dendrogram into 3 clusters
clusters = fcluster(Z, t=3, criterion="maxclust")
print("Cluster number of each sample:")
print(clusters)
print("Number of samples in each cluster:")
for c in sorted(set(clusters)):
    print("Cluster", c, ":", list(clusters).count(c))
