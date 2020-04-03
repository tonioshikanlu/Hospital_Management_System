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

def sail_date(conn):
	userInput = request.args.get('date')
	return execute(conn, "SELECT DISTINCT s.name FROM Sailors AS s INNER JOIN Voyages AS v ON s.sid = v.sid WHERE v.date_of_voyage = (?)", (userInput,))

def views(bp):
	@bp.route("/sailors/who-sailed-on-date",  methods=['GET', 'POST'])
	def _get_all_sailors_who_sailed_date():	
		with get_db() as conn:
			rows = sail_date(conn)
		return render_template("table.html", name="sailors", rows=rows)