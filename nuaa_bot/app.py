from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werobot import WeRoBot
from werobot.contrib.flask import make_view
from werobot.session.sqlitestorage import SQLiteStorage

from nuaa_bot import config

app = Flask(__name__)
from nuaa_bot.utils import command  # import all command

app.config.from_object(config)

# init db
db = SQLAlchemy(app)
from nuaa_bot.models import *  # import all models

db.create_all()
migrate = Migrate(app, db)

# init WeRoBot
# session_storage = MySQLStorage(db.engine.raw_connection())
app.config['BOT']['SESSION_STORAGE'] = SQLiteStorage()
robot = WeRoBot(config=app.config['BOT'])
from nuaa_bot.bot import *  # register all handler

# init app
app.add_url_rule(rule='/bot/', endpoint='robot', view_func=make_view(robot), methods=['GET', 'POST'])
