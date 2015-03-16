
contactsModule.factory('UserService', ['$resource' ,function($resource){

return $resource('http://127.0.0.1:8000/users/?csrfmiddlewaretoken=:token',null,{

  register : {
      method : "POST"     
  }

});


}]);


contactsModule.factory('AuthService',['$resource' , function($resource){

return $resource('http://127.0.0.1:8000/login2/?csrfmiddlewaretoken=:token',null,{

login : {
  method : "POST",
  withCredentials : false
}

});

}]);

contactsModule.factory('CheckLogin',['$resource','$http' , function($resource,$http){


//$http.defaults.headers.post.Cookies = sessionid+' '+csrf;
return $resource('http://127.0.0.1:8000/check/login/?csrfmiddlewaretoken=:token',null,{

check : {
  method : "POST"
}

});

}]);

contactsModule.factory('TokenService',['$http','$cookies',function($http,$cookies){

return function(){
  //token = $cookies.csrftoken;
  alert(token);
 // if(token === '' || token === undefined){
     $http.get("http://127.0.0.1:8000/token",{withCredentials:false}).success(
      function(response) { 
        token = response;
        $cookies.csrftoken = token;
        $cookies["X-CSRFToken"]=token;
        alert('token Set');
        return token;
      });
    
  //}
  /*else{
     $cookies["X-CSRFToken"]=token;

      contactsModule.config(['$httpProvider',

  
  function($httpProvider) {
    $httpProvider.defaults.headers.post["X-CSRFToken"]=token;
    alert(JSON.stringify($httpProvider.defaults.headers.post));
    
  
  }]);
        alert('token Set = '+$cookies["X-CSRFToken"]);

    return token;
  }*/
  }

}]);




