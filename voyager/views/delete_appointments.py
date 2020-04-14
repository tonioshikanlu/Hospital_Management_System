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

def Delete_appointments(conn):    
    aid = request.args.get('aid')
    Doctor_name = request.args.get('doc-name')
    print( aid, "  ", Doctor_name )
    if aid == None or Doctor_name ==  None:
        return
    return execute(conn, "DELETE FROM Appointments WHERE aid = (?);"\
        , ( aid,))

def views(bp):
    @bp.route("/appointments/delete",  methods=['GET', 'POST'])
    def _delete_appointments():
        with get_db() as conn:
            rows = Delete_appointments(conn)
        return render_template("delete_appointments.html", name="Delete Appointments", rows=rows)