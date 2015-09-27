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
	var friends = [];

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
			
		},
		updateFriend: function() {
			
		}
	};
	return UserService;
})
.factory('EventService', function() {

	var events = [];
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