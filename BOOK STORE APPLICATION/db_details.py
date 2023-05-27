import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='your_user_name',
        password='your_password')


cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books;')

cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

conn.commit()

cur.close()
conn.close()
