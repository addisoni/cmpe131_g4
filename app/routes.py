from flask import flash, redirect, render_template, url_for, request
from . import myapp_obj
from .models import User
from flask import flash, redirect, render_template, url_for, request, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from .forms import *
from .utils import hash_new_password
from app import myapp_obj, db, login_manager
from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash

#list of sorting note options 
sort_list = ['AscendingName', 'DescendingName', 'DateCreated']

@myapp_obj.route("/")
@myapp_obj.route("/home.html",methods=['GET', 'POST'])
def home():
    #pull sorting name from html file
    sort_type = request.form.get('sorting') 
    #Determine how notes are sorted (displayed)
    if sort_type == 'DateCreated':
        post_notes = Notes.query.order_by(Notes.timestamp.desc()).all()
        print(post_notes)

    elif sort_type == 'AscendingName':
        post_notes = Notes.query.order_by(Notes.title).all()
        print(post_notes)

    elif sort_type == 'DescendingName':
        post_notes = Notes.query.order_by(Notes.title.desc()).all()

    else:
        #otherwise just query all available notes to current user
        post_notes = Notes.query.all()

    #notes, sort_list variables are relayed to html file
    return render_template('home.html',notes=post_notes,sort_list=sort_list) 

@myapp_obj.route("/notePage", methods=['GET', 'POST'])
@login_required
def notePage():
    form = NoteForm()
    #pull title and body data to check for input (error check)
    title_default = form.title.raw_data 
    body_default = form.body.raw_data

    if form.validate_on_submit():
        #pull sorting name from html file
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
                    n = Notes(title=formatted_title, body=body, user_id=current_user.id)
                    db.session.add(n)
                    db.session.commit()
                    flash('Note duplicated successfully!', 'success')

        else:
            #only submit queries remain, prep to save note to database
            title = form.title.data
            body = form.body.data

            if title.strip():
                if body.strip():
                    #get the title, body, and specified user to add to database
                    n = Notes(title=title, body=body, user_id=current_user.id)
                    db.session.add(n)
                    db.session.commit()

        #Clear the action field to avoid interference with regular note submission
        form.action.data = ''

        return redirect(url_for('home'))

    #return error page if note titles were attempted to be saved, copied, etc. without a string inputted 
    if title_default == [""] or None:
        if body_default != ["<p><br></p>"] or None:
            return redirect(url_for('error'))

    #if nothing else, proceed back to notePage
    return render_template('notePage.html', form=form)

#Error page
@myapp_obj.route("/error", methods=['GET', 'POST'])
def error():
    return render_template('error.html')


@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Queries the database for user with the provided username
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # checks if password provided by user matches the hashed password in the database
            if check_password_hash(user.password_hash, form.password.data):
                 login_user(user)
                 # if it matches, redirect to user's note page
                 return redirect(url_for('notePage'))
            else:
                # if it does not match, flash a message
                 flash('Incorrect Password - Please try again!')
        else:
            # if they input a username that isn't in the database, flash message
             flash('User does not exist')

    return render_template('login.html', form=form)

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
            hashed_sa = hashed_sa = generate_password_hash(form.security_answer.data)
            user.security_answer = hashed_sa

        # Commit changes to the database
        db.session.commit()

        flash('Account modified successfully!', 'success')
        return redirect(url_for('notePage'))

    return render_template('modifyexistingnote.html', form=form)

@myapp_obj.route("/search.html", methods=['GET', 'POST'])
@login_required
def search():
    #pull data from search field (query)
    query = request.args.get('query')
    #If there is a value for query, return with parsed string
    if query:
        search_notes = Notes.query.filter(Notes.title.contains(query) | Notes.body.contains(query))
    else:
        #else return all available notes to the user
        search_notes = Notes.query.all()

    return render_template('search.html',notes=search_notes)

@myapp_obj.route("/<int:note_id>/view", methods=["GET", "POST"])
def view_note(note_id):
    #simply return requested specific note_id details to forefront in HMTL view
    note = Notes.query.get_or_404(note_id)
    return render_template("view_note.html", note=note)

@myapp_obj.route('/<int:note_id>/rm', methods=['POST'])
def delete_note(note_id):
    #Given the for loop in the html file, this will pull the corresponding ID based on the specific POST request region and delete the file from the database
    #after database entry is deleted, refresh to the main home page (with recently deleted note no longer present)
    rm_note = Notes.query.first_or_404(note_id)
    db.session.delete(rm_note)
    db.session.commit()
    return redirect(url_for('home'))

@myapp_obj.route('/<int:note_id>/toggle_visibility', methods=['POST'])
def toggle_visibility(note_id):
    # Queries database for the note with the attached note_id or return an 404 error if none found
    note = Notes.query.get_or_404(note_id)

    # Checks if the current user is the owner of the note
    if note.user_id == current_user.id:
        # Toggles visibility status (public/private) of the note
        note.public = not note.public
        # Commits the change to the database (0 means private (by default) and 1 means public)
        db.session.commit()

    # Checks for a referrer and if 'search' is also in the referrer URL
    if request.referrer and 'search' in request.referrer:
        return redirect(url_for('search'))
    else:
        return redirect(url_for('home'))

@myapp_obj.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = CreateAccount()
    print(form.validate_on_submit())

    if form.validate_on_submit():
        if not form.security_answer.data.isalpha():
            flash('Invalid security answer! Please only enter letters.', 'danger')
            return redirect('createaccount')
        
        # Hashes both the password and security answer using scrypt
        hashed_pw = generate_password_hash(form.password.data, method='scrypt', salt_length = 16)
        hashed_sa = generate_password_hash(form.security_answer.data, method='scrypt', salt_length=16)

        # Creates a new user with provided data and commits to the database
        u = User(username=form.username.data, password_hash=hashed_pw,
            security_question=form.security_question.data,
            security_answer=hashed_sa)
        db.session.add(u)
        db.session.commit()

        # Flashes a message to user when they successfully create their account and redirects them to the login page to login
        flash('Account created successfully!', 'success')
        return redirect('login')
    return render_template('create_account.html', form=form)

@myapp_obj.route('/logout')
@login_required
def logout():
    # Simply logs out the user and flashes a message to them
     logout_user()
     flash('You have been logged out.', 'info')
     return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@myapp_obj.context_processor
def utility_processor():
    def get_username(user_id):
        # Queries the database for a user with the provided user_id attached to them then returns the user if they exist, otherwise
        # return none
        user = User.query.get(user_id)
        return user.username if user else None
    return dict(get_username=get_username)

@myapp_obj.route("/forgotpassword", methods=['GET', 'POST'])
def forgotpassword():
    form = ForgotPassword()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_security_question(user.security_question, form.security_question.data):
                if check_security_answer_hash(user.security_answer, form.security_answer.data):

                    return redirect(url_for('resetpassword'))
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

@myapp_obj.route("/resetpassword", methods=['GET', 'POST'])
def resetpassword():
    form = ResetPassword()

    if form.validate_on_submit():
        if form.new_password.data != form.confirm_new_password.data:
            flash('New password and confirmed password do not match. Please try again.', 'danger')
        else:
            username = form.username.data
            user = User.query.filter_by(username=username).first()

            if user:
                new_password_hash = generate_password_hash(form.new_password.data, method='scrypt', salt_length=16)
                user.password_hash = new_password_hash
                db.session.commit()

                flash('Password reset successful. You can now log in with your new password.', 'success')
                return redirect(url_for('login'))
            else:
                flash('User not found. Password reset failed.', 'danger')

    return render_template('resetpassword.html', form=form)
