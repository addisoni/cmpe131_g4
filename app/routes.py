from flask import *
from .forms import *
from app import *
from app.models import User

@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    name = 'Carlos'
    books = [ {'author': 'authorname1',
                'book':'bookname1'},
             {'author': 'authorname2',
              'book': 'bookname2'}]
    return render_template('hello.html',name=name, books=books)

@myapp_obj.route("/hello")
def hello():
    return "Hello World!"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f'Here we print to terminal the input {form.username.data} and {form.password.data}')
        flash(f'Here we use flash to HTML with the input {form.username.data} and {form.password.data}')
        found_user = User.query.filter_by(username=form.username.data).first()
        print(found_user)

        return redirect('/')
    return render_template('login.html', form=form)

@myapp_obj.route("/createaccount", methods=['GET', 'POST'])
def createaccount():
    form = CreateAccountForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
            print('do something')
            print(f'this is the username of the user {form.username.data}')
            print(f'this is the password of the user {form.password.data}')
            u = User(username=form.username.data, password=form.password.data,
                     email=form.email.data)
            db.session.add(u)
            db.session.commit()
            return redirect('/')

    return render_template('create_account.html', form=form)
@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)

