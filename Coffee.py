from flask import Flask, jsonify, make_response, request
import pymysql.cursors

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

MY_ACCESS_TOKEN = "CAACEdEose0cBALpQbgPtZBYzqHIW3m1bEDai91oTwWJX10KvZBAwkNc6fphPlZAxB529ufwoh5i9ZCztxMOR9bKLx7uDEoVqqefYsfMhwsbDtNZAvx97nGF7Qo43oIY0Wk76AI0cVCnNrFcZBeVw49SbXZA5R5dflZBxI0qrSTNlniwJi2jS3QZCEOeV1JMDGZAZBz67ZC0EmXnmGkIVtetGucEh"

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)

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
        return json.dumps({'code': code, 'status': status})
    
    # Don't forget to return the response.
    return response

# Get all of the a person's friends using the app
@app.route("/api/v1/friends")
def pullFriendsList():

	graph = GraphAPI(MY_ACCESS_TOKEN)
	request = "me/friends"
	rawData = graph.get(request)
	
	return json.dumps(rawData)

# Get a friend by their Facebook ID and returns their name and picture url
@app.route("/api/v1/friends/<id>")
def pullFriendInfo(id):
	"""Pulls the profile picture and full name of a Facebook 
	user when a given id is passed through it"""
	graph = GraphAPI(MY_ACCESS_TOKEN)
	nameRequest = "/{}".format(id)
	name = graph.get(nameRequest)
	name = name['name']
	picRequest = "/{}/picture?redirect=false".format(id)
	picture = graph.get(picRequest)['data']['url']
	return json.dumps({'name': name, 'picture': picture})



# Connect to the database
def db_connect():
	return pymysql.connect(host='localhost',
						   port=5432,
						   user='owvnvhqozcnkak',
						   password='trPCRDSfIE2tPwdmZtm2LuuRr',
						   db='coffee',
						   charset='utf8mb4',
						   cursorclass=pymysql.cursors.DictCursor)


# Get ALL of the users
@app.route('/api/v1/users', methods=['GET'])
def get_users():
	# Connect to the database
	connection = db_connect()
	
	result = {'success':'False'}
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "SELECT * FROM `user`"
			cursor.execute(sql)
			result = { 'users' : cursor.fetchall() }
	finally:
		connection.close()

# Get a specific user
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	# Connect to the database
	connection = db_connect()

	result = {'success':'False'}
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "SELECT * FROM `user` WHERE id = %s"
			cursor.execute(sql, (user_id,))
			result = cursor.fetchone()
	finally:
		connection.close()
	return jsonify(result)

# Create a new user
@app.route('/api/v1/users', methods=['POST'])
def post_user():
	# Require both a name and a profileid
	if not request.json or not 'name' in request.json or not 'profileid' in request.json:
		return jsonify({'success':'false - Didn\'t supply enough parameters'})

	# Connect to the database
	connection = db_connect()
	
	result = {'success':'false'}
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "INSERT INTO `user` (`name`, `profileid`) values (%s, %s)"
			cursor.execute(sql, (request.json['name'], request.json['profileid'],))
			connection.commit()
			result = {'success':'true'}
	finally:
		connection.close()
	return jsonify(result)

# Update a specific user
@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
	# Require at least one non-id attribute
	if not request.json or (not 'name' in request.json and not 'profileid' in request.json):
		return jsonify({'success':'false - Didn\'t supply enough parameters'})

	# Connect to the database
	connection = db_connect()

	result = {'success':'false'}
	try:
		with connection.cursor() as cursor:
			if 'name' in request.json:
				sql = "UPDATE `user` SET `name`=%s where `id`=%s"
				cursor.execute(sql, (request.json['name'], user_id,))
			if 'profileid' in request.json:
				sql = "UPDATE `user` SET `profileid`=%s where `id`=%s"
				cursor.execute(sql, (request.json['profileid'], user_id,))
			connection.commit()
			result = {'success':'true'}
	finally:
		connection.close()
	return jsonify(result)

# Delete a specific user
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	# Connect to the database
	connection = db_connect()
	
	result = {'success':'false'}
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "DELETE FROM `user` WHERE id = %s"
			cursor.execute(sql, (user_id,))
			connection.commit()
			result = {'success':'true'}
	finally:
		connection.close()
	return jsonify(result)



# Get ALL of the events
@app.route('/api/v1/events', methods=['GET'])
def get_events():
	# Connect to the database
	connection = db_connect()
	
	result = {'success':'False'}
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "SELECT * FROM `event`"
			cursor.execute(sql)
			result = { 'events' : cursor.fetchall()}
	finally:
		connection.close()
	return jsonify(result)

# Get a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['GET'])
def get_event(event_id):
	# Connect to the database
	connection = db_connect()
	
	result = {'success':'False'}
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "SELECT * FROM `user` WHERE id = %s"
			cursor.execute(sql, (event_id,))
			result = cursor.fetchone()
	finally:
		connection.close()
	return jsonify(result)

# Create a new event
# Format for time is YYYY-MM-DD HH:MM:SS
@app.route('/api/v1/events', methods=['POST'])
def post_event():
	# Make sure friendid is passed in
	if not request.json or not 'friendid' in request.json:
		return jsonify({'success':'false - Didn\'t supply enough parameters'})

	# Fill each empty attribute with null
	if 'location' not in request.json:
		request.json['location'] = None
	if 'time' not in request.json:
		request.json['time'] = None
	if 'type' not in request.json:
		request.json['type'] = None

	# Connect to the database
	connection = db_connect()
	
	result = {'success':'false'}
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "INSERT INTO `event` (`friendid`, `location`, `time`, `type`) values (%s, %s, %s, %s)"
			cursor.execute(sql, (request.json['friendid'], request.json['location'], request.json['time'], request.json['type'],))
			connection.commit()
			result = {'success':'true'}
	finally:
		connection.close()
	return jsonify(result)

# Update a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['PUT'])
def put_event(event_id):
	# PUT body must contain at least one non-id attritbute
	if not request.json or (
				not 'friendid' in request.json and
				not 'type' in request.json and
				not 'time' in request.json and
				not 'location' in request.json):
		return jsonify({'success':'false - Didn\'t supply enough parameters'})

	# Connect to the database
	connection = db_connect()
	
	result = {'success':'false'}
	try:
		with connection.cursor() as cursor:
			if 'friendid' in request.json:
				sql = "UPDATE `event` SET `friendid`=%s where `id`=%s"
				cursor.execute(sql, (request.json['friendid'],event_id,))
			if 'location' in request.json:
				sql = "UPDATE `event` SET `location`=%s where `id`=%s"
				cursor.execute(sql, (request.json['location'],event_id,))
			if 'type' in request.json:
				sql = "UPDATE `event` SET `type`=%s where `id`=%s"
				cursor.execute(sql, (request.json['type'],event_id,))
			if 'time' in request.json:
				sql = "UPDATE `event` SET `time`=%s where `id`=%s"
				cursor.execute(sql, (request.json['time'],event_id,))
			connection.commit()
			result = {'success':'true'}
	finally:
		connection.close()
	return jsonify(result)

# Delete a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	# Connect to the database
	connection = db_connect()

	result = {'success':'false'}
	try:
		with connection.cursor() as cursor:
			# Read a single record
			sql = "DELETE FROM `event` WHERE id = %s"
			cursor.execute(sql, (event_id,))
			connection.commit()
			result = {'success':'true'}
	finally:
		connection.close()
	return jsonify(result)



if __name__ == '__main__':
	app.run(debug=True)
