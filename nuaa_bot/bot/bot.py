from nuaa_bot.app import robot, db, app
from nuaa_bot.models.user import User

mes = app.config['MESSAGE']


@robot.subscribe
def subscribe():
    return mes['subscribe']


@robot.unsubscribe
def unsubscribe(message, session):
    session.clear()
    return ''


@robot.key_click('auth')
def auth_click(message, session):
    if session.get('authenticated'):
        return mes['is_authenticated']
    session['authenticating'] = True
    return mes['begin_authenticate']


@robot.text
def text_handler(message, session):
    content = message.content
    if session.get('authenticating'):
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
    if not session.get('authenticated'):
        return mes['unauthenticated']
    return '嘤嘤嘤'
