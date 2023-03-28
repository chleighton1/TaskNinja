import requests
from datetime import datetime
from flask import flash, redirect, render_template, request, url_for, Blueprint
from flask_login import current_user, login_required, login_user, logout_user
from taskninja import bcrypt, db
from taskninja.users.forms import GoalForm, LoginForm, RegistrationForm, TaskForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from taskninja.models import Goal, Task, Users, Quote
from taskninja.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)




@users.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    time = datetime.now()
    task_form = TaskForm()
    goal_form = GoalForm()
    if task_form.validate_on_submit():
        task = Task(task=task_form.task.data, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('users.dashboard'))
    if goal_form.validate_on_submit():
        goal = Goal(goal=goal_form.goal.data, user_id=current_user.id)
        db.session.add(goal)
        db.session.commit()
        return redirect(url_for('users.dashboard'))
    quote = Quote.query.first()
    if (quote is None) or (quote.time.day != datetime.utcnow().day):
        db.session.query(Quote).delete()
        db.session.commit()
        response = requests.get(url="https://zenquotes.io/api/today")
        response.raise_for_status()
        data = response.json()
        print("request sent")
        quote_text = data[0]['q']
        quote_author = data[0]['a']
        new_quote = Quote(quote=quote_text, author=quote_author)
        db.session.add(new_quote)
        db.session.commit()
        quote = Quote.query.first()
    return render_template("dashboard.html", task_form=task_form, goal_form=goal_form, quote=quote, time=time)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! you are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'error')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@users.route("/<int:id>/<type>/delete")
@login_required
def delete(id, type):
    if type == 'goal':
        Goal.query.filter_by(id=id).delete()
        db.session.commit()
    elif type == 'task':
        Task.query.filter_by(id=id).delete()
        db.session.commit()
    # Redirect to previous page
    return redirect(request.referrer)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))
    user = Users.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)