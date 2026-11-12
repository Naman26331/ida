from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification report:\n",
      classification_report(y_test, y_pred, target_names=iris.target_names))

# Effect of the value of K
print("Accuracy for different values of K:")
for k in range(1, 11, 2):
    model = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    print("K =", k, ": accuracy =", round(model.score(X_test, y_test), 4))

# Predicting a new flower
sample = [[5.1, 3.5, 1.4, 0.2]]
print("\nPredicted species for", sample[0], "=", iris.target_names[knn.predict(sample)[0]])
