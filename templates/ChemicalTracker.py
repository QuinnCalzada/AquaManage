#Kristen Vigna
#Aquamanage
#October 02, 2023
#Edited by: Elise Dezotell
#October 16, 2023
#Create an array that stores user inputed information

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask('__main__')

@app.route('/')
def index():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("CREATE spreadsheet")
    cursor.execute("SELECT * FROM spreadsheet")
    data = cursor.fetchall()
    connection.close()
    return render_template('index.html', data=data)

@app.route('/save', methods=['POST'])
def save():
    data = request.form.getlist('data')
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO spreadsheet (column1, column2, column3, column4, column5) VALUES (?, ?, ?, ?, ?)", data)
    connection.commit()
    connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
