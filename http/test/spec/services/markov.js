'use strict';

describe('Service: markov', function () {

  // load the service's module
  beforeEach(module('markovnewsApp'));

  // instantiate service
  var markov;
  beforeEach(inject(function (_markov_) {
    markov = _markov_;
  }));

  it('should do something', function () {
    expect(!!markov).toBe(true);
  });

});
