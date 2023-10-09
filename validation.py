import re

def error_handling(func):
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if val == False:
                raise Exception    
        except:
            print("Invalid Input")

        finally:
            return val
    return wrapper

@error_handling
def validation(reg_exp, data):
    #print(type(reg_exp))
    res = reg_exp.search(data)
    if res:
        return True
    else:
        return False
    
# validating patient name
def validate_pname():
    while True:
        name = input("Enter patient name: ")
        regex_name = re.compile(r"^([A-Za-z\s']{2,25}$)")
        val = validation(regex_name, name)
        if val == True:
            return name.lower()

# validating doctor name
def validate_dname():
    while True:
        name = input("Enter doctor name: ")
        regex_name = re.compile(r"^([A-Za-z\s']{2,25}$)")
        val = validation(regex_name, name)
        if val == True:
            return name.lower()


# validating age
def validate_age():
    while True:
        age = input("Enter age: ")
        regex_name = re.compile(r'^([1:9]|[1-9][0-9]|1[0-4][0-9]|150)$')
        val = validation(regex_name, age)
        if val == True:
            return age.lower()

# validate age
def validate_gender():
    while True:
        gender = input("Enter gender (male/female/other): ")
        regex_name = re.compile(r'^(male|female|other)$', re.IGNORECASE)
        val = validation(regex_name, gender)
        if val == True:
            return gender.lower()