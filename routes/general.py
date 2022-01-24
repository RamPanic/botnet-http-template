
from flask import Blueprint
from flask import render_template
from flask import abort

from models.bot import Bot

from schemas.bot import bots_schema

from utils.database import database


general = Blueprint("general", __name__)


@general.route("/", methods=["GET"])
def index():

    return render_template("index.html")


@general.route("/bots", methods=["GET"])
def bot_list():

    bots = Bot.query.all()

    return render_template("list_bots.html", bots=bots)


@general.route("/bots/<uuid>", methods=["GET"])
def get_bot(uuid):

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    return render_template("bot.html", bot=bot)


@general.route("/bots/<uuid>/console", methods=["GET"])
def console(uuid):

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    return render_template("bot_console.html", bot=bot)