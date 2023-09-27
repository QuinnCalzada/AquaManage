from flask import Flask, render_template

app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
	return render_template("dashboard.html")

@app.route("/schedule")
def schedule():
	return render_template("schedule.html")

@app.route("/chemicals")
def chemicals():
	return render_template("chemicals.html")

@app.route("/employees")
def employees():
	return render_template("employees.html")

@app.route("/maintenence")
def maintenence():
	return render_template("maintenence.html")

@app.route("/lessons")
def lessons():
	return render_template("lessons.html")

@app.route("/profile")
def profile():
	return render_template("profile.html")

if __name__ == "__main__":
	app.run(debug = True)