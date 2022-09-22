# Write a Select query to fetch all the students.

import psycopg2

def get_all_students():
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor() 
        get_all_students_query = "select * from student;"
        cur.execute(get_all_students_query)
        print(cur.fetchall())
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
    
get_all_students()