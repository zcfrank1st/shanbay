/**
 * Created by zcfrank1st on 7/18/15.
 */

var shanbay = angular.module('myapp', ['ngResource','ui.router','ngDialog']);

shanbay.config(function($interpolateProvider, $stateProvider, $urlRouterProvider, $sceProvider) {
    $stateProvider
        .state('state1', {
            url: "/",
            templateUrl: "/static/partials/config.html",
            controller: "configController"
        })
        .state('state2', {
            url: "/learn",
            templateUrl: "/static/partials/learn.html",
            controller: "learnController"
        });
    $urlRouterProvider.otherwise("/");

    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');

    $sceProvider.enabled(false);
});