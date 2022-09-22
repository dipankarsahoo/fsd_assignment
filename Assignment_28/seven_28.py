# Drop the student table.

import psycopg2

def drop_student_table():
    
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor()
        
        drop_student_query = "drop table student;"
        
        cur.execute(drop_student_query)
        conn.commit()
        
        print('Student table dropped successfully  ')
        
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        
drop_student_table()