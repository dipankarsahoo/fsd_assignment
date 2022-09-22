# Insert data in both the tables

import psycopg2

def insert_courses():
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor() 
        insert_course_query = "insert into course values(1, 'Java'),(2, 'Javascript'), (3, 'Python'), (4,  'HTML'), (5, 'CSS'), (6, 'Django'), (7, 'API');"
        
        cur.execute(insert_course_query)
        conn.commit()           # Ensure to commit your changes in python
        print('rows inserted ...\n')
        
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
        
        
def insert_students():
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor() 
        insert_student_query = "insert into student values(1, 'Ron', 1),(2, 'Dan', 2), (3, 'Jan', 3), (4, 'Jim', 5);"
        
        cur.execute(insert_student_query)
        conn.commit()           # Ensure to commit your changes in python
        print('rows inserted ...\n')
        
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
   
insert_courses() 
insert_students()
