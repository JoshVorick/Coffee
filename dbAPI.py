from flask import Flask, jsonify
import pymysql.cursors

app = Flask(__name__)

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
	        result = cursor.fetchall()
	finally:
	    connection.close()
	return jsonify({ "users" : result })

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
@app.route('/api/v1/users/<int:user_id>', methods=['POST'])
def post_user(user_id):
	return jsonify({'success':'false'})

# Update a specific user
@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def put_user(user_id):
	return jsonify({'success':'false'})

# Delete a specific user
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
	return jsonify({'success':'false'})



# Get ALL of the events
@app.route('/api/v1/events', methods=['GET'])
def get_events():
	return jsonify({"events":["bob","joe","james"]})

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
	        cursor.execute(sql, (user_id,))
	        result = cursor.fetchone()
	finally:
	    connection.close()
	return jsonify(result)

# Create a new event
@app.route('/api/v1/events/<int:event_id>', methods=['POST'])
def post_event(event_id):
	return jsonify({'success':'false'})

# Update a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['PUT'])
def put_event(event_id):
	return jsonify({'success':'false'})

# Delete a specific event
@app.route('/api/v1/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
	return jsonify({'success':'false'})



if __name__ == '__main__':
	app.run(debug=True)