from datetime import timedelta
from flask import Flask
from flask import render_template, url_for, redirect, flash, session
from forms import RegistrationForm, LoginForm
from datetime import timedelta
from mysql import connector
import bcrypt

#flask instance
app = Flask(__name__)

#for cookies, not secure, change to enviroment variable
app.config['SECRET_KEY'] = '44ea3dab727dfa24322ca91c30854073'
app.permanent_session_lifetime = timedelta(days=30)

#load database conector object
db = connector.connect(host="localhost", user="root", password="root", database="flaskapplist")
cursor = db.cursor(buffered=True)

#index html root
@app.route('/')
def index():
    return render_template("index.html")

#my lists
@app.route('/my_lists', methods=['POST', 'GET'])
def my_lists():
    if 'loggedin' in session:
        return render_template("my_lists.html")
    else:
        return redirect(url_for('login'))

    

#list (to modify/create list)
#add custom URL
@app.route('/list', methods=['POST', 'GET'])
def list():
    return render_template("list.html")

#my account
#add custom URL
@app.route('/my_account', methods=['POST', 'GET'])
def my_account():
    return render_template("my_account.html")

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('username', None)
    session.pop('email', None)
    session.pop('remember', None)
    return redirect(url_for('login'))

#login
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if 'loggedin' in session:
        return redirect(url_for('my_lists'))
    if form.validate_on_submit():
        #checks if email address exists
        cursor.execute("SELECT COUNT(email) FROM users WHERE email = '{0}';".format(form.email.data))
        check_return = cursor.fetchone()
        #if true, checks if password matches
        if check_return[0] == 1:
            stored_hashword = cursor.execute("SELECT password FROM users WHERE email = '{0}';".format(form.email.data))
            stored_hashword = cursor.fetchone()
            #bcrypt required encode to unicode characters
            if bcrypt.checkpw(form.password.data.encode("utf-8"), (stored_hashword[0]).encode("utf-8")):
                cursor.execute("SELECT idusers, username, email FROM users WHERE email = '{0}';".format(form.email.data))
                user_return = cursor.fetchone()
                session['loggedin'] = True
                session['userid'] = user_return[0]
                session['username'] = user_return[1]
                session['email'] = user_return[2]
                session.permanent = form.remember.data
                flash(f'Login successful! Welcome back!', 'success')
                return redirect(url_for('my_lists'))
            else:
                flash(f'Login unsuccessful! Check password!', 'danger')
                return render_template("login.html", form=form)
        else:
            flash(f'Login unsuccessful! Check email or signup', 'danger')
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)

#register
@app.route('/register', methods=['POST', 'GET'])
def register():
    if 'loggedin' in session:
        return redirect(url_for('my_lists'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #checks if email address exists
        check_email_exists_query = "SELECT COUNT(email) FROM users WHERE email = '{0}'".format(form.email.data)
        check_return = cursor.execute(check_email_exists_query)
        check_return = cursor.fetchone()
        #if true, checks if password matches
        if check_return == 1:
            flash(f'Email Exists', 'danger')
            return render_template("register", form=form)
        else:
            #creates password hash as string. remove "decode" for bites
            pw = form.password.data.encode("utf-8")
            hash_word = bcrypt.hashpw(pw, bcrypt.gensalt()).decode('utf-8)')
            #database insert for record, change for mysql
            user_insert_query = "INSERT INTO users (idusers, username, email, password) VALUES(NULL, '{0}', '{1}', '{2}')".format(form.username.data, form.email.data, hash_word)
            cursor.execute(user_insert_query)
            db.commit()
            flash(f'Account created for {form.username.data}! Time to Login', 'success')
            return redirect(url_for('login'))
    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)