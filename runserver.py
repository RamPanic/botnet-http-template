
# System imports

from flask import Flask

# Custom imports

from config import config
from routes.bots import bots
from routes.general import general
from schemas.schema import marshmallow
from utils.database import database


# Initial

app = Flask(__name__)

# Using a production configuration

# app.config.from_object(config['prod'])

# Using a development configuration

app.config.from_object(config['dev'])

# Init DB

database.init_app(app)

# Init schema

marshmallow.init_app(app)

# Blueprints

app.register_blueprint(bots)
app.register_blueprint(general)


if __name__ == '__main__':

    app.run(host=app.config["HOST"], port=app.config["PORT"])