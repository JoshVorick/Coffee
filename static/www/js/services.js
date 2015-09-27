angular.module('starter.services', [])

.factory('MainService', function() {

})
.factory('UserService', function() {

	var users = [];
	var currentUser = {
		name: 'Sheehan Toufiq',
		bio: 'This is my bio',
		image: 'http://placehold.it/100x100'
	};
	var friends = [
		{
			_id: '1',
			name: 'Elon Musk',
			bio: 'Bossman',
			image: 'http://placehold.it/100x100',
			status: ''
		},
		{
			_id: '2',
			name: 'John Doe',
			bio: 'Im pretty boring',
			image: 'http://placehold.it/100x100',
			status: ''
		},
		{
			_id: '3',
			name: 'Goku',
			bio: 'Training in otherworld.',
			image: 'http://placehold.it/100x100',
			status: ''
		},
		{
			_id: '4',
			name: 'Rick James',
			bio: 'Im Rick James Bitch',
			image: 'http://placehold.it/100x100',
			status: 'fuck-off'
		},
		{
			_id: '5',
			name: 'Charlie Murphy',
			bio: 'Cocaine is one hell of a drug.',
			image: 'http://placehold.it/100x100',
			status: 'not-now'
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
			event_location: 'Taco Mac',
			event_friend: 'Elon Musk',
			event_status: ''
		},
		{
			_id: '2',
			event_type: 'coffee',
			event_date: 'Today',
			event_time: 'Afternoon',
			event_location: 'Starbucks',
			event_friend: 'Rick James',
			event_status: ''
		}
	];
	var newEvent = function(e) {
		this._id = '3';
		this.event_type = e.event_type;
		this.event_date = e.event_date;
		this.event_time = e.event_time;
		this.event_location = e.event_location;
	}

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
		}
	};
	return EventService;
});