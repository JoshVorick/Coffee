from flask import Flask, jsonify, make_response, request
import os
import psycopg2
import urlparse

# Facebook and json imports
from facepy import GraphAPI
import json

# Needed for Facebook Authentication
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from config import CONFIG

# Needed for Flask
from flask import Flask, render_template, request, make_response
app = Flask(__name__)

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)

MY_ACCESS_TOKEN = "883030211746778|d3c627235a423cc7ebc7ccb564cea7a2"

# Connect to the database
urlparse.uses_netloc.append('postgres')
url = urlparse.urlparse(os.environ['DATABASE_URL'])
connection = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# Return JSON on 404 instead of HTML
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'API call not found'}), 404)

# Login
@app.route('/api/v1/login', methods=['GET', 'POST'])
def login():
    # We need response object for the WerkzeugAdapter.
    response = make_response()
    
    # Log the user in, pass it the adapter and the provider name.
    result = authomatic.login(WerkzeugAdapter(request, response), 'fb')
    
	# If there is no LoginResult object, the login procedure is still pending.
    if result:
        if result.user:
            # We need to update the user to get more info.
            result.user.update()

        # Executes when a user successfully logs in and is authenticated
        code = request.args.get('code')
        status = request.args.get('status')
        return json.dumps({'code': code, 'status': status, 'id': result.user.id, 'name':result.user.name})
            
    # Don't forget to return the response.
    return response

# Get all of the a person's friends using the app
@app.route("/api/v1/users/<string:user_id>/friends")
def pullFriendsList(user_id):
	graph = GraphAPI(MY_ACCESS_TOKEN)
	request = "{}/friends".format(user_id)
	rawData = graph.get(request)
	return json.dumps(rawData)

# Get ALL of the users
@app.route('/api/v1/users', methods=['GET'])
def get_users():
	with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT * FROM users"
		cursor.execute(sql)
		return jsonify({ 'users' : cursor.fetchall() })

# Get a specific user
@app.route('/api/v1/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
	with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT * FROM users WHERE profileid = %s"
		cursor.execute(sql, (user_id,))
                res = cursor.fetchone()
                if(res is None):
                    return jsonify({'error':'No such user'})

                # Get events
		sql = "SELECT * FROM events WHERE user1 = %s OR user2 = %s"
		cursor.execute(sql, (user_id,))
                events = cursor.fetchone()
                res["events"] = events

                # Get friends
                graph = GraphAPI(MY_ACCESS_TOKEN)
                request = "{}/friends".format(user_id)
                rawData = graph.get(request)
                friends =  json.dumps(rawData)["data"]
                friend_ids = [friend["id"] for friend in friends]

                res["friends"] = friend_ids
		return jsonify(res)

# Create a new user
@app.route('/api/v1/users', methods=['POST'])
def post_user():
	# Require both a name and a profileid
	if not request.json or not 'name' in request.json or not 'profileid' in request.json or not 'accessid' in request.json:
		return jsonify({'success':'false - Didn\'t supply enough parameters'})

	if not 'accountid' in request.json:
		request.json['accountid'] = None

	with connection.cursor() as cursor:
		# Read a single record
		sql = "INSERT INTO users (name, profileid, accessid, accountid) values (%s, %s, %s, %s)"
		cursor.execute(sql, (request.json['name'], request.json['profileid'], request.json['accessid'], request.json['accountid']))
		connection.commit()
		return jsonify({'success':'true'})

# Update a specific user
@app.route('/api/v1/users/<string:user_id>', methods=['PUT'])
def put_user(user_id):
	# Require at least one non-id attribute
	if not request.json or (not 'name' in request.json and not 'accountid' in request.json):
		return jsonify({'success':'false - Didn\'t supply enough parameters'})

	with connection.cursor() as cursor:
		if 'name' in request.json:
			sql = "UPDATE users SET name=%s where profileid=%s"
			cursor.execute(sql, (request.json['name'], user_id,))
		if 'accountid' in request.json:
			sql = "UPDATE users SET accountid=%s where profileid=%s"
			cursor.execute(sql, (request.json['accountid'], user_id))
        connection.commit()
        return jsonify({'success':'true'})

# Delete a specific user
@app.route('/api/v1/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
	with connection.cursor() as cursor:
		# Read a single record
		sql = "DELETE FROM users WHERE profileid = %s"
		cursor.execute(sql, (user_id,))
		connection.commit()
		return jsonify({'success':'true'})


# Get ALL of the events
@app.route('/api/v1/events', methods=['GET'])
def get_events():
	with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT * FROM events"
		cursor.execute(sql)
		return jsonify({ 'events' : cursor.fetchall()})

@app.route('/api/v1/users/<string:user_id>/events', methods=['GET'])
def get_users_event(user_id):
	with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT * FROM events WHERE user1 = %s OR user2 = %s"
		cursor.execute(sql, (user_id,))
                res = cursor.fetchone()
                if(res is None):
                    return jsonify({'error':'No such event'})
		return jsonify(res)

# Get a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
	with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT * FROM events WHERE id = %s"
		cursor.execute(sql, (event_id,))
                res = cursor.fetchone()
                if(res is None):
                    return jsonify({'error':'No such event'})
		return jsonify(res)

# Create a new event
# Format for time is YYYY-MM-DD HH:MM:SS
@app.route('/api/v1/events', methods=['POST'])
def post_event():
	# Make sure user1 and user2 are passed in
	if not request.json or not 'user1' or not 'user2' in request.json:
		return jsonify({'success':'false - Didn\'t supply enough parameters'})

	# Fill each empty attribute with null
	if 'location' not in request.json:
		request.json['location'] = None
	if 'time' not in request.json:
		request.json['time'] = None
	if 'type' not in request.json:
		request.json['type'] = None

	with connection.cursor() as cursor:
		# Read a single record
		sql = "INSERT INTO events (user1, user2, location, time, type, status) values (%s, %s, %s, %s, %s, %s)"
		cursor.execute(sql, (request.json['user1'], request.json['user2'], request.json['location'], request.json['time'],request.json['type'],request.json['status']))
		connection.commit()
		return jsonify({'success':'true'})

# Update a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['PUT'])
def put_event(event_id):
	# PUT body must contain at least one non-id attritbute
	if not request.json or (
				(
                                    not 'user2' in request.json or
				    not 'user1' in request.json
                                ) and
				not 'type' in request.json and
				not 'time' in request.json and
				not 'location' in request.json):
		return jsonify({'success':'false - Didn\'t supply enough parameters'})

	with connection.cursor() as cursor:
		if 'user1' in request.json and 'user2' in request.json:
			sql = "UPDATE events SET user1=%s user2=%s where id=%s"
			cursor.execute(sql, (request.json['friendid'],event_id,))
		if 'location' in request.json:
			sql = "UPDATE events SET location=%s where id=%s"
			cursor.execute(sql, (request.json['location'],event_id,))
		if 'type' in request.json:
			sql = "UPDATE events SET type=%s where id=%s"
			cursor.execute(sql, (request.json['type'],event_id,))
		if 'time' in request.json:
			sql = "UPDATE events SET time=%s where id=%s"
			cursor.execute(sql, (request.json['time'],event_id,))
		connection.commit()
		return jsonify({'success':'true'})

# Delete a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	with connection.cursor() as cursor:
		# Read a single record
		sql = "DELETE FROM events WHERE id = %s"
		cursor.execute(sql, (event_id,))
		connection.commit()
		return jsonify({'success':'true'})

if __name__ == '__main__':
	app.run(debug=True)
