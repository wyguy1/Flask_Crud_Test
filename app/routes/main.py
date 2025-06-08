from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/about")
def about():
    return render_template("about.html")

@main_bp.route("/DevHome")
def dev_home():
    return render_template("DevHome.html")

@main_bp.route("/playmaker")
def playmaker():
    return render_template("play_maker.html")

@main_bp.route("/GameOne")
def game_one():
    return render_template("GameOne.html")

