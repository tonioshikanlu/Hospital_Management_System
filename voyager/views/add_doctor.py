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

def add_doctor(conn):
    InputPid = request.args.get('patient-id')
    InputName = request.args.get('doctor-name')
    InputNumber = request.args.get('d-phone-no')
    if InputPid == None or InputName == None or InputNumber == None:
        return
    return execute(conn, "INSERT INTO Doctor (pid, Doc_name, Doc_number) VALUES ((?), (?), (?));", (InputPid,InputName,InputNumber))

def views(bp):
	@bp.route("/doctors/add", methods=['GET', 'POST'])
	def _add_doctor():		
		with get_db() as conn:
			rows = add_doctor(conn)
		return render_template("add_doctor.html", name="Doctors")


