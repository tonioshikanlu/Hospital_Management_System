from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute

from . import login

def Appointments(conn):

    currentDoctor = str(login.user())
    return execute(conn, "SELECT a.aid as AID, d.Doc_name AS Doctor_Name, n.N_name as Nurse_Name,\
     p.P_name as Patient_Name, a.Appointment_date AS Appointment_Date, a.Appointment_time AS Time,\
     a.Appointment_type as Appointment_Type , a.room_number as Room_Number\
     FROM Appointments as A \
    	Join Nurse as n ON a.nid = n.nid \
    	Join Doctor as d ON a.did = d.did \
    	Join Patient as p ON a.pid = p.pid \
        Where d.Doc_email = (?) ", (currentDoctor,))

def views(bp):
    @bp.route("/appointments")
    def _appointments():
        with get_db() as conn:
            rows = Appointments(conn)
        return render_template("appointments.html", name="Appointments", rows=rows)
