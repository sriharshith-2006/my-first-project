##url routing
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "<h1>Welcome to the Flask App!</h1>"
@app.route('/index', methods=['GET'])
def index():
    return "This is the index page."
@app.route('/success/<int:score>')
def success(score):
    return f"Your score is {str(score)}."
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        name = request.form['name']
        age = request.form['age']
        return f"Name: {name}, Age: {age}"
if __name__ == "__main__":
    app.run(debug=True) # app.py


