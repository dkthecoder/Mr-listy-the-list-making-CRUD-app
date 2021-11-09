from flask import Flask
from flask import render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
import mysql.connector 

#flask instance
app = Flask(__name__)

#database connection - FIX
#db = mysql.connector.connect(host="localhost", user="root", password="root", database="flaskmrlistylist")
#cursor = db.cursor()

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
        flash(f'Account created for {form.username.data}! Time to Login', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)