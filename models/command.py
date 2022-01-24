
from datetime import datetime as dt

from utils.database import database

class Command(database.Model):

    __tablename__ = "commands"

    id = database.Column(database.Integer, primary_key=True)
    line = database.Column(database.String(100))
    timestamp = database.Column(database.DateTime, default=dt.now)
    output = database.Column(database.Text)

    bot_uuid = database.Column(database.String(36), database.ForeignKey("bots.uuid"))
    bot = database.relationship("Bot", backref=database.backref("commands", lazy="dynamic"))