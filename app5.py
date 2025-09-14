import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request
##WSGI application
with open("model.pkl","rb") as f:
    model=pickle.load(f)
with open("vectorizer.pkl","rb") as f:
    vectorizer=pickle.load(f)
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        message=request.form["message"]
        data=[message]
        vect=vectorizer.transform(data)
        my_prediction=model.predict(vect)[0]
        result="spam" if my_prediction==0 else "not spam"
        return render_template('naive.html',prediction=result)
    else:
        return render_template('naive.html',prediction="")
if __name__=="__main__":
    app.run(debug=True)  # app5.py