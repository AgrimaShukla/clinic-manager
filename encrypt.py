from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# with open('filekey.key', 'wb') as filekey:
#     filekey.write(key)
def get_key():
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    return key

def encrypt(password):
    password = bytes(password, 'utf-8')
    fernet = Fernet(get_key())
    cipher_pw = fernet.encrypt(password)
    #print(cipher_pw)
    return cipher_pw

def decrypt(en_pw):
    fernet = Fernet(get_key())
    plain_pw = fernet.decrypt(en_pw)
    return plain_pw

