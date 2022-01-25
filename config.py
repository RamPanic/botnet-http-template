
""" Flask configuration. """

class Config:

    """ Base config """

    SECRET_KEY = ""
    
    STATIC_FOLDER = 'static'
    
    TEMPLATES_FOLDER = 'templates'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):

    """ Base config production """

    IP_SERVER = ""
    PORT_SERVER = 5000

    ENV = 'production'
    DEBUG = False
    TESTING = False

    """ Database config production """

    MYSQL_USER = ""
    MYSQL_PASSWORD = ""
    MYSQL_DATABASE = ""
    MYSQL_PORT = 3306

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{IP_SERVER}/{MYSQL_DATABASE}"


class DevConfig(Config):

    """ Base config development """

    HOST = "127.0.0.1"
    PORT = 5000

    ENV = 'development'
    DEBUG = True
    TESTING = True

    """ Database config development """

    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DATABASE = "botnet"
    MYSQL_PORT = 3306

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{HOST}/{MYSQL_DATABASE}"


config = {
 
    'dev': DevConfig,
    'prod': ProdConfig

}