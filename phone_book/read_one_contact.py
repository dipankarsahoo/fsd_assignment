import db_connect
import termtables
from termcolor import colored


def get_contact_details_to_search():
    
    print(colored("Please enter first name / email / phone number to search contact details", 'green') )
    print()
    fname = input("First Name: ")
    print()
    email = input("Email: ")
    print()
    phno = input("Phone Number: ")

    return (fname, email, phno)

def validate_and_search(user_name):
    while True:
        fname, email, phno = get_contact_details_to_search()
        
        if fname == "" and email == "" and phno == "":
            print(colored("Please enter any one information to search" , 'red'))
            continue
        elif phno.isnumeric() != True and phno != "":
            print(colored("Phone number must be a number", 'red'))
            continue
        else:
            break
        
    return search_contact(user_name, fname, email, phno)

def search_contact(user_name, fname = None, email = None, phno = None):
    
    search = f"select first_name, last_name, email, phone_no from contacts where user_name = '{user_name}'  "
    with_fname = f"and first_name = '{fname}'"
    with_email = f"and email = '{email}'"
    with_phno = f"and phone_no = {phno}"
    
    if fname != "" and fname != None:
        search += with_fname
        
    if email != "" and email != None:
        search += with_email
        
    if phno != "" and phno != None:
        search += with_phno
        
    search += " ;"
    
    try:
        conn = db_connect.connection()
        cur = conn.cursor()
        
        header = ["First Name", "Last Name", "Email", "Phone Number"]
        data = []
        
        cur.execute(search)
        
        for row in cur.fetchall():
            data.append(list(row))
            
        if len(data) > 0:
            print("Your Contacts list")
            termtables.print(data, header=header, style = termtables.styles.double_thin)
            return data
        else:
            print(colored("Contact not found", 'yellow') )
            return False
        
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    
# validate_and_search('dipankar')  # Test case