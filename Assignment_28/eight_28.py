# Create Courses table (cid, cname) where cid is a primary key and Student table
# (rollno, name, cid) where rollno is a primary key and cid is a foreign key.

import psycopg2

def create_course_student_table():
    create_course_table_query = "create table course(cid int, cname text, PRIMARY KEY(cid));"
    
    create_student_table_query = "create table student(rollno int, name text, cid int, PRIMARY KEY(rollno), CONSTRAINT fk_course FOREIGN KEY(cid) references course(cid));"
    
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        cur = conn.cursor()
        
        # create course table
        cur.execute(create_course_table_query)
        conn.commit()
        print('Course table created successfully')
        
        # create student table
        cur.execute(create_student_table_query)
        conn.commit()
        print('Student table created successfully')
        
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        
create_course_student_table()