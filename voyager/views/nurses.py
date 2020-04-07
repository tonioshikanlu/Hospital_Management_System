from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute


def Nurses(conn):
    return execute(conn, "SELECT n.N_ID, n.Doc_ ID, n.N_name, n.N_number FROM Nurse AS n")

def views(bp):
    @bp.route("/nurses")
    def _nurses():
        with get_db() as conn:
            rows = Nurses(conn)
        return render_template("table.html", name="nurses", rows=rows)
