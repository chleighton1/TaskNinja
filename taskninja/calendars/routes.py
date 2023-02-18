from datetime import datetime
from flask import redirect, render_template, url_for, Blueprint
from flask_login import current_user, login_required
from taskninja import db
from taskninja.calendars.utils import UserCalendar
from taskninja.users.forms import TaskForm
from taskninja.models import Task


calendars = Blueprint('calendars', __name__)


@calendars.route("/calendars/", defaults={'year': datetime.now().year, 'month': datetime.now().month, 'offset': 0})
@calendars.route("/calendars/<int:year>/<int:month>/<int:offset>", methods=['GET', 'POST'])
@login_required
def calendar(year, month, offset):
    time = datetime.now()
    today = f"{time.month}{time.day}"
    if offset == 2:
        month = month - 1
    else:
        month = month + offset
    if month == 13:
        month = 1
        year = year + 1
    if month == 0:
        month = 12
        year = year - 1
    cal = UserCalendar().formatmonth(theyear=year, themonth=month)
    return render_template('calendar.html', year=year, month=month, title='Calendar', cal=cal, today=today)


@calendars.route("/date/<string:month>/<string:day>/<string:year>", methods=['GET', 'POST'])
@login_required
def date(month, day, year):
    task_form = TaskForm()
    month = int(month)
    day = int(day)
    year = int(year)
    date = datetime(year=year, month=month, day=day)
    if task_form.validate_on_submit():
        task = Task(task=task_form.task.data, user_id=current_user.id, date_scheduled=datetime(year=datetime.now().year, month=month, day=day))
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('calendars.date', month=month, day=day, year=year))
    return render_template('date.html', month=month, day=day, task_form=task_form, date=date)