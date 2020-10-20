from datetime import date

from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from better_profanity import profanity
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

import flix.adapters.repository as repo
import flix.utilities.utilities as utilities
import flix.movies000.services as services

from flix.authentication.authentication import login_required


# Configure Blueprint.
movies000_blueprint = Blueprint(
    'movies000_bp', __name__)

#TODO