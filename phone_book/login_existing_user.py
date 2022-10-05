import db_connect
import register
import datetime
import display
from termcolor import colored


    
def get_user_input():        
    return display.get_input_user_password()


def verify_user( user_name, password):

    if register.verify_if_user_exists(user_name):
        if verify_password(user_name,password):
            print(colored(f"[User {user_name} logged in]" , 'green'))
            print(datetime.datetime.now())
            return True
        else:
            print("Incorrect user_name or password")
            return False
    else:
        print("[User does not exist. Please register to continue...]")
        return False
        
def verify_password( user_name, password):
    try:
        conn = db_connect.connection()
        cur = conn.cursor()
        check_user_pass = f"select count(*) from users where user_name = '{user_name}' and password = '{password}';"
        
        cur.execute(check_user_pass)
        
        for row in cur:
            if row == (1,):
                return True
            else:
                return False
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()