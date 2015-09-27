from facepy import GraphAPI
import json

# Needed for Facebook Authentication
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from config import CONFIG

# Needed for Flask
from flask import Flask, render_template, request, make_response
app = Flask(__name__)

MY_ACCESS_TOKEN = "CAACEdEose0cBAII2V0BZC8IX4knFZCmnZBlIzqdWap3TXUt1O4l0zwJo7Dfy9ZCd7vOzOE4yekt9nX45h11rmNP7ZA8S8croGcZCkaPoa3Mxs5tt97ZAHdgV7meRu5oANcv9o243ZAGA8AYIi7INhcHOyLPGzginZB1UBhWaXHZB9TPHOxSdPiFk65sV0C1Ld9jTpiKAwpUn8DsLQZCB3iZAHaL3"

# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=False)

@app.route('/')
def index():
	return "Please visit the login page: localhost:8080/api/v1/login"
	# Can use once we have the index template done
	# return render_template('index.html')

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
        
        # The rest happens inside the template.
        # TODO: return render_template('login.html', result=result)
        # return "You have logged in"
        code = request.args.get('code')
        status = request.args.get('status')
        return json.dumps({'code': code, 'status': status})
    
    # Don't forget to return the response.
    return response

@app.route("/api/v1/friends")

def pullFriendsList():

	graph = GraphAPI(MY_ACCESS_TOKEN)
	request = "me/friends"
	rawData = graph.get(request)
	
	return json.dumps(rawData)

@app.route("/api/v1/friends/<id>")

def pullFriendInfo(id):
	"""Pulls the profile picture and full name of a Facebook 
	user when a given id is passed through it"""
	graph = GraphAPI(MY_ACCESS_TOKEN)
	nameRequest = "/{}".format(id)
	name = graph.get(nameRequest)
	name = name['name']
	# picRequest = "/{}/picture".format(id)
	# picture = graph.get(picRequest).decode('utf-16')
	# return json.dumps({'name': name, 'picture': picture})
	return json.dumps({'name': name})

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)