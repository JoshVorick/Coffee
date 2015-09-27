angular.module('starter.controllers', [])

.controller('MainController', function($scope, $state, $ionicModal, $timeout, UserService, EventService) {

  $scope.user = UserService.getUser();
  $scope.events = EventService.getEvents();
  $scope.friends = UserService.getFriends();

  $scope.newEvent = {
    event_type: "",
    event_date: "",
    event_time: "",
    event_location: "",
    event_friend: ""
  };

  $scope.createEvent = function() {
    
    $state.go('/settings');
    //EventService.createEvent($scope.newEvent);
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

  // Triggered in the modal to close it
  $scope.closeModal = function() {
    $scope.modal.hide();
    $scope.modalTime.hide();
  };

  // Open the date modal
  $scope.createDate = function() {
    $scope.modal.show();
  };

  // Open the login modal
  $scope.createTime = function() {
    $scope.modal.hide();
    $scope.modalTime.show();
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
