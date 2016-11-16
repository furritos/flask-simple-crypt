# coding:utf-8
import binascii
import os
import unittest

import flask

from flask_simple_crypt import SimpleCrypt


class BasicTestCase(unittest.TestCase):
    def setUp(self):
        app = flask.Flask(__name__)
        app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))
        self.fsc = SimpleCrypt(app)

    def test_payload_is_string(self):
        pw_enc = self.fsc.encrypt('secret')
        self.assertTrue(isinstance(pw_enc, str))

    def test_payload_is_not_string(self):
        with self.assertRaises(TypeError):
            self.fsc.encrypt(1234)

    def test_encrypt_and_decrypt_match(self):
        pw_enc = self.fsc.encrypt('secret')
        pw_dec = self.fsc.decrypt(pw_enc)
        self.assertEqual(pw_dec, 'secret')

    def test_encrypt_and_decrypt_mismatch(self):
        pw_enc = self.fsc.encrypt('secret')
        pw_dec = self.fsc.decrypt(pw_enc)
        self.assertNotEqual(pw_dec, 'bad_secret')

    def test_empty_secret_key(self):
        bad_app = flask.Flask(__name__)
        bad_app.config['SECRET_KEY'] = None
        with self.assertRaises(RuntimeError):
            SimpleCrypt(bad_app)


if __name__ == '__main__':
    unittest.main()
