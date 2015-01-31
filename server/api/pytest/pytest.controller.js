'use strict';

var _ = require('lodash');
var Pytest = require('./pytest.model');
var PythonShell = require('python-shell');

// Get list of pytests
exports.index = function(req, res) {
  var options = {
    scriptPath: __dirname
  };

  PythonShell.run('./hw.py',options, function (err, results) {
    if (err) throw err;
    return res.json(200, [{
      "results": results 
    }])
  });
  /*var options = {
    scriptPath: __dirname,
    args: [req.params.name]
  };

  PythonShell.run('./greet.py', options, function(err, results) {
      if (err) throw err;
      return res.json(200, [{
        "output" : results
      }]);
  });*/
};

// Get a single pytest
exports.show = function(req, res) {
  Pytest.findById(req.params.id, function (err, pytest) {
    if(err) { return handleError(res, err); }
    if(!pytest) { return res.send(404); }
    return res.json(pytest);
  });
};

exports.greet = function(req, res) {
  var options = {
    scriptPath: __dirname,
    args: [req.params.name]
  };

  PythonShell.run('./greet.py', options, function(err, results) {
      if (err) throw err;
      return res.json(200, [{
        "output" : results
      }]);
  });
};

exports.scrapUrl = function(req, res) {
  var options = {
    scriptPath: __dirname,
    args: [req.body.url]
  };

  PythonShell.run('/htmltotext.py', options, function(err, results) {
    if (err) throw err;
    return res.json(200, [{
      "output": results
    }]);
  });
}

// Creates a new pytest in the DB.
exports.create = function(req, res) {
  Pytest.create(req.body, function(err, pytest) {
    if(err) { return handleError(res, err); }
    return res.json(201, pytest);
  });
};

// Updates an existing pytest in the DB.
exports.update = function(req, res) {
  if(req.body._id) { delete req.body._id; }
  Pytest.findById(req.params.id, function (err, pytest) {
    if (err) { return handleError(res, err); }
    if(!pytest) { return res.send(404); }
    var updated = _.merge(pytest, req.body);
    updated.save(function (err) {
      if (err) { return handleError(res, err); }
      return res.json(200, pytest);
    });
  });
};

// Deletes a pytest from the DB.
exports.destroy = function(req, res) {
  Pytest.findById(req.params.id, function (err, pytest) {
    if(err) { return handleError(res, err); }
    if(!pytest) { return res.send(404); }
    pytest.remove(function(err) {
      if(err) { return handleError(res, err); }
      return res.send(204);
    });
  });
};

function handleError(res, err) {
  return res.send(500, err);
}