from collections import namedtuple

from flask import render_template
from flask import request
from flask import escape

from voyager.db import get_db, execute

def Patients(conn):
    return execute(conn, "SELECT p.pid, p.did, p.P_name, p.DOB, p.Gender, p.P_number, p.P_address, p.medical_history, p.aid FROM Patient AS p")

def views(bp):
    @bp.route("/patients")
    def _patients():
        with get_db() as conn:
            rows = Patients(conn)
        return render_template("table.html", name="Patients", rows=rows)