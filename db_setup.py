import os
import psycopg2

conn = psycopg2.connect(os.environ['DATABASE_URL'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS feedbacks;')
cur.execute('CREATE TABLE feedbacks (id serial PRIMARY KEY,'
            'cellId varchar (150) NOT NULL,'
            'value integer NOT NULL,'
            'date_added date DEFAULT CURRENT_TIMESTAMP);')

# Insert data into the table

cur.execute('INSERT INTO feedbacks (cellId, value)'
            'VALUES (%s, %s)', ('e2c0dad5-8175-4074-b522-f854af8bca88', 4))

conn.commit()

cur.close()
conn.close()