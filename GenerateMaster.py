import os
from base64 import b64encode
import hashlib


def generate_master():
    salt = os.urandom(32)

    password = str

    hash = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
    )

    encoded_salt = b64encode(salt).decode('utf-8')

    encoded_hash = b64encode(hash).decode('utf-8')

    f = open('Master.txt', 'w')
    f.write(encoded_hash + '\n')
    f.write(encoded_salt + '\n')
    f.close()
