from run import app
from taskninja import db


with app.app_context():
    db.create_all()



