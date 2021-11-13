import pytest
from mysql import connector
from flask import Flask
import json

from flaskr import routes

def test_base_route():
    """
    given an application route, checks to see if return is successful.
    """
    app = Flask(__name__)
    routes(app)
    client = app.test_client()
    url = '/'
    
    responce = client.get(url)
    assert responce.status_code == 200



def test_route_register():
    """
    given data, how does the register page validate
    """
    app = Flask(__name__)
    routes(app)
    client = app.test_client()
    url = '/register'

    test_user = {form.username : 'Ronald Mcdonald', form.email : 'RonaldMcdonald@hotmail.com', form.password : 'pa33w0rd', form.confirm_password : 'pa33w0rd'}

    responce = client.post(url, data=test_user, follow_redirects=True)
    assert responce.status_code == 200

    

def test_route_login():
    app = Flask(__name__)
    routes(app)
    client = app.test_client()
    url = '/login'
    
    test_user = {form.email : 'RonaldMcdonald@hotmail.com', form.password : 'pa33w0rd', form.remember : True}

    responce = client.post(url, data=test_user, follow_redirects=True)
    assert responce.status_code == 200



