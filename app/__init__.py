from flask import Flask
from app.routes.main import main_bp
from app.routes.dashboard import dashboard_bp
from app.routes.calculator import calculator_bp
from app.routes.weather import weather_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(calculator_bp)
    app.register_blueprint(weather_bp)

    return app