from flask import Flask, render_template,request
import joblib
model=joblib.load("economic_model.pkl")
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("economic.html", prediction_text="")
@app.route('/predict', methods=['POST'])
def predict():
    interest_rate = float(request.form['interest_rate'])
    unemployment_rate = float(request.form['unemployment_rate'])
    print("✅ Interest Rate entered:", interest_rate)  # Debug: confirm input received
    print("✅ Unemployment Rate entered:", unemployment_rate)
    prediction = model.predict([[interest_rate, unemployment_rate]])[0]
    print("✅ Prediction result:", prediction)
    index_price = f"Predicted Economic Index Price: {prediction:,.2f}"
    return render_template('economic.html', prediction_text=index_price)
if __name__ == "__main__":
    app.run(debug=True)

