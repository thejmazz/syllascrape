'use strict';

var mongoose = require('mongoose'),
    Schema = mongoose.Schema;

var PytestSchema = new Schema({
  name: String
});

module.exports = mongoose.model('Pytest', PytestSchema);