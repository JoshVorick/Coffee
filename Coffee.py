from facepy import GraphAPI
import json

from flask import Flask
app = Flask(__name__)

MY_ACCESS_TOKEN = "CAACEdEose0cBAAcIH7bK52rActX0AC6HwYQTYFHAoQUdpy40yLOkCniZAoolSgUt8RvTOZCAGv086J6yT9cstORRKBgZBWDyfFZBf1lZBfpQcCmeP05TZBZCnMZAPI38tjkJk8J6VwDkXQTFlJBzAbaQpQOP9ywsvkFTSpVZBPmy8tXzWG0Fa4ukR7uhmSYLa2yaXJwBY4Ee3FnG9Pm0DkPxS"

@app.route("/facebook")

def pullFriendsList():
	graph = GraphAPI(MY_ACCESS_TOKEN)
	request = "me/friends"
	rawData = graph.get(request)
	
	return json.dumps(rawData)

if __name__ == "__main__":
    app.run()