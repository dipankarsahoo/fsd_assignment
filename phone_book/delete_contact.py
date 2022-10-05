import read_one_contact
import db_connect
from termcolor import colored


def delete_contact(user_name):
    print("Please search contact to be deleted")
    
    contact_list = read_one_contact.validate_and_search(user_name)
    
    if contact_list != False:
        fname, lname, email, phno = contact_list[0]
    else:
        return

    print(colored("Please type yes to confim deletion of above contact. Type no to go back to menu.", 'yellow'))
    print()
    user_consent = input()
    
    delete_sql = f"delete from contacts where user_name = '{user_name}' and first_name = '{fname}' and last_name = '{lname}' and email = '{email}' and phone_no = {phno} ;"
    
    if user_consent == "yes":
        try:
            conn = db_connect.connection()
            cur = conn.cursor()
            
            cur.execute(delete_sql)
            conn.commit()
            
            print(colored('Contact deleted successfully', 'green'))
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
    elif user_consent == "no":
        pass
    else:
        print(colored("Please enter valid input. Contact not deleted without user consent.", 'green'))
        
# delete_contact('dipankar')