from flask import Flask
from flask_crypto import Crypto
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

from sqlalchemy.ext.declarative import declared_attr


class PasswordMixin:
    pass


def encryptor(cls):
    """
    function to decorates the User5 class.
    Params:
    It takes username and ssid and generate a key for the user which acts a password to the user.
    And is used as a key for more functionality of the library.
    """
    return cls


class Encryptor:
    def __call__(self, cls):
        class Inner(cls):
            crypt = Crypto(app)
            var = crypt.key_derive(cls.ssid)
            # print(print(cls.ssid))
            setattr(cls, "password", var)

        return Inner


@Encryptor()
class User5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    # email = db.Column(db.String(120), unique=True, nullable=False)
    # password = db.Column(db.String(60))
    ssid = db.Column(db.String(20))

    def __repr__(self):
        return f"User('{self.username}',{self.ssid})"


db.create_all()

user = User5(username="prince", ssid="3456ait")
db.session.add(user)
db.session.commit()

user = User5.query.all()

print(user)
