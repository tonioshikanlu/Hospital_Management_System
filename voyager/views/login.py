
from collections import namedtuple
import flask_login
from flask import Flask, render_template, request, redirect
from flask import request, url_for
from flask import escape
from flask_login import LoginManager, UserMixin, login_required
from voyager.db import get_db, execute
import config


class User(UserMixin):
    # proxy for a database of users
    c_user = None
    def __init__(self):        
    	User.c_user = None

def Patients(conn):
    return execute(conn, "SELECT d.Doc_email, d.Doc_password FROM Doctor AS d")

boo = User()
def views(bp):
	@bp.route('/login', methods=['GET', 'POST'])
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
		    	if request.form['password'] == doc["Doc_password"] and email == doc["Doc_email"]:
			        c_user = email
			        boo.c_user = c_user
			        user()
			        return render_template("index.html")

		    return 'Unauthorized login'
def user():
	return boo.c_user