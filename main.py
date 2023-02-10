from flask import Flask, request, make_response, abort
import os
import psycopg2
from psycopg2 import pool
from replit import db

postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(
  1, 20, os.environ['DATABASE_URL'])


def get_db_connection():
  conn = psycopg2.connect(os.environ['DATABASE_URL'])
  return conn


app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Flask!'


@app.route('/stats')
def stats():
  return 'Hello from Stats!'


@app.route('/feedback', methods=['POST'])
def feedback():
  # Get the JSON payload
  payload = request.get_json()
  # Extract the data from the payload
  try:
    cell_id, value, user_hash = payload['cell_id'], payload['value'], payload[
      'user_hash']
    print("Values: ", cell_id, value, user_hash)
  except:
    print("bad json")
    return abort(400)
    # Use getconn() to Get Connection from connection pool
  ps_connection = postgreSQL_pool.getconn()
  # use cursor() to get a cursor as normal
  ps_cursor = ps_connection.cursor()
  #
  # use ps_cursor to interact with DB
  ps_cursor.execute(
    'INSERT INTO feedbacks (cell_id, value, user_hash)'
    'VALUES (%s, %s, %s)', (cell_id, value, user_hash))

  ps_connection.commit()
  #
  # close cursor
  ps_cursor.close()
  # release the connection back to connection pool
  postgreSQL_pool.putconn(ps_connection)

  response = make_response('Success', 200)
  return response


app.run(host='0.0.0.0', port=81)
