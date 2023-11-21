from flask import flash, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .forms import *
from app import myapp_obj, db, login_manager
from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash

@myapp_obj.route("/")
@myapp_obj.route("/home.html")
def home():
    return render_template('home.html')

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                 login_user(user)
                 return redirect(url_for('notes'))
            else:
                 flash('Incorrect Password - Please try again!')
        else:
             flash('User does not exist')
             
    return render_template('login.html', form=form)

@myapp_obj.route("/notes", methods=['GET', 'POST'])
@login_required
def notes():

    form = manageNotes()
    #deleteNote = DeleteNote()
    print(form.validate_on_submit())
    #print(deleteNote.validate_on_submit())

    if form.validate_on_submit():
            u = User(noteBody=form.noteBody.data)
            db.session.add(u)
            db.session.commit()

    return render_template('Notes2.html', form=form)

@myapp_obj.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = CreateAccount()
    print(form.validate_on_submit())

    if form.validate_on_submit():
            if not form.security_answer.data.isalpha():
                 flash('Invalid security answer! Please only enter letters.', 'danger')
                 return redirect('createaccount')
            hashed_pw = generate_password_hash(form.password.data, method='scrypt', salt_length = 16)
            hashed_sa = generate_password_hash(form.security_answer.data, method='scrypt', salt_length=16)
            u = User(username=form.username.data, password_hash=hashed_pw,
                     security_question=form.security_question.data,
                     security_answer=hashed_sa)
            db.session.add(u)
            db.session.commit()

            flash('Account created successfully!', 'success')
            return redirect('login')

    return render_template('create_account.html', form=form)
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)

@myapp_obj.route('/logout')
@login_required
def logout():
     logout_user()
     flash('You have been logged out.', 'info')
     return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))