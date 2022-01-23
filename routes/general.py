
from flask import Blueprint, render_template

from models.bot import Bot

from schemas.bot import bots_schema

from utils.database import database


general = Blueprint("general", __name__)

@general.route("/list")
def bot_list():

	bots = Bot.query.all()

	return render_template("list_bots.html", bots=bots)