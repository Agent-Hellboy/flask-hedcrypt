from flaskcrypto.flask_crypto import Crypto
from flask import Flask
import os

import unittest
class TestCrypto(unittest.TestCase):

    @staticmethod
    def _get_instance():
        app=Flask(__name__)
        crypto=Crypto(app)
        return crypto

    def test_key_derive_and_verify(self):
        kdf = Crypto._setup()
        crypto = TestCrypto._get_instance()
        key = crypto.key_derive(b'data')
        self.assertTrue(crypto.key_verify(b'data',key)==None)

if __name__ == '__main__':
    unittest.main()
