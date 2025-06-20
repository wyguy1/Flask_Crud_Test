from flask import Blueprint, render_template, request

calculator_bp = Blueprint('calculator_bp', __name__)

@calculator_bp.route("/calculator", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = int(request.form.get("num1", 0))
        num2 = int(request.form.get("num2", 0))
        return formulaTable(num1, num2)
    else:
        return render_template("calculator.html")

def formulaTable(x, y):
    return exitProcess(x, y, (x + y))

def exitProcess(x, y, answer):
    return render_template("calculator.html", result=answer, num1=x, num2=y)