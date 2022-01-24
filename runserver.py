
import config

from flask import Flask

from routes.bots import bots
from routes.general import general
from schemas.schema import marshmallow
from utils.database import database

def create_app(config=None):

    app = Flask(__name__)

    return app

# Initial

app = create_app()

# Config

app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init DB

database.init_app(app)

# Init schema

marshmallow.init_app(app)

# Blueprints

app.register_blueprint(bots)
app.register_blueprint(general)


if __name__ == '__main__':

    app.run(host=config.IP_SERVER, port=config.PORT_SERVER, debug=config.DEBUG)