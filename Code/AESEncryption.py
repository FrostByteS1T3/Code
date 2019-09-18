import base64
import hashlib
from Crypto import Random
from pathlib import Path
from Crypto.Cipher import AES
import VerifyMaster

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-s[-1]]


class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode('utf-8')).digest()

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


def encrypt2(content):
    contents = content
    f = open('Master.txt', 'r')
    cipher = AESCipher(f.read())
    f.close()
    encrypted = cipher.encrypt(contents)
    decrypted = cipher.decrypt(encrypted)
    return encrypted
    print(encrypted.strip())
    print(decrypted.strip())
def decrypt2(name):
    my_dict = {}
    with open('Passwords.txt') as fileobj:
        for line in fileobj:
            key, *value = line.split(":")
            my_dict[key] = value
    f = open('Master.txt', 'r')
    cipher = AESCipher(f.read())
    f.close()
    decrypted = cipher.decrypt(''.join(my_dict[name]))
    print(decrypted.strip())
decrypt2('Test')
