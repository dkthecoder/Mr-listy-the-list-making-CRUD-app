from datetime import timedelta
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

#flask instance
app = Flask(__name__)
app.config.update(DEBUG=True, WTF_CSRF_ENABLED=True)
#app.config['SECRET_KEY'] = '44ea3dab727dfa24322ca91c30854073'

# Get environment variables for secrete key
SECRET_KEY = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = 'SECRET_KEY'

#for cookies, not secure, change to enviroment variable
app.permanent_session_lifetime = timedelta(days=30)

csrf = CSRFProtect()
csrf.init_app(app)

from flaskr import routes

