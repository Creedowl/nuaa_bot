import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    os.getenv('database_user', 'root'),
    os.getenv('database_password', '1234qwer'),
    os.getenv('database_host', '127.0.0.1'),
    os.getenv('database_port', '3306'),
    os.getenv('database_db', 'nuaa_bot'),
)

SQLALCHEMY_TRACK_MODIFICATIONS = True
