
import db_connect
import display

    
def verify_if_user_exists(user_name):
    try:
        conn = db_connect.connection()
        cur = conn.cursor()
        check_existing_user = f"select count(*) from users where user_name = '{user_name}';"
        
        cur.execute(check_existing_user)
        
        for row in cur:
            if row == (0,):
                return False
            else:
                return True
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    
def get_user_input():
    return display.get_input_user_password()
    
def add_new_user( user_name, password):
    try:
        conn = db_connect.connection()
        cur = conn.cursor()
        
        insert_user = f"insert into users values ('{user_name}', '{password}');"
        cur.execute(insert_user)
        conn.commit()
        print(f"[User {user_name} added successfully]")
        
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()