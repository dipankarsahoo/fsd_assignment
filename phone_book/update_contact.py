import read_one_contact
import add_new_contact
import db_connect
from termcolor import colored


def update_contact(user_name):
    print(colored("Please search contact to be updated", 'green') )

    contact_list = read_one_contact.validate_and_search(user_name)

    if contact_list != False:
        fname, lname, email, phno = contact_list[0]
    else:
        return

    print(colored("Please enter the details to be updated for this contact", 'green') )
    new_fname, new_lname, new_email, new_phno = add_new_contact.get_contact_details_to_add()

    update_contact = f"update contacts set "
    with_fname = f"first_name = '{new_fname}' ,"
    with_lname = f"last_name = '{new_lname}' ,"
    with_email = f"email = '{new_email}' ,"
    with_phno = f"phone_no = {new_phno} "
    where_clause = f"where user_name = '{user_name}' and first_name = '{fname}' and last_name = '{lname}' and email = '{email}' and phone_no = {phno} ; "
    
    if new_fname == "" and new_lname == "" and new_email == "" and new_phno == "" :
        update_contact_sql = update_contact + f"first_name = '{fname}' " + where_clause
    else:
        if new_fname != "" and new_fname != None:
            update_contact += with_fname
        
        if new_lname != "" and new_lname != None:
            update_contact += with_lname
            
        if new_email != "" and new_email != None:
            update_contact += with_email
            
        if new_phno != "" and new_phno != None:
            update_contact += with_phno
            
        if update_contact[-1] == ",":
            update_contact_sql = update_contact[:-1]
            update_contact_sql += where_clause
        else:
            update_contact_sql = update_contact
            update_contact_sql += where_clause

        
    try:
        conn = db_connect.connection()
        cur = conn.cursor()
        
        cur.execute(update_contact_sql)
        conn.commit()

    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
    
    if new_fname == "" and new_lname == "" and new_email == "" and new_phno == "" :
        read_one_contact.search_contact(user_name, fname, email, phno)
    else:
        print(colored('Contact updated successfully', 'green') )
        print("Updated", end= " ")
        read_one_contact.search_contact(user_name, new_fname, new_email, new_phno)
        
    
# update_contact('dipankar')   # Test case