// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
angular.module('starter', ['ionic', 'starter.controllers', 'starter.services'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    if(window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }
    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
  });
})
.config(function($stateProvider, $urlRouterProvider) {
  
  $stateProvider.state('tab', {
    url: '/tab',
    abstract: true,
    templateUrl: 'templates/tabs.html'    
  })
  .state('tab.friends', {
    url: '/friends',
    views: {
      'friends': {
        templateUrl: "templates/friends.html",
        controller: 'MainController'
      }
    }
  })
  .state('tab.events', {
    url: '/events',
    views: {
      'events': {
        templateUrl: "templates/events.html",
        controller: 'MainController'
      }
    }
  })
  .state('tab.settings', {
    url: '/settings',
    views: {
      'settings': {
        templateUrl: "templates/settings.html",
        controller: 'MainController'
      }
    }
  })
  .state('date', {
    url: '/date',
    views: {
      'date': {
        templateUrl: "templates/date.html",
        controller: 'MainController'
      }
    }
  });
  $urlRouterProvider.otherwise('/tab/friends');

})