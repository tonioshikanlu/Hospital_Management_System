from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute
from . import login

def Patients(conn):
	currentDoctor = str(login.user())
	return execute(conn, "SELECT p.pid AS ID , p.P_name AS Name, p.DOB, p.Gender as Gender,\
		p.P_number as Phone_Number, p.P_address AS Address \
    	FROM Patient AS p Join Appointments as a on p.pid = a.pid Join Doctor as d on a.did = d.did\
    	Where d.Doc_email = (?) ", (currentDoctor,))

def views(bp):
    @bp.route("/patients")
    def _patients():
        with get_db() as conn:
            rows = Patients(conn)
        return render_template("table.html", name="Patients", rows=rows)