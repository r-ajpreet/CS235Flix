from flask import Blueprint, render_template, redirect, url_for, session, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from password_validator import PasswordValidator

from functools import wraps

import flix.utilities.utilities as utilities
import flix.authentication.services as services
import flix.adapters.repository as repo

# Configure Blueprint.
authentication_blueprint = Blueprint(
    'authentication_bp', __name__, url_prefix='/authentication')


@authentication_blueprint.route('register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    username_not_unique = None

    if form.validate_on_submit():
        # Successful POST, i.e. the username and password have passed validation checking.
        # Use the service layer to attempt to add the new user.
        try:
            services.add_user(form.username.data, form.password.data, repo.repo_instance)

            # All is well, redirect the user to the login page.
            return redirect(url_for('authentication_bp.login'))
        except services.NameNotUniqueException:
            username_not_unique = 'Your username is already taken - please supply another'

    # For a GET or a failed POST request, return the Registration Web page.
    return render_template(
        'authentication/credentials.html',
        title='Register',
        form=form,
        username_error_message=username_not_unique,
        handler_url=url_for('authentication_bp.register'),
        selected_movies=utilities.select_movies(),
        #TODO
    )

# TODO