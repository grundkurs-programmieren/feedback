from flask import Flask, request, make_response, abort

db = {}

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
        cellId, value = payload['cellId'], payload['value']
        print("Values: ", cellId, value)
    except:
        print("bad json")
        return abort(400)

    # Connection based
    # conn = sql.connect()
    # courser = conn.courser()
    # courser.insert()

    # Pool based
    # conn = sql.pool.get_connection()
    # courser = conn.courser()
    # courser.insert()

    # insert data into key value store
    try:
        values = db[cellId]
        values.append(value)
    except:
        db[cellId] = [value]

    for key in db.keys():
        print(db[key])

    response = make_response('Success', 200)
    return response


app.run(host='0.0.0.0', port=81)
