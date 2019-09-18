import hashlib
from base64 import b64encode
from base64 import b64decode
def verify_master(password):
    f = open('Master.txt', 'r')
    stored_hash = f.readline().strip()
    stored_salt = f.readline().strip()
    decoded_salt = b64decode(stored_salt)


    
    hash = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        decoded_salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        )
    encoded_test_hash = b64encode(hash).decode('utf-8')
    if encoded_test_hash == stored_hash:
        return True

def verify_master_return_hash(password):
    f = open('Master.txt', 'r')
    stored_hash = f.readline().strip()
    stored_salt = f.readline().strip()
    decoded_salt = b64decode(stored_salt)


    
    hash = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        password.encode('utf-8'), # Convert the password to bytes
        decoded_salt, # Provide the salt
        100000 # It is recommended to use at least 100,000 iterations of SHA-256 
        )
    encoded_test_hash = b64encode(hash).decode('utf-8')
    
    return encoded_test_hash