# Create a table (student) with 3 columns (rollno, name, course).

import psycopg2

def create_student_table():
    
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        # print(conn.get_dsn_parameters(), "\n")
        cur = conn.cursor() 
        
        create_student_query = 'create table student(rollno int, name text, course text, PRIMARY KEY(rollno));'
        
        cur.execute(create_student_query)
        conn.commit()           # Ensure to commit your changes in python
        print('Student table created ...\n')
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
    
create_student_table()