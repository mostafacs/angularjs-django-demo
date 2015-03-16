 
var token = '';
var contactsModule = angular.module("contacts",['ngRoute','ngResource','ngCookies']);

contactsModule.config(['$routeProvider','$httpProvider',

	
  function($routeProvider,$httpProvider) {
  	//$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	//$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  	//$httpProvider.defaults.withCredentials = true;
  	//$httpProvider.defaults.headers.post["x-csrf"]=123;
  	//alert(JSON.stringify($httpProvider.defaults.headers.post));
  	//$httpProvider.defaults.withCredentials = true;
    $routeProvider.
      when('/register', {
        templateUrl: 'views/register.html',
        controller: 'register'
      }).
      when('/phones/:phoneId', {
        templateUrl: 'partials/phone-detail.html',
        controller: 'PhoneDetailCtrl'
      }).
      otherwise({
        redirectTo: '/phones'
      });
  }]);