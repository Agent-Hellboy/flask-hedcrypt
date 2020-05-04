from .flask_crypto import Crypto

from flask import Flask 
app=Flask(__name__)
crypto = Crypto(app)
print(crypto)
