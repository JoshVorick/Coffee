angular.module('starter.controllers', [])

.controller('MainController', function($scope, $state, $ionicModal, $timeout, UserService, EventService) {

  $scope.user = UserService.getUser();
  $scope.events = EventService.getEvents();
  $scope.friends = UserService.getFriends();
  $scope.merchants = EventService.getMerchants();


  $scope.newEvent = {
    event_type: "",
    event_date: "",
    event_time: "",
    event_location: "",
    event_friend: ""
  }; 

  $scope.removeFriend = function(friendId) {
    UserService.deleteFriend(friendId);
  };
  $scope.removeEvent = function(eventId) {
    EventService.deleteEvent(eventId);
  };

  $ionicModal.fromTemplateUrl('templates/date.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  $ionicModal.fromTemplateUrl('templates/time.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modalTime = modal;
  });

  $ionicModal.fromTemplateUrl('templates/merchants.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modalLocation = modal;
  });

  // Triggered in the modal to close it
  $scope.closeModal = function() {
    $scope.modal.hide();
    $scope.modalTime.hide();
    $scope.modalLocation.hide();
  };

  var colors = ['assertive', 'energized', 'royal', 'positive', 'calm', 'balanced', 'dark'];
  $scope.color = colors[Math.floor((Math.random() * 6))];

  // Open the date modal
  $scope.createDate = function(type, friendId) {
    var pos = $scope.friends.map(function(e) { return e._id; }).indexOf(friendId);
    var friendName = $scope.friends[pos].name;
    $scope.newEvent.event_type = type;
    console.log(friendName);
    $scope.newEvent.event_friend = friendName;
    $scope.modal.show();
  };

  // Open the login modal
  $scope.createTime = function(date) {
    $scope.newEvent.event_date = date;
    $scope.modalTime.show();
    $scope.modal.hide();
  };

  $scope.createLocation = function(time) {
    $scope.newEvent.event_time = time;
    $scope.modalLocation.show();
    $scope.modalTime.hide();
  };

  $scope.createEvent = function(location) {
    $scope.newEvent.event_location = location;
    $scope.modalLocation.hide();
    EventService.createEvent($scope.newEvent);
  };


  $scope.color = 'assertive',

  $scope.chooseColor = function() {
    var count = 1;
    while ($scope.colors.length < 7) {
      $scope.color = 'assertive',
      count++;
    }

  };
  

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };

});
