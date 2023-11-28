from flask import flash, redirect, render_template, url_for, request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from .forms import ResetPassword, CreateAccount, ForgotPassword, ModifyAccountForm
from .utils import hash_new_password
from app import myapp_obj, db, login_manager
from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import ForgotPassword, LoginForm

sort_list = ['AscendingName', 'DescendingName', 'DateCreated']

@myapp_obj.route("/")
@myapp_obj.route("/home.html",methods=['GET', 'POST'])
def home():
    sort_type = request.form.get('sorting')
    print(sort_type)
    if sort_type == 'DateCreated':
        post_notes = Notes.query.order_by(Notes.timestamp.desc()).all()

    if sort_type == 'AscendingName':
        post_notes = Notes.query.order_by(Notes.title).all()

    if sort_type == 'DescendingName':
        post_notes = Notes.query.order_by(Notes.title.desc()).all()

    else:
        print("Issue with Button generator, no input found")
        post_notes = Notes.query.all()

    return render_template('home.html',notes=post_notes,sort_list=sort_list)

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                return redirect(url_for('notePage'))
            else:
                flash('Incorrect Password - Please try again!')
        else:
            flash('User does not exist')

    return render_template('login.html', form=form)

@myapp_obj.route("/notePage", methods=['GET', 'POST'])
@login_required
def notePage():
    form = NoteForm()

    if form.validate_on_submit():
        action = request.form.get('action')

        if action == 'copy':
            # Implement the logic for copying the note
            flash('Note copied successfully!', 'success')
        elif action == 'paste':
            # Implement the logic for pasting the note
            flash('Note pasted successfully!', 'success')
        elif action == 'duplicate':
            # Implement the logic for duplicating the note
            title = form.title.data
            body = form.body.data

            if title.strip():
                if body.strip():
                    n = Notes(title=title, body=body)
                    db.session.add(n)
                    db.session.commit()
                    flash('Note duplicated successfully!', 'success')
        else:
            # Handle other actions or form submissions
            title = form.title.data
            body = form.body.data
            
    if request.method == 'POST':
        try:
            print(f'Title: {request.form["title"]}')
            print(f'Body: {request.form["body"]}')
        except:
            print("No forms here")

        try:
            title = request.form["title"]
            body = request.form["body"]

            if title.strip():
                if body.strip():
                    n = Notes(title=title, body=body)
                    db.session.add(n)
                    db.session.commit()

        # Clear the action field to avoid interference with regular note submission
        form.action.data = ''

        return redirect(url_for('home'))

    return render_template('notePage.html')

@myapp_obj.route("/search.html", methods=['GET', 'POST'])
@login_required
def search():
    print(request.args.get('query'))
    query = request.args.get('query')
    if query:
        search_notes = Notes.query.filter(Notes.title.contains(query) | Notes.body.contains(query))
    else:
        search_notes = Notes.query.all()

    return render_template('search.html',notes=search_notes)

@myapp_obj.route("/<int:note_id>/edit", methods=["GET", "POST"])
def edit_notes(note_id):
    if request.method == "POST":
        if request.form["title"]:
            Notes.query.get(note_id).title = request.form["title"]
            db.session.commit()
            return open_note(note_id)
        else:
            return render_template("edit_note.html", notes=Notes.query.get(note_id))

    post_notes = Notes.query.order_by(Notes.timestamp.desc()).all()
    return render_template('notePage.html', form=form, notes=post_notes)

@myapp_obj.route('/<int:note_id>/rm', methods=['POST'])
def delete_note(note_id):
    rm_note = Notes.query.first_or_404(note_id)
    db.session.delete(rm_note)
    db.session.commit()
    return redirect(url_for('home'))


@myapp_obj.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = CreateAccount()

    if form.validate_on_submit():
        if not form.security_answer.data.isalpha():
            flash('Invalid security answer! Please only enter letters.', 'danger')
            return redirect('createaccount')
        hashed_pw = generate_password_hash(form.password.data, method='scrypt', salt_length=16)
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

@myapp_obj.route("/modifyaccount", methods=['GET', 'POST'])
@login_required
def modifyaccount():
    form = ModifyAccountForm()

    if form.validate_on_submit():
        user = current_user

        # Update username
        if form.username.data:
            user.username = form.username.data

        # Update password
        if form.password.data:
            user.set_password(form.password.data)

        # Update security question and answer
        if form.security_question.data:
            user.security_question = form.security_question.data
        if form.security_answer.data:
            user.security_answer = form.security_answer.data

        # Commit changes to the database
        db.session.commit()

        flash('Account modified successfully!', 'success')
        return redirect(url_for('notePage'))

    return render_template('modifyexistingnote.html', form=form)

  @myapp_obj.route("/forgotpassword", methods=['GET', 'POST'])
def forgotpassword():
    form = ForgotPassword()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_security_question(user.security_question, form.security_question.data):
                if check_security_answer_hash(user.security_answer, form.security_answer.data):

                    return redirect(url_for('resetpassword', username=user.username))
                else:
                    flash('Wrong answer, please try again.')
            else:
                flash('Incorrect security question.')
        else:
            flash('User does not exist.')

    return render_template('forgotpassword.html', form=form)

def check_security_question(user_security_question, provided_security_question):
    return user_security_question == provided_security_question

def check_security_answer_hash(user_security_answer_hash, provided_security_answer):
    return check_password_hash(user_security_answer_hash, provided_security_answer)

@myapp_obj.route("/resetpassword/<username>", methods=['GET', 'POST'])
def resetpassword(username):
    form = ResetPassword()

    if form.validate_on_submit():
        if form.new_password.data != form.confirm_password.data:
            flash('New password and confirmed password do not match. Please try again.')
            return redirect(url_for('resetpassword', username=username))

        user = User.query.filter_by(username=username).first()

        if user:
            new_password_hash = generate_password_hash(form.new_password.data)
            user.password_hash = new_password_hash
            db.session.commit()

            flash('Password reset successful. You can now log in with your new password.')
            return redirect(url_for('login'))
        else:
            flash('User not found. Password reset failed.')

    return render_template('resetpassword.html', form=form)
