# Delete all the data from student table.

import psycopg2

def delete_all_student():
    
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor() 
        delete_student_query = "delete from student ;"
        
        cur.execute(delete_student_query)
        conn.commit()           # Ensure to commit your changes in python
        print('all data of student table deleted ...\n')
        
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
        
delete_all_student()