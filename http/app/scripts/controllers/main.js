'use strict';

/**
 * @ngdoc function
 * @name markovnewsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the markovnewsApp
 */
angular.module('markovnewsApp')
  .controller('MainCtrl', function ($scope, $timeout, Scraperwiki) {
    Scraperwiki.getSources().then(function(res){
      $scope.sources = res.data;
    });

    $scope.selectedPapers = 2;

    $scope.dateStart = undefined;
    $scope.dateEnd = undefined;
    $scope.output = [];
    $scope.markovOrder = 2;
    $scope.tokenLimit = 5;

    $scope.dateOptions = {
      format: 'yyyy-mm-dd',
      max: $scope.dateStart || new Date(), // TODO put in directive or something
    };

    $scope.generate = function() {
      Scraperwiki.getHeadlines($scope.selectedPapers, $scope.dateStart, $scope.dateEnd).then(function(res){
        var rows = res.data;
        var headlines = [];
        $scope.output = [];

        angular.forEach(rows, function(v){
          headlines.push(v.title);
        });

        console.dir(headlines.join('\n'));
        var m = nodemarkov(Number($scope.markovOrder));
        m.seed(headlines.join('\n'), function(){
          for (var i = 0; i < 20; i++) {
            var rando = m.pick();
            $scope.output.push(m.respond(rando, $scope.tokenLimit).join(' '));
          }
        });
      });
    };
  });
