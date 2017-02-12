from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'April 14 1988'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name

@app.route('/add/<arg1>/<arg2>')
def add(arg1,arg2):
    x = int(arg1)
    y = int(arg2)
    answer = x + y
    return str(answer)

@app.route('/multiply/<arg1>/<arg2>')
def multiply(arg1,arg2):
    x = float(arg1)
    y = float(arg2)
    answer = x * y
    return str(answer)

@app.route('/favoriteFoods')
def favoriteFoods():
    favoriteFoodsList = ['pizza','tacos','sushi']
    return jsonify(favoriteFoodsList)

if __name__ == "__main__":
    app.run()
