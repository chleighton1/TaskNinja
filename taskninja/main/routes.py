from datetime import datetime
from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route("/")
def home():
    time = datetime.now()
    return render_template('index.html', time=time)