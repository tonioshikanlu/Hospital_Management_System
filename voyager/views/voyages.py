from collections import namedtuple

from flask import render_template
from flask import request

from voyager.db import get_db, execute


def Voyages(conn):
    return execute(conn, "SELECT v.sid, v.bid, v.date_of_voyage FROM Voyages AS v")

def views(bp):
    @bp.route("/voyages")
    def _voyages():
        with get_db() as conn:
            rows = Voyages(conn)
        return render_template("table.html", name="voyages", rows=rows)
