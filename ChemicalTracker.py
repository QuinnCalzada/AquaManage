#Kristen Vigna
#Aquamanage
#October 02, 2023
#Edited by: Elise Dezotell
#October 16, 2023
#Create an array that stores user inputed information

from flask import Flask, render_template, request
import sqlite3

DATABASE = '/Users/mdezo/OneDrive - Embry-Riddle Aeronautical University/ERAU/Fall 23/SE 300/AquaManage/AquaManage/Scripts/Chemicals.sql'

app = Flask(__name__)

@app.route('/chemicals')
def index():
    return render_template('chemicals.html')

@app.route('/addchemical', methods = ['POST'])
def addChem():
    chemical_name = request.form['chemical_name']
    chemical_value = request.form['chemical_value']

if __name__ == "__main__":
    app.run(debug = True)

