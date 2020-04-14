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

def add_appointment(conn):
	doctorID = request.args.get('doctor-id')
	nurseID = request.args.get('nurse-id')
	patientID = request.args.get('patient-id')
	appointmentDate = request.args.get('appointment-date')
	appointmentTime = request.args.get('appointment-time')
	appointmentType = request.args.get('appointment-type')
	roomNumber = request.args.get('room-number')
	if doctorID == None or nurseID == None or patientID == None or appointmentDate == None or\
	 appointmentTime == None or appointmentType == None or roomNumber == None:
		return
	return execute(conn, "INSERT INTO Appointments (did, nid, pid, Appointment_date, Appointment_time,\
	 Appointment_type, room_number) VALUES ( (?), (?), (?), (?), (?), (?), (?));",\
	  (doctorID,nurseID,patientID,appointmentDate,appointmentTime,appointmentType,roomNumber,))

def views(bp):
	@bp.route("/appointments/add",  methods=['GET', 'POST'])
	def _add_appointment():		
		with get_db() as conn:
			rows = add_appointment(conn)
		return render_template("add_appointments.html", name="Appointments")


