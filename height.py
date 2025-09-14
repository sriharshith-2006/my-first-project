import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
df=pd.read_csv('height-weight.csv')
print(df.head(5))
X=df[["Weight"]]
y=df["Height"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
joblib.dump(model,"height_model.pkl")
print("Model trained and saved as height_model.pkl")
# The model is trained to predict height based on weight and saved as 'heigth_model.pkl'
