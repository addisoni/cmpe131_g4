from flask import flash, redirect, render_template, url_for, request
from . import myapp_obj
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
from .forms import *
from app import myapp_obj, db, login_manager
from app.models import *
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

#list of sorting note options 
sort_list = ['AscendingName', 'DescendingName', 'DateCreated']

@myapp_obj.route("/")
@myapp_obj.route("/home.html",methods=['GET', 'POST'])
def home():
    # pull sorting name from the HTML file
    sort_type = request.form.get('sorting') 

    # Determine how notes are sorted (displayed)
    if sort_type == 'DateCreated':
        post_notes = Notes.query.order_by(Notes.date_created.desc()).all()
    elif sort_type == 'AscendingName':
        post_notes = Notes.query.order_by(Notes.title).all()
    elif sort_type == 'DescendingName':
        post_notes = Notes.query.order_by(Notes.title.desc()).all()
    else:
        # otherwise just query all available notes to the current user
        post_notes = Notes.query.all()

    folders = Folder.query.all()
    
    # Make sure to pass the form to the template context
    return render_template('home.html', notes=post_notes, sort_list=sort_list, folders=folders, form=NoteForm())

@myapp_obj.route("/createnotes", methods=['GET', 'POST'])
@login_required
def createnotes():
    form = NoteForm()

    # Check if the user has any folders
    folders_exist = current_user.folders.first() is not None

    # If the user doesn't have any folders, flash a message and redirect to the folder creation page
    if not folders_exist:
        flash('You need to create a folder before creating a note.', 'info')
        return redirect(url_for('folderPage'))
    
    # Set choices for the folder dropdown, only including folders created by the current user
    form.folder.choices = [(folder.id, folder.folder_name) for folder in current_user.folders]

    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        folder_id = form.folder.data
        body_html = form.body_html.data
        last_modified = datetime.today().replace(microsecond=0)

        if title.strip() and body.strip():
            n = Notes(title=title, body=body, body_html=body_html, last_modified=last_modified, user_id=current_user.id, folder_id=folder_id)
            db.session.add(n)
            db.session.commit()
        return redirect(url_for('home'))

    return render_template('createnotes.html', form=form)

@myapp_obj.route("/folderPage", methods=['GET', 'POST'])
@login_required
def folderPage():
    form = FolderForm()

    if form.validate_on_submit():
        folder_name = form.title.data
        user_id = current_user.id

        folder = Folder(folder_name=folder_name, user_id=user_id)
        db.session.add(folder)
        db.session.commit()

        flash('Folder created successfully!', 'success')
        return redirect(url_for('folderPage'))
    
    folders = current_user.folders.all()

    return render_template('folderPage.html', form=form, folders=folders)

@myapp_obj.route("/gotofolder/<int:folder_id>", methods=['GET', 'POST'])
@login_required
def gotofolder(folder_id):
    folder = Folder.query.get_or_404(folder_id)
    # Retrieve the sorting option from request.args
    sort_type = request.args.get('sorting')

    # Fetch all folders for the dropdown
    folders = Folder.query.all()
    
    if sort_type == 'DateCreated':
        notes_in_folder = folder.notes.order_by(Notes.date_created.desc()).all()
    elif sort_type == 'AscendingName':
        notes_in_folder = folder.notes.order_by(Notes.title).all()
    elif sort_type == 'DescendingName':
        notes_in_folder = folder.notes.order_by(Notes.title.desc()).all()
    else:
        notes_in_folder = folder.notes.all()

    return render_template('gotofolder.html', folder=folder, sort_list=sort_list, notes=notes_in_folder, folders=folders, form=NoteForm())


@myapp_obj.route('/delete_folder', methods=['POST'])
@login_required
def delete_folder():
    folder_id = request.form.get('folder_id')

    if folder_id:
        folder = Folder.query.get_or_404(int(folder_id))

        # Check if the current user owns the folder
        if folder.user_id == current_user.id:
            # Delete all notes in the folder
            notes_in_folder = folder.notes.all()
            for note in notes_in_folder:
                db.session.delete(note)

            # Delete the folder itself
            db.session.delete(folder)
            db.session.commit()

            flash('Folder and its contents deleted successfully!', 'success')
        else:
            flash('You do not have permission to delete this folder!', 'danger')

    # Redirect to the same page after processing the form
    return redirect(url_for('folderPage'))


