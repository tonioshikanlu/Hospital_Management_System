
from flask import Blueprint

from voyager.views import patients
from voyager.views import doctors
from voyager.views import nurses
from voyager.views import appointments
from voyager.views import view_med_history
from voyager.views import login
from voyager.views import add_patient
from voyager.views import add_nurse
from voyager.views import add_appointments
from voyager.views import edit_appointments
from voyager.views import delete_appointments

blueprint = Blueprint('views', __name__)
patients.views(blueprint)
doctors.views(blueprint)
nurses.views(blueprint)
appointments.views(blueprint)
view_med_history.views(blueprint)
login.views(blueprint)
add_patient.views(blueprint)
add_nurse.views(blueprint)
add_appointments.views(blueprint)
edit_appointments.views(blueprint)
delete_appointments.views(blueprint)

def init_app(app):
    app.register_blueprint(blueprint)
    app.add_url_rule('/', endpoint='index')