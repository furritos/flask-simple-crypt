[![furritos](https://circleci.com/gh/furritos/flask-simple-crypt.svg?style=svg)](https://circleci.com/gh/furritos/flask-simple-crypt)

# Flask-Simple-Crypt

Flask extension based on `simple-crypt` that allows simple, secure encryption and decryption for Python.  The original module is available in [pypi](http://pypi.python.org/pypi/simple-crypt) and [github](https://github.com/andrewcooke/simple-crypt).

## Overview

This Flask extension provides two functions, which encrypt and decrypt data, delegating all the hard work to the [pycrypto](https://www.dlitz.net/software/pycrypto) 

## Dependencies

 - Python 3.7 or greater
 - Flask 2.1.0 or greater
 - PyCryptoDome 3.15.0 or greater

## Install from PyPi

```
pip install flask-simple-crypt
```

## Install from source

```
git clone https://github.com/furritos/flask-simple-crypt
python setup.py install
```

## Usage 

### Simple Flask Application

For this extension to work properly, a `SECRET_KEY` must be defined.  It is **strongly** suggested that one use strong key, **especially** when working with sensitive data.

```
from flask import Flask
from flask_simple_crypt import SimpleCrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is my key!"

cipher = SimpleCrypt()
cipher.init_app(app)

enc_data = cipher.encrypt("shhhhhhh!")
print(enc_data)  # returns base64 encoded and encrypted data

dec_data = cipher.decrypt(enc_data)
print(dec_data)  # returns original data
```

## Performance

Both encryption and decryption are can be relatively slow.  However, this is a tunable parameter. In the original version of **simple-crypt**, there is a fixed value of 10,000 iterations.

With `flask-simple-crypt`, this value is now tunable from the default of 25,000.  Obviously, this needs to be adjust for acceptable performance.  To override this, simply add `FSC_EXPANSION_COUNT` into the Flask configuration manifest:

```
from flask import Flask
from flask_simple_crypt import SimpleCrypt

import time

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is my key!"
app.config['FSC_EXPANSION_COUNT'] = 2048

cipher = SimpleCrypt()
cipher.init_app(app)

start = time.time()
enc_data = cipher.encrypt("shhhhhhh!")
dec_data = cipher.decrypt(enc_data)
end = time.time()
print(end - start)
```

On an i5, 2.5 Ghz machine, this finished in about .2 seconds.
With `app.config['FSC_EXPANSION_COUNT'] = 20000`, it finished in about 2.1 seconds.
Finally, with `app.config['FSC_EXPANSION_COUNT'] = 200000`, it finished in about 21 seconds.

Generally, the thinking is that this lapse in processing would deter any would be attackers from programmatically brute forcing their way into the passwords.  Again, tune to your liking, balancing performance with security, but be cognizant that this library is designed to make the key (the password) hard to guess (it uses a [PBKDF](https://en.wikipedia.org/wiki/Key_derivation_function), which can take a couple of seconds to run).

To quote the [original](https://github.com/andrewcooke/simple-crypt#speed):

> In simple terms, if an attacker tries to decrypt the data by guessing passwords, then they *also* have to wait for a couple of seconds for each guess.  This stops an attacker from trying "thousands" of different passwords every second.

> So the pause on encryption and decryption is actually a sign that the library is protecting you.  If this is unacceptable for your program then you may need to look for a different solution.  I'm sorry, but this is the trade-off I chose when writing simple-crypt.

## Algorithms

Notable exceptions from the original implementation are as follows:

* The password is expanded to two 256 bit keys using PBKDF2 with a 256 bit random salt, SHA256, and 25,000 iterations.

* An encrypted messages starts with a 5 byte header (**fsc** in ASCII followed by two bytes containing version data).

* On top of the above mentioned encryption, the result is then base64 encoded for ease of use with databases.

* Built against Release 4.1 of `simple-crypt`.

## Warnings

Heed the [same](https://github.com/andrewcooke/simple-crypt#warnings) as the original.

## Credits

Much of the work has been made possible thanks to [Andrew Cooke's](https://github.com/andrewcooke) original work.  The purpose (and focus) of this project was to `flaskify` it.
