from flask import Flask, render_template, request, jsonify
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/enternew')
def enternew():
    return render_template('food.html')

@app.route('/addfood', methods = ['POST'])
def addfood():
    connection = sql.connect('database.db')
    cursor = connection.cursor()

    try:
        name = request.form['name']
        calories = request.form['calories']
        cuisine = request.form['cuisine']
        is_vegetarian = request.form['is_vegetarian']
        is_gluten_free = request.form['is_gluten_free']

        #connection.execute('CREATE TABLE foods (name TEXT, calories TEXT, cuisine TEXT, is_vegetarian TEXT, is_gluten_free TEXT)')
        cursor.execute('INSERT INTO foods (name,calories,cuisine,is_vegetarian,is_gluten_free) VALUES (?,?,?,?,?)', (name,calories,cuisine,is_vegetarian,is_gluten_free))
        connection.commit()
        message = 'Record Successfully Added!'
        connection.close()
    except:
        connection.rollback()
        connection.close()
        message = 'Error in insert operation'
    finally:
        return render_template('result.html', message=message)

@app.route('/favorite/')
def favorite():
    connection = sql.connect('database.db')
    cursor = connection.cursor()

    favFood = ('pizza',)
    try:
        cursor.execute('SELECT * FROM foods WHERE name = ?', favFood)
        foodList = cursor.fetchall()
        message = foodList #jsonify(foodList)
    except:
        message = 'Failure! Something went wrong with the request.'
    finally:
        return jsonify(message)

@app.route('/search', methods = ['GET'])
def search():
    connection = sql.connect('database.db')
    cursor = connection.cursor()

    try:
        name = request.args.get('name')
        data = (name,)
        cursor.execute('SELECT * FROM foods WHERE name = ?',data)
        foodList = cursor.fetchall()
        message = foodList
    except:
        message = 'Failure! Something went wrong.'
    finally:
        return jsonify(message)

@app.route('/drop')
def drop():
    connection = sql.connect('database.db')
    cursor = connection.cursor()

    try:
        cursor.execute('DROP TABLE IF EXISTS "foods"')
        message = 'dropped'
    except:
        message = 'not dropped. Something went wrong.'
    finally:
        return message

if __name__ == "__main__":
    app.run()
