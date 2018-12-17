from nuaa_bot.app import robot, db, app
from nuaa_bot.models.user import User

mes = app.config['MESSAGE']


@robot.subscribe
def subscribe():
    return mes['subscribe']


@robot.unsubscribe
def unsubscribe(message, session):
    session.clear()
    return 'success'


# @robot.key_click('auth')
# def auth_click(message, session):
#
#     session['authenticating'] = True
#     return mes['begin_authenticate']


@robot.text
def text_router(message, session):
    """
    handle text user sent
    :param message:
    :param session:
    :return:
    """
    content = message.content
    if session.get('authenticating'):
        return user_authenticate(message, session)
    if not session.get('authenticated'):
        if content == 'auth':
            session['authenticating'] = True
            return mes['begin_authenticate']
        return mes['unauthenticated']
    return '嘤嘤嘤'


def user_authenticate(message, session):
    """
    authenticate uesr
    :param message:
    :param session:
    :return: authenticating succeeded or failed
    """
    content = message.content
    info = content.split('-')
    if len(info) == 1:
        return mes['format_error']
    name = info[0]
    student_num = info[1]
    user = User.query.filter_by(name=name, student_num=student_num).all()
    if len(user) == 0:
        return mes['message_error']
    user = user[0]
    user.open_id = message.source
    db.session.add(user)
    db.session.commit()
    del session['authenticating']
    session['authenticated'] = True
    return mes['authenticate_success']
