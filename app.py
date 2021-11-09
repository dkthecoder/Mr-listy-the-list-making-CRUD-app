from flask import Flask, render_template
import mysql.connector
from datetime import datetime

#flask instance
app = Flask(__name__)

db = mysql.connector.connect(host="localhost",
                            user="root",
                            password="root",
                            database="flaskapplist")

cursor = db.cursor()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    #returns user profile
    def __repf__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Listdescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, unique=False, nullable=False)
    #owner is foreign key
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #returns user profile
    def __repf__(self):
        return f"User('{self.description}', '{self.date_posted}')"

class ItemsList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(120), unique=False, nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    complete = db.Column(db.Boolean, nullable=True)
    #list belong foreign key to list description id
    list_belong = db.Column(db.Integer, db.ForeignKey('Listdescription.id'), nullable=False)

    #returns items belonging to user
    def __repf__(self):
        return f"User('{self.item_name}', '{self.quantity}', '{self.complete}')"


#creation of databse
#id, content, completedm date creates (import datetime)

#index html root
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)