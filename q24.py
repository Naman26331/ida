import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2.5, 5.5, 7.5, 3.5, 8.5],
    "Marks": [35, 42, 48, 55, 60, 68, 72, 80, 85, 92, 45, 63, 77, 52, 83],
})

X = data[["Hours"]]
y = data["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

model = LinearRegression()
model.fit(X_train, y_train)

print("Slope (coefficient) :", round(model.coef_[0], 3))
print("Intercept           :", round(model.intercept_, 3))

y_pred = model.predict(X_test)
print("\nActual marks   :", y_test.tolist())
print("Predicted marks:", np.round(y_pred, 2).tolist())
print("R-squared      :", round(r2_score(y_test, y_pred), 4))
print("Mean squared error:", round(mean_squared_error(y_test, y_pred), 4))

hours = 7.2
predicted = model.predict(pd.DataFrame({"Hours": [hours]}))[0]
print("\nPredicted marks for", hours, "study hours =", round(predicted, 2))

plt.scatter(X, y, color="blue", label="Actual data")
plt.plot(X, model.predict(X), color="red", label="Regression line")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()
