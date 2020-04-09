# from flask import render_template
# from flask import request
# from collections import namedtuple

# from flask import g
# from flask import escape
# from flask import render_template
# from flask import request

# from voyager.db import get_db, execute
# from voyager.validate import validate_field, render_errors
# from voyager.validate import NAME_RE, INT_RE, DATE_RE

# def add_voyage(conn):
# 	userInputSid = request.args.get('sailor-id')
# 	userInputBid = request.args.get('boat-id')
# 	userInputDate = request.args.get('date-of-voyage')
# 	if userInputSid == None or userInputBid == None or userInputDate == None:
# 		return
# 	return execute(conn, "INSERT INTO Voyages (sid, bid, date_of_voyage) VALUES ((?), (?), (?));", (userInputSid,userInputBid,userInputDate))

# def views(bp):
# 	@bp.route("/voyages/add",  methods=['GET', 'POST'])
# 	def _add_voyages():		
# 		with get_db() as conn:
# 			rows = add_voyage(conn)
# 		return render_template("add_voyage.html", name="voyages")


