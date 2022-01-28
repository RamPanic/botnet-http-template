
# Standard library imports

# Third-party imports

from flask import Blueprint, render_template

# Local application/library specific imports


noauth = Blueprint("noauth", __name__)


# ================================================================== #
#                                                                    #
#                               Paths                                #
#                                                                    #
# ================================================================== #


@noauth.route("/login", methods=["GET"])
def login():

    return render_template("login.html")