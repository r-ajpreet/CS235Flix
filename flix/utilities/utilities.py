from flask import Blueprint, request, render_template, url_for, session

import flix.adapters.repository as repo
import flix.utilities.services as services


# Configure Blueprint.
utilities_blueprint = Blueprint(
    'utilities_bp', __name__)
)

def #TODO