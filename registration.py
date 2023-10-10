import hashlib
import shortuuid
from database_conn import DatabaseConnection
import validation
import menu
import maskpass
from encrypt import encrypt, decrypt

def register_user():
    patient_id = shortuuid.ShortUUID().random(length = 10)
    username = validation.validate_user()
    password = maskpass.advpass()
    password = encrypt(password)
    name = validation.validate_pname()
    m_no = validation.validate_mobile_no()
    gender = validation.validate_gender()
    
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO REGISTRATION (id, username, password, name, mobile_number, gender) VALUES (?, ?, ?, ?, ?, ?)', (patient_id, username, password, name, m_no, gender))
    return patient_id

# registering user
def reg():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS REGISTRATION(id text primary key, username text, password text, name text, mobile_number age, gender text)')
        register_user()
        
# Login user
def login():
    with DatabaseConnection('data.db') as connection:
        while True:
            u_name = input("Enter username: ")
            u_pw = maskpass.advpass()
            cursor = connection.cursor()
            pw = cursor.execute('SELECT password from REGISTRATION WHERE username = ?', (u_name,)).fetchone()
            password = decrypt(pw[0])
            u_pw = bytes(u_pw, 'utf-8')

            try: 
                if password == u_pw:
                    p_id = cursor.execute('SELECT id FROM REGISTRATION WHERE username = ?', (u_name, )).fetchone()
                    #print(p_id)
                    print("Successful login")
                    return p_id[0]
                else:
                    raise Exception
            except:
                print("Invalid username or password")
           
            