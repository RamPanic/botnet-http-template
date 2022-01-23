
from datetime import datetime as dt

from utils.database import database


class Bot(database.Model):

    __tablename__ = "bots"

    uuid = database.Column(database.String(36), primary_key=True)
    hostname = database.Column(database.String(100), nullable=True)
    username = database.Column(database.String(100), nullable=True)
    os = database.Column(database.String(50), nullable=True)
    datetime = database.Column(database.DateTime, default=dt.now)
    remote_ip = database.Column(database.String(15), nullable=True)
    local_ip = database.Column(database.String(15), nullable=True)
    state = database.Column(database.String(15), nullable=True)
    location = database.Column(database.String(20), nullable=True)