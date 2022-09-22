# Insert records for 4 students

import psycopg2

def insert_students():
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor() 
        insert_student_query = "insert into student values(1, 'Ron', 'Java'),(2, 'Dan', 'Javascript'), (3, 'Jan', 'Python'), (4, 'Jim', 'HTML');"
        
        cur.execute(insert_student_query)
        conn.commit()           # Ensure to commit your changes in python
        print('rows created ...\n')
        
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
    
insert_students()