from nuaa_bot.app import db


class User(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    class_name = db.Column(db.String(10), nullable=False)
    student_num = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    major = db.Column(db.String(20), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    dormitory = db.Column(db.String(20), nullable=False)
    remark = db.Column(db.Text)
    open_id = db.Column(db.String(30))

    def __repr__(self):
        return '<User {}:{}>'.format(self.name, self.open_id)

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()
    #     return self
    #
    # def update(self):
    #     db.session.commit()
    #     return self
