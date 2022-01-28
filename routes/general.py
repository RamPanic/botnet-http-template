
# Third-party imports

from flask import ( Blueprint,
                    render_template,
                    abort )

from flask_login import login_required

# Local application/library specific imports

from models.bot import Bot
from schemas.bot import bots_schema
from utils.database import database


general = Blueprint("general", __name__)


# ================================================================== #
#                                                                    #
#                               Paths                                #
#                                                                    #
# ================================================================== #


@general.route("/", methods=["GET"])
@login_required
def index():

    return render_template("index.html")


@general.route("/bots", methods=["GET"])
@login_required
def bot_list():

    bots = Bot.query.all()

    return render_template("list_bots.html", bots=bots)


@general.route("/bots/<uuid>", methods=["GET"])
@login_required
def get_bot(uuid):

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    return render_template("bot.html", bot=bot)


@general.route("/bots/<uuid>/console", methods=["GET"])
@login_required
def console(uuid):

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    return render_template("bot_console.html", bot=bot)