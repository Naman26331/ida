from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("\nConfusion matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification report:\n",
      classification_report(y_test, y_pred, target_names=iris.target_names))

# Predicting a new flower with class probabilities
sample = [[6.3, 2.9, 5.6, 1.8]]
print("Predicted species:", iris.target_names[nb.predict(sample)[0]])
print("Class probabilities:")
for name, prob in zip(iris.target_names, nb.predict_proba(sample)[0]):
    print("  ", name, ":", round(prob, 4))
