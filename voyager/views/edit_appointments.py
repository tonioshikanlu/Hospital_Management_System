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

from . import login


def Edit_appointments(conn):
    
    #currentDoctor = str(login.user())
    aid = request.args.get('aid')
    Appointment_date = request.args.get('appointment-date')
    Appointment_time = request.args.get('appointment-time')
    room_number = request.args.get('room-number')
    print( Appointment_date, "  ", Appointment_time, " ",  room_number )

    if Appointment_date == None or Appointment_time ==  None or \
     room_number == None or aid == None:
        return
    return execute(conn, "UPDATE Appointments\
        SET Appointment_date = (?), \
        Appointment_time = (?), room_number = (?) \
        WHERE aid = (?);",  ( Appointment_date, Appointment_time, room_number, aid))

def views(bp):
    @bp.route("/appointments/edit",  methods=['GET', 'POST'])
    def _edit_appointments():
        with get_db() as conn:
            rows = Edit_appointments(conn)
        return render_template("edit_appointments.html", name="Reschedule Appointments", rows=rows)