@myapp_obj.route('/transfer_note/<int:note_id>', methods=['POST'])
@login_required
def transfer_note(note_id):
    # Get the note from the database
    note = Notes.query.get_or_404(note_id)

    # Check if the current user is the owner of the note
    if note.user_id == current_user.id:
        # Get the folder ID from the form data
        folder_id = request.form.get('folder_id')

        # Check if the folder ID is valid
        folder = Folder.query.get(folder_id)
        if folder:
            # Update the note's folder ID
            note.folder_id = folder.id
            db.session.commit()

            flash('Note transferred to folder successfully!', 'success')
        else:
            flash('Invalid folder selected!', 'danger')

    return redirect(url_for('home'))

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
                 return redirect(url_for('createnotes'))
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
    # create a modifyaccountform instance
    form = ModifyAccountForm()

    # get curr user
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

        # success message
        flash('Account modified successfully!', 'success')

        #redirect to createnotes when done modifying account details
        return redirect(url_for('createnotes'))

    return render_template('modifyaccount.html', form=form)

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

@myapp_obj.route("/<int:note_id>/modify", methods=["GET", "POST"])
def modify_note(note_id):
    # Fetch the note from the database
    my_note = Notes.query.get_or_404(note_id)
    # Create a NoteForm instance and populate it with the existing note data
    form = NoteForm(title=my_note.title, body=my_note.body, old_body=my_note.old_body, body_html=my_note.body_html)

    form.folder.choices = [(folder.id, folder.folder_name) for folder in Folder.query.all()]

    if form.validate_on_submit():
        time_mod = datetime.today().replace(microsecond=0)

        # Update the note data with the form data
        my_note.title = form.title.data
        my_note.body = form.body.data
        my_note.body_html = form.body_html.data
        my_note.last_modified = time_mod

        # Commit the changes to the database
        db.session.commit()

        # Redirect to the home page after successful modification
        return redirect(url_for('home'))

    else:
        my_note.old_body = form.body_html.data
        db.session.commit()

    return render_template('noteModify.html', note=my_note, form=form)

@myapp_obj.route("/<int:note_id>/revisions", methods=["GET", "POST"])
def revision_history(note_id):
    # Fetch the note from the database
    my_note = Notes.query.get_or_404(note_id)
    my_note_copy = Notes.query.get_or_404(note_id)

    # Create a NoteForm instance and populate it with the old note data
    form = NoteForm(title=my_note.title, body=my_note.body, body_html=my_note.body_html, old_body=my_note_copy.old_body)
    print('1')
    if form.validate_on_submit():
        time_mod = datetime.today().replace(microsecond=0)
        my_note.body_html, my_note.old_body = form.old_body.data, form.body_html.data

        # Commit the changes to the database
        db.session.commit()

        # Redirect to the home page after successful modification
        return redirect(url_for('home'))

    return render_template('revisionHistory.html', note=my_note, form=form)

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
    elif request.referrer and 'gotofolder' in request.referrer:
        # Extract folder_id from the referrer URL and redirect to the specific folder
        folder_id = request.referrer.split('/')[-1]
        return redirect(url_for('gotofolder', folder_id=folder_id))
    else:
        return redirect(url_for('home'))

@myapp_obj.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = CreateAccount()

    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username is already taken! Please try a different username.', 'danger')
            return redirect('createaccount')
        elif form.password.data != form.confirm.data:
            flash('Passwords must match! Please try again.', 'danger')
            return redirect('createaccount')
        elif not form.security_answer.data.isalpha():
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
#checks the database if the user exists or not
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
        #checks the database if the user's security question and answers exists
            if check_security_question(user.security_question, form.security_question.data):
                if check_security_answer_hash(user.security_answer, form.security_answer.data):
#if everything checks out, they get sent to the resetpassword link
                    return redirect(url_for('resetpassword', username=form.username.data))
                else:
                    flash('Wrong answer, please try again.')
            else:
                flash('Incorrect security question.')
        else:
            flash('User does not exist.')

    return render_template('forgotpassword.html', form=form)
#checks the database if the security question is right
def check_security_question(user_security_question, provided_security_question):
    return user_security_question == provided_security_question
#checks the database if the security answer is right 
def check_security_answer_hash(user_security_answer_hash, provided_security_answer):
    return check_password_hash(user_security_answer_hash, provided_security_answer)

@myapp_obj.route("/resetpassword/<string:username>", methods=['GET', 'POST'])
def resetpassword(username):
    form = ResetPassword()
#checks if the passwords match when retyping
    if form.validate_on_submit():
        if form.new_password.data != form.confirm_new_password.data:
            flash('New password and confirmed password do not match. Please try again.', 'danger')
        else:
            user = User.query.filter_by(username=username).first()
#when users type the new password and confirms the new password, the database will rewrite the old password with the new password 
            if user:
                new_password_hash = generate_password_hash(form.new_password.data, method='scrypt', salt_length=16)
                user.password_hash = new_password_hash
                db.session.commit()
#when it is successful, it will redirect user to the login page 
                flash('Password reset successful. You can now log in with your new password.', 'success')
                return redirect(url_for('login'))
            else:
                flash('User not found. Password reset failed.', 'danger')

    return render_template('resetpassword.html', form=form, username=username)
