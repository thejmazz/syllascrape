'use strict';

angular.module('syllascrapeApp')
  .config(function ($routeProvider) {
    $routeProvider
      .when('/files', {
        templateUrl: 'app/files/files.html',
        controller: 'FilesCtrl'
      });
  });
