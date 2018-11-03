from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werobot import WeRoBot
from werobot.contrib.flask import make_view
from werobot.session.mysqlstorage import MySQLStorage

from nuaa_bot import config

app = Flask(__name__)
app.config.from_object(config)

# init db
db = SQLAlchemy(app)

# init werobot
session_storage = MySQLStorage(db.engine.raw_connection())
robot = WeRoBot(token='2333', session_storage=session_storage)
from nuaa_bot.bot import *  # register all handler

# init app
app.add_url_rule(rule='/bot/', endpoint='robot', view_func=make_view(robot), methods=['GET', 'POST'])
