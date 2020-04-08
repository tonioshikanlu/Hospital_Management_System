from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from voyager.db import get_db, execute
from voyager.validate import validate_field, render_errors
from voyager.validate import NAME_RE, INT_RE, DATE_RE


def Doctors(conn):
    return execute(conn, "SELECT d.did, d.pid, d.Doc_name, d.Doc_number FROM Doctor AS d")

def views(bp):
    @bp.route("/doctors")
    def _doctors():
        with get_db() as conn:
            rows = Doctors(conn)
        return render_template("table.html", name="doctors", rows=rows)