# Select all the students who are doing a specific course, eg. Python.

import psycopg2

def filter_data(tablename, data):
    try:
        filter_query = f"select * from {tablename} where cid in (select cid from course where cname = '{data}' ) ;"
        
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor() 
        
        cur.execute(filter_query)
        print(cur.fetchall())
    except Exception as e:
        print(e)
    finally:
        # close cursor and connection with DB
        cur.close()
        conn.close()
        
filter_data('student', 'Python')