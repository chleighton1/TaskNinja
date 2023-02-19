from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from taskninja.config import Config
from whitenoise import WhiteNoise
import os



# Initialize The Database
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from taskninja.users.routes import users
        from taskninja.calendars.routes import calendars
        from taskninja.main.routes import main
        from taskninja.errors.handlers import errors
        app.register_blueprint(users)
        app.register_blueprint(calendars)
        app.register_blueprint(main)
        app.register_blueprint(errors)

    WHITENOISE_MAX_AGE = 31536000 if not app.config["DEBUG"] else 0

    # configure WhiteNoise
    app.wsgi_app = WhiteNoise(
        app.wsgi_app,
        root=os.path.join(os.path.dirname(__file__), "staticfiles"),
        prefix="assets/",
        max_age=WHITENOISE_MAX_AGE,
    )

    return app
