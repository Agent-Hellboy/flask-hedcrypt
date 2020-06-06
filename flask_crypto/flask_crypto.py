"""
flask_cypto.py 
Contains Crypto class which derive and verify key in accordance with PKCS7. 
"""


import os
import base64

from flask import current_app

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


SALT = os.urandom(16)


class Crypto:
    """
    Class that provide APIs which acts as an interface to the cryptography library of python. 
    You can tune the parameters in _setup function.
    We need to pass a hashing function that will be used as the HMAC, 
    number of iterations to mitigate brute-force attack, and a salt for rainbow tables.
    """

    @staticmethod
    def _setup():
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=SALT,
            iterations=100000,
            backend=default_backend(),
        )
        return kdf

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.app_context()

    def key_derive(self, name):
        # Returns key of length 32 as I have used length of 32, however you can tune it.
        kdf = Crypto._setup()
        key = kdf.derive(name)
        key = base64.b64encode(key)
        return key

    def key_verify(self, password, l_key):
        # Return None if password is verified else generate an EXCEPTION InvalidKey.
        kdf = Crypto._setup()
        return kdf.verify(password, base64.b64decode(l_key))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
