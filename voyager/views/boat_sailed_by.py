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

def boats_sailed(conn):
	userInput = request.args.get('sailor-name')
	print(userInput)
	return execute(conn, "SELECT DISTINCT b.name FROM Boats AS b INNER JOIN Voyages AS v ON b.bid = v.bid INNER JOIN Sailors AS s ON s.sid = v.sid WHERE s.name = (?)", (userInput,))

def views(bp):
	@bp.route("/boats/sailed-by",  methods=['GET', 'POST'])
	def _get_all_boats_sailed():	
		with get_db() as conn:
			rows = boats_sailed(conn)
		return render_template("table.html", name="boats", rows=rows)