import os
import base64

from flask import current_app, _app_ctx_stack

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend


# key derivation
salt = os.urandom(16)

class Crypto:
    
    @staticmethod
    def _setup():
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
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
        kdf = Crypto._setup()
        key = kdf.derive(name)
        return key

    def key_verify(self, password, l_key):        
        kdf = Crypto._setup()
        return kdf.verify(password, l_key)
