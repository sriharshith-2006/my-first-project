import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Sample dataset
data = pd.DataFrame({
    "YearsExperience": [1, 2, 3, 4, 5],
    "Salary": [30000, 35000, 40000, 45000, 50000]
})

X = data[["YearsExperience"]]
y = data["Salary"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "linear_model.pkl")
print("Model saved as linear_model.pkl")
