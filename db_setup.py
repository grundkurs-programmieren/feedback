import os
import psycopg2

conn = psycopg2.connect(os.environ['DATABASE_URL'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS feedbacks;')
cur.execute('CREATE TABLE feedbacks (id serial PRIMARY KEY,'
            'cell_id varchar (150) NOT NULL,'
            'value integer NOT NULL,'
            'user_hash varchar (64),'
            'date_added date DEFAULT CURRENT_TIMESTAMP);')

conn.commit()

cur.close()
conn.close()
