from flask import flash, redirect, render_template, url_for, request
from . import myapp_obj
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
from .forms import *
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

    elif sort_type == 'AscendingName':
        post_notes = Notes.query.order_by(Notes.title).all()

    elif sort_type == 'DescendingName':
        post_notes = Notes.query.order_by(Notes.title.desc()).all()

    else:
        #otherwise just query all available notes to current user
        post_notes = Notes.query.all()

    #notes, sort_list variables are relayed to html file
    return render_template('home.html', notes=post_notes, sort_list=sort_list) 

@myapp_obj.route("/notePage", methods=['GET', 'POST'])
@login_required
def notePage():
    form = NoteForm()

    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        if title.strip() and body.strip():
            n = Notes(title=title, body=body, user_id=current_user.id)
            db.session.add(n)
            db.session.commit()

        return redirect(url_for('home'))

    #Check if no input is in body, if not return an error
    title_default = form.title.data
    body_default = form.body.data
    if title_default == '' or None:
        if body_default != '' or None:
            return redirect(url_for('error'))

    return render_template('notePage.html', form=form)

@myapp_obj.route("/folderPage", methods=['GET', 'POST'])
@login_required
def folderPage():
    form = FolderForm()
    post_folders = Folder.query.order_by(Folder.folder_name.desc()).all()

    if form.validate_on_submit():
        title = form.title.data

        if title.strip():
            n = Folder(folder_name=title, user_id=current_user.id)
            db.session.add(n)
            db.session.commit()

        return redirect(url_for('folderPage'))

    #Check if no input is in body, if not return an error
    title_default = form.title.data
    if title_default == '' or None:
        return redirect(url_for('error'))

    return render_template('folderPage.html', form=form, folders=post_folders)


@myapp_obj.route('/<int:note_id>/gofolder', methods=['GET','POST'])
def gofolder(note_id):
    #Unsure whether to use note.id or folder.id here (or both)
    get_folder = Notes.query.get(note_id)
    print(note_id)
    print(get_folder)
    n = Notes(folder_id=get_folder) #also Notes or Folder call here
    #Either session.add or insert 
    db.session.add(n)
    db.session.commit()
    return redirect(url_for('folderPage'))

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

        #redirect to notepage when done modifying account details
        return redirect(url_for('notePage'))

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

@myapp_obj.route("/<int:note_id>/view", methods=["GET", "POST"])
def view_note(note_id):
    #simply return requested specific note_id details to forefront in HMTL view
    note = Notes.query.get_or_404(note_id)
    return render_template("view_note.html", note=note)

@myapp_obj.route("/<int:note_id>/modify", methods=["GET", "POST"])
def modify_note(note_id):
    #simply return requested specific note_id details to forefront in HMTL view
    #my_note = db.session.execute(db.select(Notes).filter_by(id=note_id)).first()
    my_note = db.get_or_404(Notes,note_id)
    #my_note = Notes.query.filter(Notes.body.contains(request.args.get())
    #my_note = db.session.query(Notes).order_by(note_id)
    print('---')
    print(my_note)
    print('---')
    form = NoteForm()

    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        if title.strip() and body.strip():
            db.session.commit()

        return redirect(url_for('home'))

    #Check if no input is in body, if not return an error
    title_default = form.title.data
    body_default = form.body.data
    if title_default == '' or None:
        if body_default != '' or None:
            return redirect(url_for('error'))

    return render_template('noteModify.html', note=my_note, form=form)

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
