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

# def sailors_who_sailed(conn):
# 	userInput = request.args.get('boat-name')
# 	return execute(conn, "SELECT DISTINCT s.name FROM Sailors AS s INNER JOIN Voyages AS v ON s.sid = v.sid INNER JOIN Boats AS b ON b.bid = v.bid WHERE b.name = (?)", (userInput,))

# def views(bp):
# 	@bp.route("/sailors/who-sailed",  methods=['GET', 'POST'])
# 	def _get_all_sailors_who_sailed():
		
# 		with get_db() as conn:
# 			rows = sailors_who_sailed(conn)
# 		return render_template("table.html", name="sailors", rows=rows)