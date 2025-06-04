from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    csrf = CSRFProtect(app)

    db.init_app(app)
    login_manager.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
