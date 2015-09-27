angular.module('starter.services', [])

.factory('MainService', function() {

})
.factory('UserService', function() {

	var users = [];
	var currentUser = {
		first_name: 'Sheehan',
		last_name: 'Toufiq',
		bio: 'This is my bio',
		image: 'http://placehold.it/100x100'
	};
	var friends = [
		{
			_id: '1',
			first_name: 'Elon',
			last_name: 'Musk',
			bio: 'Bossman',
			image: 'http://placehold.it/100x100',
			status: ''
		},
		{
			_id: '2',
			first_name: 'John',
			last_name: 'Doe',
			bio: 'Im pretty boring',
			image: 'http://placehold.it/100x100',
			status: ''
		},
		{
			_id: '3',
			first_name: 'Goku',
			last_name: '',
			bio: 'Training in otherworld.',
			image: 'http://placehold.it/100x100',
			status: ''
		},
		{
			_id: '4',
			first_name: 'Rick',
			last_name: 'James',
			bio: 'Im Rick James Bitch',
			image: 'http://placehold.it/100x100',
			status: 'fuck-off'
		},
		{
			_id: '5',
			first_name: 'Charlie',
			last_name: 'Murphy',
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
		deleteEvent: function() {

		}
	};
	return EventService;
});