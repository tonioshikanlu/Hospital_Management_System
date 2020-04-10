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

def add_patient(conn):
	userInputDid = request.args.get('doctor-id')
	userInputName = request.args.get('patient-name')
	userInputDob = request.args.get('date-of-birth')
	userInputGender = request.args.get('patient-gender')
	userInputNumber = request.args.get('phone-no')
	userInputAddress = request.args.get('phone-address')
	userInputMedHistory = request.args.get('med-history')
	userInputAid = request.args.get('appointment-id')
	if userInputDid == None or userInputName == None or userInputDob == None or userInputGender == None or userInputNumber == None or userInputAddress == None or userInputMedHistory == None or userInputAid == None:
		return
	return execute(conn, "INSERT INTO Patient (did, P_name, DOB, Gender, P_number, P_address, medical_history, aid) VALUES ((?), (?), (?), (?), (?), (?), (?), (?));", (userInputDid,userInputName,userInputDob,userInputGender,userInputNumber,userInputAddress,userInputMedHistory,userInputAid))

def views(bp):
	@bp.route("/patients/add",  methods=['GET', 'POST'])
	def _add_patient():		
		with get_db() as conn:
			rows = add_patient(conn)
		return render_template("add_patient.html", name="Patients")


