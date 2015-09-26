from authomatic.providers import oauth2

CONFIG = {
	'fb': {
	'class_': oauth2.Facebook,

	# Facebook is an AuthorizationProvider too.
        'consumer_key': '521483501348976',
        'consumer_secret': '42977fbac8f368a0755b8a1106984823',
        
        # But it is also an OAuth 2.0 provider and it needs scope.
        'scope': ['public_profile', 'email', 'user_friends']
	}
}