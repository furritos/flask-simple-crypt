# from flask_simple_crypt import encrypt, decrypt

# output = encrypt("mypwd", "this is mydata")
# print output
# outout = decrypt("mypwd", output)
# print outout

from flask import Flask
from flask_simple_crypt import SimpleCrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is my key!"

cipher = SimpleCrypt()
cipher.init_app(app)

enc_data = cipher.encrypt("shhhhhhh!")
print enc_data

dec_data = cipher.decrypt(enc_data)
print dec_data