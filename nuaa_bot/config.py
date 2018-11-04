import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    os.getenv('DATABASE_USER', 'root'),
    os.getenv('DATABASE_PASSWORD', '1234qwer'),
    os.getenv('DATABASE_HOST', '127.0.0.1'),
    os.getenv('DATABASE_PORT', '3306'),
    os.getenv('DATABASE_DB', 'nuaa_bot'),
)

SQLALCHEMY_TRACK_MODIFICATIONS = True

MESSAGE = {
    'is_authenticated': '已认证',
    'begin_authenticate': '开始认证，请输入姓名，如xxx-2333',
    'format_error': '输入格式错误，请重新输入',
    'message_error': '信息错误',
    'authenticate_success': '认证成功',
    'unauthenticated': '你还未认证，请点击auth来认证身份',
    'subscribe': '欢迎关注，请点击auth认证身份'
}

# WeRoBot config
BOT = {
    'TOKEN': os.getenv('webot_token', '2333'),
    'APP_ID': os.getenv('app_id', '2333'),
    'APP_SECRET': os.getenv('app_secret', '2333')
}
