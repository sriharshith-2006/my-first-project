import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
df=pd.read_csv("economic_index.csv")
# Features and target variable
print(df.head(5))
X=df[["interest_rate", "unemployment_rate"]]
y=df["index_price"]
# Create and train the model
model=LinearRegression()
model.fit(X,y)
joblib.dump(model,"economic_model.pkl")
print("Model trained and saved as economic_model.pkl")
