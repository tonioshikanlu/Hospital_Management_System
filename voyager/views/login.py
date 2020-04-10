
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
        pass


c_user = None
def Patients(conn):
    return execute(conn, "SELECT d.Doc_email, d.Doc_password FROM Doctor AS d")

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
		    	print(doc)
		    	if request.form['password'] == doc["Doc_password"] and email == doc["Doc_email"]:
			        # user = User()
			        c_user = email
			        # print(c_user)
			        # flask_login.login_user(user)
			        return render_template("index.html")

		    return 'Unauthorized login'


	# @bp.route('/')
	# def index():
	# 	print(email)
	# 	if not c_user:
	# 		return render_template("form_error.html")
	# 	else:
	# 		return render_template("index.html")