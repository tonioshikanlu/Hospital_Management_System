from flask import render_template

def views(bp):
    @bp.route("/")
    def index():
        return render_template("index.html")

