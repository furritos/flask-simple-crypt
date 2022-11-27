"""
    Flask-Simple-Crypt
    ------------------

    Simple Crypt helper for encrypting/decrypting data in Flask.
"""

import os

from setuptools import setup

module_path = os.path.join(os.path.dirname(__file__), 'flask_simple_crypt.py')
with open(module_path) as module:
    for line in module:
        if line.startswith('__version__'):
            version_line = line
            break

__version__ = eval(version_line.split('__version__ = ')[-1])

setup(
    name='Flask-Simple-Crypt',
    version=__version__,
    url='https://github.com/furritos/flask-simple-crypt',
    license='MIT',
    author='Carlos Rivas',
    author_email='carlos@riv.as',
    description='Simple Crypt helper for encrypting/decrypting data in Flask.',
    py_modules=['flask_simple_crypt'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'pycryptodome'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_flask_simple_crypt'
)
