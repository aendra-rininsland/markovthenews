'use strict';

//scraperwiki.readSettings().target.url + "/sqlite"

/**
 * @ngdoc overview
 * @name markovnewsApp
 * @description
 * # markovnewsApp
 *
 * Main module of the application.
 */
angular
  .module('markovnewsApp', [
    'ngAnimate',
    'ngAria',
    'ngCookies',
    'ngMessages',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'angular-datepicker'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
