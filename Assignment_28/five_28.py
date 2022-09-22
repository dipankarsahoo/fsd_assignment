# Delete any student from table with their rollno.

import psycopg2

def delete_student(rollno):
    
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor() 
        delete_student_query = f"delete from student where rollno = {rollno} ;"
        
        cur.execute(delete_student_query)
        conn.commit()           # Ensure to commit your changes in python
        print('row(s) deleted ...\n')
        
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
        
delete_student(4)