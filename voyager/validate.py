import re

from flask import escape
from flask import render_template

NAME_RE = re.compile('^[A-Za-z ]+$')
INT_RE = re.compile('^[0-9]+$')
DATE_RE = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}$')

def validate_field(name, pattern, value):
    errors = list()
    if value is None:
        errors.append("no {} supplied".format(name))
    elif not pattern.match(value):
        errors.append("{} ({}) did not match {}".format(
            name, escape(value), pattern.pattern))
    return errors

def render_errors(errors):
    return render_template("form_error.html", errors=errors), 400
