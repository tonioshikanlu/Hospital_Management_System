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

def sail_color(conn):
	userInput = request.args.get('color')
	return execute(conn, "SELECT DISTINCT s.name FROM Sailors AS s INNER JOIN Voyages AS v ON s.sid = v.sid INNER JOIN Boats AS b ON b.bid = v.bid WHERE b.color = (?)", (userInput,))

def views(bp):
	@bp.route("/sailors/who-sailed-on-boat-of-color",  methods=['GET', 'POST'])
	def _get_all_sailors_who_sailed_color():	
		with get_db() as conn:
			rows = sail_color(conn)
		return render_template("table.html", name="sailors", rows=rows)