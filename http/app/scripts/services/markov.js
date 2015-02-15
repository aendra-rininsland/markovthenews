'use strict';

/**
 * @ngdoc service
 * @name markovnewsApp.markov
 * @description
 * # markov
 * Service in the markovnewsApp.
 */
angular.module('markovnewsApp')
  .run(function(markov){})
  .service('markov', function ($window) {
    var markov = $window.markov;
    delete($window.markov);
    return markov;
  });
