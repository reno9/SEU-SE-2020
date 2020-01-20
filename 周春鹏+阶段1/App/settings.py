import os


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)

class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "NMSL"


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "111",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "TrainQuery"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

class TestConfig(Config):
    TESTING = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "111",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "TrainQuery"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

class StagingConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "111",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "TrainQuery"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

class ProductConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "111",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "TrainQuery"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)

envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}

ADMINS = ('reno')
BASE_DIR = "C:\\Users\\reno\\Desktop\\Train"
FILE_PATH_PREFIX = "/static/uploads/icons"
UPLOADS_DIR = os.path.join(BASE_DIR, 'App/static/uploads/icons')