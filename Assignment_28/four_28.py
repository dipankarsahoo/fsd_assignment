# Update the student name of rollno 3 with ‘Mohan’

import psycopg2

def update_student_name(rollno, name):
    
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor() 
        update_student_query = f"update student set name = '{name}' where rollno = {rollno} ;"
        
        cur.execute(update_student_query)
        conn.commit()           # Ensure to commit your changes in python
        print('row(s) updated ...\n')
        
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
        
update_student_name(3, 'Mohan')