import db_connect
from termcolor import colored


def delete_all_contacts(user_name):
    user_consent = input("Are you sure you want to delete all contacts ? [y/n]")
    
    if user_consent == "y":
        try:
            conn = db_connect.connection()
            cur = conn.cursor()
            
            delete_all_contact_sql = f"delete from contacts where user_name = '{user_name}' ;"
            
            cur.execute(delete_all_contact_sql)
            conn.commit()
            
            print(colored('All contacts deleted successfully', 'green') )
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()
            
    else:
        pass
    

# delete_all_contacts('dipankar')
    