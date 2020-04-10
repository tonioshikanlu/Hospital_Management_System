from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute

def Appointments(conn):
    return execute(conn, "SELECT a.aid, a.did, a.Appointment_date, a.Appointment_time, a.Appointment_type, a.room_number FROM Appointments AS a")

def views(bp):
    @bp.route("/appointments")
    def _appointments():
        with get_db() as conn:
            rows = Appointments(conn)
        return render_template("table.html", name="Appointments", rows=rows)
