'use strict';

describe('Service: scraperwiki', function () {

  // load the service's module
  beforeEach(module('markovnewsApp'));

  // instantiate service
  var scraperwiki;
  beforeEach(inject(function (_scraperwiki_) {
    scraperwiki = _scraperwiki_;
  }));

  it('should do something', function () {
    expect(!!scraperwiki).toBe(true);
  });

});
