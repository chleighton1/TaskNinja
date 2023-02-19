from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from taskninja.config import Config



# Initialize The Database
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    import taskninja.models
    with app.app_context():
        db.create_all()

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from taskninja.users.routes import users
    from taskninja.calendars.routes import calendars
    from taskninja.main.routes import main
    from taskninja.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(calendars)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
