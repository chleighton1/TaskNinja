from calendar import HTMLCalendar
from flask import url_for
from flask_login import current_user
from taskninja.models import Users


class UserCalendar(HTMLCalendar):
    def formatday(self, day: int, weekday: int, themonth, year) -> str:
        user = Users.query.filter_by(id=current_user.id).first()
        tasks = self.get_tasks(user, themonth, day)
        if len(tasks) > 4:
            tasks = tasks[:4]
        if day == 0:
            result = '<td class="noday">&nbsp;</td>' # Day outside month
        elif len(tasks) == 0:
            result = f'''<td class="%s d-{themonth}{day}"><a href="{ url_for('calendars.date', month=themonth, day=day, year=year) }">%d</a>''' % (self.cssclasses[weekday], day)
        else:
            result = ''.join([f'''<td class="%s d-{themonth}{day}"><a href="{ url_for('calendars.date', month=themonth, day=day, year=year) }">%d''' % (self.cssclasses[weekday], day), ''.join(task for task in tasks), ('</a></td>')])

        return result


    def get_tasks(self, user, themonth, day):
        tasks = [task.task for task in user.tasks if
                 task.date_scheduled.month == themonth and task.date_scheduled.day == day]
        list = []
        for task in tasks:
            list.append(f'<p class=cal-task>•</p>')
        return list

    def formatweek(self, theweek, themonth, year):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, themonth=themonth, year=year) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="%s calendar-table">' % (
            self.cssclass_month))
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, themonth, year=theyear))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)