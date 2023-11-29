from flask import flash, redirect, render_template, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from .forms import *
from app import myapp_obj, db, login_manager
from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import ModifyAccountForm


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

            if title.strip():
                if body.strip():
                    n = Notes(title=title, body=body)
                    db.session.add(n)
                    db.session.commit()

        # Clear the action field to avoid interference with regular note submission
        form.action.data = ''

        return redirect(url_for('notePage'))

    post_notes = Notes.query.order_by(Notes.timestamp.desc()).all()
    return render_template('notePage.html', form=form, notes=post_notes)

@myapp_obj.route('/rm/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    rm_note = Notes.query.first_or_404(note_id)
    db.session.delete(rm_note)
    db.session.commit()
    return redirect(url_for('notePage'))

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