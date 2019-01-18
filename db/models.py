import sqlalchemy.dialects.postgresql

from app import db


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    result_all = db.Column(sqlalchemy.dialects.postgresql.JSON)
    result_no_stop_words = db.Column(sqlalchemy.dialects.postgresql.JSON)

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return "<id : {}>".format(self.id)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

def test():
    return  __name__

if __name__ == "__main__":
    from test import  foo
    print(test())
    print(foo())
