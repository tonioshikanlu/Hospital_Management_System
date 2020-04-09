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

# def add_boat(conn):
# 	userInputName = request.args.get('boat-name')
# 	userInputColor = request.args.get('boat-color')
# 	if userInputName == None or userInputColor == None:
# 		return
# 	return execute(conn, "INSERT INTO Boats (name, color) VALUES ((?), (?));", (userInputName,userInputColor))

# def views(bp):
# 	@bp.route("/boats/add",  methods=['GET', 'POST'])
# 	def _add_boats():		
# 		with get_db() as conn:
# 			rows = add_boat(conn)
# 		return render_template("add_boat.html", name="Boats")


