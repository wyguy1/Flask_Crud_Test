from flask import Blueprint, render_template

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route("/dashboard")
def dashboard():
    user = "Wyatt"
    notifications = ["Apphoot", "urnann", "more urnan"]
    return render_template("dashboard.html", user=user, notifications=notifications)
