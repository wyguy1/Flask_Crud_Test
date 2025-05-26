from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/DevHome")
def DevHome():
    return render_template("DevHome.html")

@app.route("/dashboard")
def dashboard():
    user = "Wyatt"
    notifications = ["Apphoot", "urnann", "more urnan"]
    return render_template("dashboard.html",user = user, notifications = notifications)

@app.route("/calculator", methods = ["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = int(request.form.get("num1", 0))
        num2 = int(request.form.get("num2", 0))
        num3 =  num1 + num2
        return render_template("calculator.html", result = num3, num1 = num1, num2 = num2)
    else:
        return render_template("calculator.html")

@app.route("/playmaker")
def play_maker():
    return render_template("play_maker.html")
@app.route("/GameOne")
def GameOne():
    return render_template("GameOne.html")

if __name__ == "__main__":
    app.run(debug=True)
