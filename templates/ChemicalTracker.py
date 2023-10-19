#Kristen Vigna
#Aquamanage
#October 02, 2023
#Edited by: Elise Dezotell
#October 16, 2023
#Create an array that stores user inputed information

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Define the database connection
db = mysql.connector.connect(
    host="AquaManage",
    user="root",
    password="Doodles7",
    database="chemical_data"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM chemical_data")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    value = float(request.form['value'])
    cursor = db.cursor()
    cursor.execute("INSERT INTO chemical_data (name, value) VALUES (%s, %s)", (name, value))
    db.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
