from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from taskninja import db, login_manager
from flask_login import UserMixin
from flask import current_app


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


# Create Models
class Quote(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(120), unique=True, nullable=False)
    author = db.Column(db.String(60), unique=True, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Quote('{self.quote}', '{self.author}')"


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)
    goals = db.relationship('Goal', backref='user', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Users.query.get(user_id)

    def __repr__(self):
        return f"User('{self.email}', '{self.image_file}')"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_scheduled = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_completed = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Task('{self.task}', '{self.date_created}')"


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    date_scheduled = db.Column(db.DateTime, nullable=True)
    date_completed = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Goal('{self.goal}', '{self.date_created}')"


