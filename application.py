from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__, template_folder="templates")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



# @app.route("/", methods=["GET", "POST"])
# def index():
# 	if session.get("notes") is None:
# 		session["notes"] = []
# 	if request.method == "POST":
# 		nota = request.form.get("nota")
# 		session["notas"].append(nota)

# 	return render_template("index.html", notas=session["notas"])


@app.route("/", methods=["GET", "POST"])
def index():
	if session.get("cars") is None:
		session["cars"] = []
	if request.method == "POST":
		car = request.form.get("car")
		session["cars"].append(car)


	return render_template("index.html", cars=session["cars"])


