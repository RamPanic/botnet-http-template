
# System imports

from flask_login import LoginManager

# Custom imports

from models.user import User


login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(uuid):

    return User.query.get(uuid)