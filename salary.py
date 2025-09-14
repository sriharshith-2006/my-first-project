import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
data={
    "years":[1,2,3,4,5],
    "Salary":[40000,50000,60000,70000,80000]
}
df=pd.DataFrame(data)
# Features and target variable
print(df.head(5))
X=df[["years"]]
y=df["Salary"]
# Create and train the model
model=LinearRegression()
model.fit(X,y)
joblib.dump(model,"salary_model.pkl")
print("Model trained and saved as salary_model.pkl")