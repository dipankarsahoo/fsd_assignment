import db_connect
from termcolor import colored


def get_contact_details_to_add():
    fname = input("First Name: ")
    print()
    lname = input("Last Name: ")
    print()
    email = input("Email: ")
    print()
    phno = input("Phone Number: ")
    
    return (fname, lname, email, phno)

def insert_contact_info(user_name):
    
    # validate inputs and call get_contact_details_to_add() incase of validation failure
    while True:
        fname , lname , email , phno = get_contact_details_to_add()
    
        if fname == '' or phno == '':
            print("First Name and Phone Number cannot be empty.")
            continue
        elif len(phno) != 10 and phno.isnumeric() != True:
            print("Phone Number must be 10 digits")
            continue
        else:
            break
       
    try:
        conn = db_connect.connection()
        cur = conn.cursor()
        insert_contact = f"insert into contacts values('{fname}', '{lname}', '{email}', {phno}, '{user_name}' );"
        
        cur.execute(insert_contact)
        conn.commit()
        
        print(colored('Contact added successfully', 'green'))
        
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()