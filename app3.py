from flask import Flask,render_template,request
import joblib
app=Flask(__name__)
model=joblib.load("height_model.pkl")
@app.route('/')
def home():
    return render_template('height_index.html',prediction_text="")
@app.route('/predict',methods=['POST'])
def predict():
    weight=float(request.form['weight'])
    print("✅ Weight entered:", weight)  # Debug: confirm input received
    prediction=model.predict([[weight]])[0]
    print("✅ Prediction result:", prediction)  # Debug: confirm model output
    height=f"predicted Height:{prediction:,.2f}"
    return render_template('height_index.html',prediction_text=height)
if(__name__=="__main__"):
    app.run(debug=True)
