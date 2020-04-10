
from flask import Blueprint

# from voyager.views import index
from voyager.views import patients
from voyager.views import doctors
from voyager.views import nurses
from voyager.views import appointments
from voyager.views import view_med_history
from voyager.views import login

# from voyager.views import boats_by_popularity
# from voyager.views import sailors_who_sailed
# from voyager.views import given_sail_date
# from voyager.views import given_color
# from voyager.views import add_sailor
# from voyager.views import add_boat
# from voyager.views import add_voyage



blueprint = Blueprint('views', __name__)
# index.views(blueprint)
patients.views(blueprint)
doctors.views(blueprint)
nurses.views(blueprint)
appointments.views(blueprint)
view_med_history.views(blueprint)
login.views(blueprint)

# boats_by_popularity.views(blueprint)
# sailors_who_sailed.views(blueprint)
# given_sail_date.views(blueprint)
# given_color.views(blueprint)
# add_sailor.views(blueprint)
# add_boat.views(blueprint)
# add_voyage.views(blueprint)


def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')

