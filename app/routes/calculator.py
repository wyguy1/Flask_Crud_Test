from flask import Blueprint, render_template, request

calculator_bp = Blueprint('calculator_bp', __name__)

@calculator_bp.route("/calculator", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        num1 = int(request.form.get("num1", 0))
        num2 = int(request.form.get("num2", 0))
        result = num1 + num2
        return render_template("calculator.html", result=result, num1=num1, num2=num2)
    return render_template("calculator.html")
