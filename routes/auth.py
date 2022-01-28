
# Standard library imports

from werkzeug.security import check_password_hash

# Third-party imports

from flask import ( Blueprint, 
                    redirect,
                    request )

from flask_login import ( login_user,
                          logout_user,
                          login_required )

# Local application/library specific imports

from models.user import User


auth = Blueprint("auth", __name__)


# ================================================================== #
#                                                                    #
#                               Paths                                #
#                                                                    #
# ================================================================== #


@auth.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):

        return redirect("/login")

    login_user(user)

    return redirect("/")


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect("/login")