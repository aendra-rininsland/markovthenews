'use strict';

/**
 * @ngdoc service
 * @name markovnewsApp.scraperwiki
 * @description
 * # scraperwiki
 * Service in the markovnewsApp.
 */
angular.module('markovnewsApp')
  .service('Scraperwiki', function ($http) {
    var scraperwikiUrl = scraperwiki.readSettings() ? scraperwiki.readSettings().target.url : 'https://premium.scraperwiki.com/zyskktk/kq2sjjdqal3jkcy';
    this.getSources = function() {
      var query = 'SELECT distinct origin FROM headlines';
      return $http.get(scraperwikiUrl + '/sql', {
        params: {
          q: query
        }
      });
    };

    this.getHeadlines = function(paper, from, to) {
      var select = 'SELECT title FROM headlines ';
      var where = paper ? 'WHERE origin == "' + paper + '" ' : ' ';
      where = from ? where + 'AND published > ' + from + ' ' : ' ';
      where = to ? where + 'AND published < ' + to + ' ' : ' ';
      var orderby = 'ORDER BY published DESC LIMIT 500';
      var query = select + where + orderby;
      console.log(query);
      return $http.get(scraperwikiUrl + '/sql', {
        params: {
          q: query
        }
      });
    };

  });
