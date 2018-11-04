from nuaa_bot.app import robot
from nuaa_bot.models.user import User


@robot.handler
def hello(message):
    return 'Hello World!'


@robot.key_click('auth')
def auth(message, session):
    open_id = message.source
    query = User.query.filter_by(open_id=open_id)
    if query.count() != 0:
        return '已经认证'
    user = query[0]
    return 'auth'
