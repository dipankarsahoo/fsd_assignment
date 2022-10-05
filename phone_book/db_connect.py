import psycopg2


def connection():
    try:
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                password='password',
                                host = 'localhost',
                                port='5434')
        
        return conn
    
    except Exception as e:
        print(e)