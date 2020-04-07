
# from collections import namedtuple

# from flask import render_template
# from flask import request
# from flask import escape

# from voyager.db import get_db, execute

# def boats_popularity(conn):
#     return execute(conn, "SELECT b.name, count(Voyages.bid) AS Number_of_Voyages FROM Boats AS b INNER JOIN Voyages WHERE b.bid = Voyages.bid GROUP BY 1 ORDER BY Number_of_Voyages desc")

# def views(bp):
#     @bp.route("/boats/by-popularity")
#     def _boats_popularity():
#         with get_db() as conn:
#             rows = boats_popularity(conn)
#         return render_template("table.html", name="boats", rows=rows)
