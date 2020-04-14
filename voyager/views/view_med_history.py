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

def med_history(conn):
	userInput = request.args.get('medical-history')
	print(userInput)
	#Fix return statement
	return execute(conn, "SELECT DISTINCT p.P_name AS Patient_Name, p.medical_history as Medical_History\
		FROM Patient AS p WHERE p.P_name = (?)", (userInput,))

def views(bp):
	@bp.route("/patients/view-med-history",  methods=['GET', 'POST'])
	def _get_all_med_history():	
		with get_db() as conn:
			rows = med_history(conn)
		return render_template("table.html", name="Patient", rows=rows)