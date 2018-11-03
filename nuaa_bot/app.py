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
app.config['BOT']['SESSION_STORAGE'] = session_storage
robot = WeRoBot(config=app.config['BOT'])
from nuaa_bot.bot import *  # register all handler

# init app
app.add_url_rule(rule='/bot/', endpoint='robot', view_func=make_view(robot), methods=['GET', 'POST'])
