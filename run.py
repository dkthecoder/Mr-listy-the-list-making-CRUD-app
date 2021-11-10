from datetime import timedelta
from flask import Flask
from flask import render_template, url_for, redirect, flash, session
from werkzeug.wrappers import request
from forms import RegistrationForm, LoginForm, MyAccountForm, ListForm, NewListForm
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

#delete list
@app.route('/my_lists/<list_id>/delete', methods=['POST', 'GET'])
def delete_list(list_id):
    cursor.execute("SELECT userid FROM lists WHERE idlists = '{0}';".format(list_id))
    user_id_fetch = cursor.fetchone()
    if user_id_fetch == session['userid']:
        cursor.execute("DELETE FROM items WHERE list_owner = '{0}';".format(list_id))
        cursor.execute("DELETE FROM lists WHERE idlists = '{0}';".format(list_id))
        db.commit()
        flash(f'List Deleted!', 'success')
        return render_template(url_for('my_lists'))
    else:
        flash(f'Error in Deletion', 'danger')
        return render_template(url_for('my_lists'))

#delete list item
@app.route('/list_item/<iditems>/delete', methods=['POST', 'GET'])
def delete_list_item(iditems):
    cursor.execute("SELECT userid FROM lists WHERE idlists = '{0}';".format(iditems))
    user_id_fetch = cursor.fetchone()
    if user_id_fetch == session['userid']:
        cursor.execute("DELETE FROM lists WHERE idlists = '{0}';".format(iditems))
        db.commit()
        flash(f'Item Deleted!', 'success')
        return render_template(url_for('list'))
    else:
        flash(f'Error in Deletion', 'danger')
        return render_template(url_for('list'))


#list (to modify/create list)
#add custom URL
@app.route('/list/<list_id>', methods=['POST', 'GET'])
def list(list_id):
    form = ListForm()
    cursor.execute("SELECT item_name, date_created FROM items WHERE list_owner = '{0}';".format(list_id))
    items_in_list = cursor.fetchall()
    if form.validate_on_submit():
        cursor.execute("INSERT INTO items (iditems, item_name, list_owner, date_created) VALUES(NULL, '{0}', '{1}', NULL);".format(form.list_item.data, list_id))
        db.commit()
        flash(f'New List Created!!', 'success')
        return render_template("list.html", form=form, user_lists = items_in_list)

    return render_template("list.html", form=form, list_items = items_in_list)


#my lists
@app.route('/my_lists', methods=['POST', 'GET'])
def my_lists():
    form = NewListForm()
    if 'loggedin' in session:
        cursor.execute("SELECT list_name, date_created, description, idlists FROM lists WHERE userid = '{0}';".format(session['userid']))
        list_data = cursor.fetchall()

        if form.new_list_name.data!="" and form.new_list_description.data!="":
        #if form.validate_on_submit():
            cursor.execute("INSERT INTO lists (idlists, list_name, userid, description, date_created) VALUES(NULL, '{0}', '{1}', '{2}', NULL);".format(form.new_list_name.data, session['userid'], form.new_list_description.data))
            db.commit()
            flash(f'New List Created!!', 'success')
            return render_template("my_lists.html", form=form, user_lists = list_data)

        return render_template("my_lists.html", form=form, user_lists = list_data)
    else:
        return redirect(url_for('login'))
    

#my account
@app.route('/my_account', methods=['POST', 'GET'])
def my_account():
    form = MyAccountForm()
    form.username.data = session['username']
    form.email.data = session['email']

    #ADD CHECKS FOR NO REPEAT ENTRIES OF user email
    #ADD ERROR FLASHS

    if form.validate_on_submit():
        #checks if field is not empty, updates email in db and session
        if not form.email.data and form.email.data != session['email']:
            cursor.execute("UPDATE users set email = '{0}' WHERE idusers = '{1}';".format(form.email.data, session['userid']))
            db.commit()
            session['email'] = form.email.data
            flash(f'Update successful!', 'success')
            return redirect(url_for('my_account'))
        
        #checks if field is not empty, updates username in db and session
        if not form.username.data and form.username.data != session['username']:
            cursor.execute("UPDATE users set username = '{0}' WHERE idusers = '{1}';".format(form.username.data, session['userid']))
            db.commit()
            session['username'] = form.username.data
            flash(f'Update successful!', 'success')
            return redirect(url_for('my_account'))

        #checks if field is not empty, updates password in db
        if not form.old_password.data and not form.password.data:
            if not form.password.data and form.password.data != session['username']:
                pw = form.password.data.encode("utf-8")
                hash_word = bcrypt.hashpw(pw, bcrypt.gensalt()).decode('utf-8)')
                cursor.execute("UPDATE users set password = '{0}' WHERE idusers = '{1}';".format(hash_word, session['userid']))
                db.commit()
                flash(f'Update successful!', 'success')
                return redirect(url_for('my_account'))
    return render_template("my_account.html", form=form)



@app.route('/logout')
def logout():
    #session.pop('loggedin', None)
    #session.pop('userid', None)
    #session.pop('username', None)
    #session.pop('email', None)
    #session.pop('remember', None)
    session.clear()
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
        check_return = cursor.execute("SELECT COUNT(email) FROM users WHERE email = '{0}'".format(form.email.data))
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
            cursor.execute("INSERT INTO users (idusers, username, email, password) VALUES(NULL, '{0}', '{1}', '{2}')".format(form.username.data, form.email.data, hash_word))
            db.commit()
            flash(f'Account created for {form.username.data}! Time to Login', 'success')
            return redirect(url_for('login'))
    return render_template("register.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)