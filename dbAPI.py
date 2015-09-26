from flask import Flask, jsonify, make_response, request
import pymysql.cursors

app = Flask(__name__)

# Return JSON on 404 instead of HTML
@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'API call not found'}), 404)

# Get ALL of the users
@app.route('/api/v1/users', methods=['GET'])
def get_users():
	# Connect to the database
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
	result = {'success':'False'}
	try:
	    with connection.cursor() as cursor:
	        # Read a single record
	        sql = "SELECT * FROM `user`"
	        cursor.execute(sql)
	        result = { 'users' : cursor.fetchall() }
	finally:
	    connection.close()
	return jsonify(result)

# Get a specific user
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
	# Connect to the database
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
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
		abort(400)

	# Connect to the database
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
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
		abort(400)

	# Fill in each empty attribute with null
	if not 'name' in request.json:
		request.json['name'] = None
	if not 'profileid' in request.json:
		request.json['profileid'] = None

	# Connect to the database
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
	result = {'success':'false'}
	try:
	    with connection.cursor() as cursor:
	        sql = "UPDATE `user` SET `name`=%s, `profileid`=%s where `id`=%s"
	        cursor.execute(sql, (request.json['name'], request.json['profileid'],request.json['id']))
	        connection.commit()
	        result = {'success':'true'}
	finally:
	    connection.close()
	return jsonify(result)

# Delete a specific user
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	# Connect to the database
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
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
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
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
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
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
		abort(400)

	# Fill each empty attribute with null
	if 'location' not in request.json:
		request.json['location'] = None
	if 'time' not in request.json:
		request.json['time'] = None
	if 'type' not in request.json:
		request.json['type'] = None

	# Connect to the database
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
	result = {'success':'false'}
	try:
	    with connection.cursor() as cursor:
	        # Read a single record
	        # TODO: Allow you to only create required fields
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
		abort(400)

	# Fill each empty attribute with null
	if not 'friendid' in request.json:
		request.json['friendid'] = None
	if not 'location' in request.json:
		request.json['location'] = None
	if not 'time' in request.json:
		request.json['time'] = None
	if not 'type' in request.json:
		request.json['type'] = None

	# Connect to the database
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
	result = {'success':'false'}
	try:
	    with connection.cursor() as cursor:
	        # TODO: Allow updating of only one attribute
	        sql = "UPDATE `event` SET `friendid`=%s, `type`=%s, `time`=%s, `location`=%s where `id`=%s"
	        cursor.execute(sql, (request.json['friendid'],request.json['type'],request.json['time'],request.json['location'],event_id,))
	        connection.commit()
	        result = {'success':'true'}
	finally:
	    connection.close()
	return jsonify(result)

# Delete a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	# Connect to the database
	connection = pymysql.connect(host='localhost',
                	             port=3306,
                                 user='josh',
            	                 password='asdf',
                	             db='coffee',
                    	         charset='utf8mb4',
                        	     cursorclass=pymysql.cursors.DictCursor)
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