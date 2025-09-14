from flask import Flask,render_template,request
import joblib
app=Flask(__name__)
model=joblib.load("salary_model.pkl")
@app.route('/')
def home():
    return render_template('index.html', prediction_text="") 

@app.route('/predict', methods=['POST'])
def predict():
        years = float(request.form['years'])
        print("✅ Years entered:", years)  # Debug: confirm input received
        prediction = model.predict([[years]])[0]
        print("✅ Prediction result:", prediction)  # Debug: confirm model output

        try:
            salary = f"Predicted Salary: ₹{prediction:,.2f}"
        except Exception as e:
            print("❌ Error during prediction formatting:", e)
            salary = "Error in prediction. Please check your input."
        return render_template('index.html', prediction_text=salary)
if(__name__=="__main__"):
    app.run(debug=True)  # app2.py
