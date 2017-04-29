'use strict';
var app = angular.module('app', []);

app.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller('ScoresCtrl', function ($scope, $http) {
    $scope.clients = [];

    $http.get('/api/clients/').then(function (response) {
        $scope.clients = response.data;
    });


    $scope.increment_score = function (client_id) {
        $http({
            url: '/api/update_score/',
            method: "PATCH",
            data: {"client": client_id}
        })
            .success(function (data) {
                $http.get('/api/clients/').then(function (response) {
                    $scope.clients = response.data;
                });
            });
    }
});

app.config([
    '$httpProvider', function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);

