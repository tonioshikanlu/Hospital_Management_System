from flask import render_template
from flask import request
from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE

def add_sailor(conn):
	userInputName = request.args.get('sailor-name')
	userInputAge = request.args.get('sailor-age')
	userInputExp = request.args.get('sailor-experience')
	if userInputName == None or userInputAge == None or userInputExp == None:
		return
	return execute(conn, "INSERT INTO Sailors (name, age, experience) VALUES ((?), (?), (?));", (userInputName,userInputAge,userInputExp))

def views(bp):
	@bp.route("/sailors/add",  methods=['GET', 'POST'])
	def _add_sailors():		
		with get_db() as conn:
			rows = add_sailor(conn)
		return render_template("add_sailor.html", name="sailors")


