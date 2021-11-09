from flask import Flask
from flask import render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
from flask_login import LoginManager

from mysql import connector
import bcrypt

#flask instance
app = Flask(__name__)

db = connector.connect(host="localhost", user="root", password="root", database="flaskapplist")
cursor = db.cursor()

#for cookies, not secure, change to enviroment variable
app.config['SECRET_KEY'] = '44ea3dab727dfa24322ca91c30854073'

#index html root
@app.route('/')
def index():
    return render_template("index.html")

#my lists
@app.route('/my_lists', methods=['POST', 'GET'])
def my_lists():
    return render_template("my_lists.html")

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

#login
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #checks if email ddress exists
        check_email_exists_query = "SELECT COUNT(email) FROM users WHERE email = '{0}';".format(form.email.data)
        check_return = cursor.execute(check_email_exists_query)
        #if true, checks if password matches
        if check_return == 1:
            stored_hashword = cursor.execute("SELECT COUNT(email) FROM users WHERE email = '{0}';".format(form.email.data))
            if bcrypt.check(form.password.data.encode(), )



        #check if user exsists
        #sql return password hashg to compare to user input, by searching for iunputted username
        #if username isnt returned, print, user doesnt exsist/wrong username
        #else if bcrypt.checkpw(password, hashed):

        flash(f'Login successful! Welcome back!', 'success')
        return redirect(url_for('my_lists'))
    else:
        flash(f'Login unsuccessful! Try again!', 'danger')
    return render_template("login.html", form=form)

#register
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        #creates password hash as string. remove "decode" for bites
        pw = form.password.data.encode()
        hash_word = bcrypt.hashpw(pw, bcrypt.gensalt()).decode('utf-8)')
        #database insert for record, change for mysql
        user_insert_query = "INSERT INTO users (idusers, username, email, password) VALUES(NULL, '{0}', '{1}', '{2}');".format(form.username.data, form.email.data, hash_word)
        cursor.execute(user_insert_query)
        db.commit()
        flash(f'Account created for {form.username.data}! Time to Login', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)