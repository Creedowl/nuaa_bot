import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    os.getenv('DARABASE_USER', 'root'),
    os.getenv('DARABASE_PASSWORD', '1234qwer'),
    os.getenv('DARABASE_HOST', '127.0.0.1'),
    os.getenv('DARABASE_PORT', '3306'),
    os.getenv('DARABASE_DB', 'nuaa_bot'),
)

SQLALCHEMY_TRACK_MODIFICATIONS = True

# webot config
BOT = {
    'TOKEN': os.getenv('webot_token', '2333'),
    'APP_ID': os.getenv('app_id', '2333'),
    'APP_SECRET': os.getenv('app_secret', '2333')
}
