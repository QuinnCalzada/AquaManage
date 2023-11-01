from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)

class users(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100))

	def __init__(self, name, email):
		self.name = name
		self.email = email

class chemicalLog(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	chlorine = db.Column(db.Float)
	pH = db.Column(db.Float)
	Alkalinity = db.Column(db.Float)

	def __init__(self, chlorine, pH, Alkalinity):
		self.chlorine = chlorine
		self.pH = pH
		self.Alkalinity = Alkalinity

@app.route("/Dashboard")
def dashboard():
	return render_template("Dashboard.html")

@app.route("/Schedule")
def schedule():
	return render_template("Schedule.html")

@app.route("/Rotation Schedule")
def rotationSchedule():
	return render_template("Rotation Schedule.html")

@app.route("/Open Sub Requests")
def openSubRequests():
	return render_template("Open Sub Requests.html")

@app.route("/Open Shifts")
def openShifts():
	return render_template("Open Shifts.html")


@app.route("/Chemical Log", methods=["POST", "GET"])
def chemicalLog():

	if "chemical_value" in session:
		
		chlorine_value = session["chlorine_value"]
		pH_value = session["pH_value"]
		Alkalinity_value = session["Alkalinity_value"]
		
		return render_template("Chemical Log.html", chlorine_value = chlorine_value, pH_value = pH_value, Alkalinity_value = Alkalinity_value)

	else:

		return render_template("Chemical Log.html")


@app.route("/Add Record", methods=["POST", "GET"])
def addRecord():

	if request.method == "POST":

		chlorine_value = request.form["chlorine_value"]
		pH_value = request.form["pH_value"]
		Alkalinity_value = request.form["Alkalinity_value"]

		session["chlorine_value"] = chlorine_value
		session["pH_value"] = pH_value
		session["Alkalinity_value"] = Alkalinity_value
		
		return redirect(url_for("chemicalLog"))

	else:

		return render_template("Add Record.html")

@app.route("/Contact List")
def contactList():
	return render_template("Contact List.html")

@app.route("/Checklist")
def checklist():
	return render_template("Checklist.html")

@app.route("/Maintenance Request")
def maintenanceRequest():
	return render_template("Maintenance Request.html")

@app.route("/Incident Report", methods=["POST", "GET"])
def incidentReport():
	if request.method == "POST":
		pass
	else:
		return render_template("Incident Report.html")

@app.route("/Patron Count")
def patronCount():
	return render_template("Patron Count.html")

@app.route("/Files")
def files():
	return render_template("Files.html")

@app.route("/Lesson Requests")
def lessonRequests():
	return render_template("Lesson Requests.html")

@app.route("/My Profile")
def myProfile():
	return render_template("My Profile.html")

@app.route("/My Schedule")
def mySchedule():
	return render_template("My Schedule.html")

@app.route("/My Availability")
def myAvailability():
	return render_template("My Availability.html")

@app.route("/My Sub Requests")
def mySubRequests():
	return render_template("My Sub Requests.html")

@app.route("/My Time Off Requests")
def myTimeOffRequests():
	return render_template("My Time Off Requests.html")

@app.route("/My Notifications")
def myNotifications():
	return render_template("My Notifications.html")

@app.route("/Login")
def login():
	return render_template("Login.html")

@app.route("/Logout")
def logout():
	return redirect(url_for("login"))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
	app.run(debug = True)