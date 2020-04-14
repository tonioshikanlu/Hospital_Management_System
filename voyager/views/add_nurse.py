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

def add_nurse(conn):
    InputName = request.args.get('nurse-name')
    InputNumber = request.args.get('n-phone-no')
    if InputName == None or InputNumber == None:
        return
    return execute(conn, "INSERT INTO Nurse ( N_name, N_number) VALUES ((?), (?));", (InputName, InputNumber))

def views(bp):
	@bp.route("/nurses/add",  methods=['GET', 'POST'])
	def _add_nurse():		
		with get_db() as conn:
			rows = add_nurse(conn)
		return render_template("add_nurse.html", name="Nurses")