'''
This module handles encryption and decryption od password stored in database
'''
import os

from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# with open('filekey.key', 'wb') as filekey:
#     filekey.write(key)

key_path = key_path = os.path.abspath(os.curdir) + "utils/filekey.key"
def get_key()->bytes:
    with open(key_path, 'rb') as filekey:
        key = filekey.read()
    return key

def encrypt(password)->bytes:
    password = bytes(password, 'utf-8')
    fernet = Fernet(get_key())
    cipher_pw = fernet.encrypt(password)
    #print(cipher_pw)
    return cipher_pw

def decrypt(en_pw)->bytes:
    fernet = Fernet(get_key())
    plain_pw = fernet.decrypt(en_pw)
    return plain_pw
