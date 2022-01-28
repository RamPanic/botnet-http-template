
# Third-party imports

from flask_login import UserMixin

# Local application/library specific imports

from utils.database import database


class User(UserMixin, database.Model):

    __tablename__ = "users"

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(100), unique=True)
    password = database.Column(database.String(42))