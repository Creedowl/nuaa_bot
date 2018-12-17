from datetime import datetime
import json
from json import JSONDecodeError

import click

from nuaa_bot.app import app


@app.cli.command(short_help='import user')
@click.argument('filename')
def import_user(filename):
    mes = app.config['MESSAGE']
    try:
        from nuaa_bot.app import db
        from nuaa_bot.models.user import User
        f = open(filename, 'r')
        data = json.loads(f.read())
        total = len(data)
        sum = 0
        print(mes['begin_import_user'])
        for index, item in enumerate(data):
            print(mes['handling_user'].format(index, total), end='\r')
            if len(User.query.filter_by(student_num=item[1]).all()) != 0:
                print(mes['user_existed'], end='\r')
                break
            u = User(class_name=item[0], student_num=item[1], name=item[2], major=item[3],
                     birthday=datetime.strptime(item[4], '%Y-%m-%d'),
                     phone=item[5], gender=item[6], dormitory=item[7])
            db.session.add(u)
            sum += 1
        db.session.commit()
        print(mes['user_import_succeeded'].format(sum))
    except JSONDecodeError:
        print('json parser failed')
    except Exception as e:
        print(e)


@app.cli.command(short_help='database controller')
@click.argument('action')
def database(action):
    try:
        from nuaa_bot.app import db
        if action == 'reset':
            db.drop_all()
            db.create_all()
    except Exception as e:
        print(e)
