angular.module('starter.services', [])

.factory('MainService', function() {

})
.factory('UserService', function() {

	var users = [];
	var currentUser = {
		name: 'Sheehan Toufiq',
		bio: 'This is my bio',
		image: 'https://scontent.xx.fbcdn.net/hprofile-xft1/v/t1.0-1/p50x50/11822361_10204744803556409_4436723064704007126_n.jpg?oh=1fcd50e2037dbdf5ad8dd5165a496f19&oe=5690FB0C'
	};
	var friends = [
		{
			_id: '1',
			name: 'Murtaza Bambot',
			bio: 'Caffeine dependent lifeform.',
			image: 'https://scontent.xx.fbcdn.net/hprofile-xpt1/v/t1.0-1/p50x50/11892082_10205764109235430_3719144021167908461_n.jpg?oh=4922b4a51dc0d205a4a4dad71c2e6411&oe=569582CB',
			status: ''
		},
		{
			_id: '2',
			name: 'Josh Vorick',
			bio: 'Naturally and artificially flavored.',
			image: 'https://scontent.xx.fbcdn.net/hprofile-xta1/v/t1.0-1/p50x50/12006158_10205185064009643_6679842642211992409_n.jpg?oh=0fcee24391b4a3b8ac2568ea0d5ebf73&oe=56948BD7',
			status: ''
		},
		{
			_id: '3',
			name: 'Manas George',
			bio: 'OMG no one cares.',
			image: 'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xpf1/v/t1.0-1/p50x50/10426694_10205895139714220_3493950187191357801_n.jpg?oh=76cb462e4256e7104b851399f709e813&oe=569D7C81&__gda__=1452368743_cdcfcbe33d886b66e9bbb89464bb47ba',
			status: 'fuck-off'
		}
	];

	var UserService = {
		getUser: function() {
			return currentUser;
		},
		getUsers: function() {

		},
		createUser: function() {
			
		},
		updateUser: function() {
			
		},
		deleteUser: function() {

		},
		getFriends: function() {
			return friends;
		},
		updateFriend: function() {
			
		},
		deleteFriend: function(friendId) {
			var pos = friends.map(function(e) { return e._id; }).indexOf(friendId);
			friends.splice(pos, 1);
		}
	};
	return UserService;
})
.factory('EventService', function() {

	var events = [
		{
			_id: '1',
			event_type: 'pizza',
			event_date: 'Today',
			event_time: 'Evening',
			event_location: 'Fatburger',
			event_friend: 'Murtaza Bambot',
			event_status: ''
		},
		{
			_id: '2',
			event_type: 'coffee',
			event_date: 'Today',
			event_time: 'Afternoon',
			event_location: 'Starbucks',
			event_friend: 'Josh Vorick',
			event_status: ''
		}
	];
	var merchants = [
		{
			_id: '1',
			name: 'Firehouse Subs',
			type: 'pizza',
			color: 'assertive'
		},
		{
			_id: '2',
			name: 'Fatburger',
			type: 'pizza',
			color: 'energized'
		},
		{
			_id: '3',
			name: 'Qdoba Mexican Grill',
			type: 'pizza',
			color: 'royal'
		},
		{
			_id: '4',
			name: 'Zaxbys',
			type: 'pizza',
			color: 'positive'
		},
		{
			_id: '5',
			name: 'Chipotle',
			type: 'pizza',
			color: 'calm'
		},
		{
			_id: '6',
			name: 'Golden Coral',
			type: 'pizza',
			color: 'balanced'
		},
		{
			_id: '7',
			name: 'Taco Mac',
			type: 'pizza',
			color: 'dark'
		}
	];

	var newEvent = function(e) {
		this._id = '3';
		this.event_type = e.event_type;
		this.event_date = e.event_date;
		this.event_time = e.event_time;
		this.event_location = e.event_location;
		this.event_friend = e.event_friend;
		this.event_status = '';

	};

	var EventService = {
		getEvent: function() {

		},
		getEvents: function() {
			return events;
		},
		createEvent: function(e) {
			var createNewEvent = new newEvent(e);
			events.push(createNewEvent);
		},
		updateEvent: function() {
			
		},
		deleteEvent: function(eventId) {
			var pos = events.map(function(e) { return e._id; }).indexOf(eventId);
			events.splice(pos, 1);
		},
		getMerchants: function() {
			return merchants;
		}
	};
	return EventService;
});