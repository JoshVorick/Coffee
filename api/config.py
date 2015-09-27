from authomatic.providers import oauth2

CONFIG = {
	'fb': {
	'class_': oauth2.Facebook,

	# Facebook is an AuthorizationProvider too.
        'consumer_key': '883030211746778',
        'consumer_secret': 'd3c627235a423cc7ebc7ccb564cea7a2',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['public_profile', 'email', 'user_friends']
	}
}
