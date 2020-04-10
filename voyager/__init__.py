import os

from flask import Flask

from voyager import db, views
from collections import namedtuple
import flask_login
from flask import Flask, render_template, request, redirect
from flask import request, url_for
from flask import escape
from flask_login import LoginManager, UserMixin, login_required
from voyager.db import get_db, execute

import flask

app = flask.Flask(__name__)
app.secret_key = 'super secret string'
import flask_login

login_manager = flask_login.LoginManager()

login_manager.init_app(app)
views.init_app(app)
# Our mock database.
users = {'foo@bar.tld': {'password': 'secret'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if flask.request.method == 'GET':
#         return '''
#                <form action='login' method='POST'>
#                 <input type='text' name='email' id='email' placeholder='email'/>
#                 <input type='password' name='password' id='password' placeholder='password'/>
#                 <input type='submit' name='submit'/>
#                </form>
#                '''

#     email = flask.request.form['email']
#     if flask.request.form['password'] == users[email]['password']:
#         user = User()
#         user.id = email
#         flask_login.login_user(user)
#         return flask.redirect(flask.url_for('protected'))

#     return 'Bad login'

def Patients(conn):
    return execute(conn, "SELECT d.Doc_email, d.Doc_password FROM Doctor AS d")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    with get_db() as conn:
        rows = Patients(conn)
        email = request.form['email']
        for i in range(len(rows)):
            doc = rows[i]
            print(doc)
            if request.form['password'] == doc["Doc_password"] and email == doc["Doc_email"]:
                user = User()
                user.id = email
                flask_login.login_user(user)
                return redirect(url_for('protected'))

        return 'Bad login'


@app.route('/protected')
@login_required
def index():
    return render_template("index.html")


# @app.route('/protected')
# @flask_login.login_required
# def protected():
#     return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))