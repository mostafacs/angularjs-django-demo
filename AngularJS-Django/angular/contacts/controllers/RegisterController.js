
contactsModule.controller("register",function($scope,$http,UserService,TokenService){
	TokenService();
	$scope.user = {};

	

	$scope.show = function(){
	
		var response = UserService.register({token: token},$scope.user);/*.then(function(registeredUser){
			alert(registeredUser);
		},function (error){
			alert(error);
		}) */
		alert('response == '+JSON.stringify( response) );

		//$http.get("http://127.0.0.1:8000/users/").success(
		//	function(response) { alert(JSON.stringify(response)); });
	};

});


contactsModule.controller("auth",function($scope,$http,$cookies,AuthService,TokenService,CheckLogin){

	$scope.email = '';
	$scope.password='';
	TokenService();
	//token = 'GbwXnl04gp9vGRGcfq0zCKHFG7tGelQR';
	//$cookies.x-csrftoken = 'GbwXnl04gp9vGRGcfq0zCKHFG7tGelQR';
	$scope.login=function(){
		
	    AuthService.login({token:token},{email:$scope.email , password:$scope.password}).$promise.then(
				function(response){
					alert('sessionid = '+response.sessionid);
					$cookies.sessionid = response.sessionid;
					alert('response == '+JSON.stringify( response) );
					
				}
			);
		
	};


	$scope.check = function(){

		var sessionid = $cookies.sessionid;
		var csrf = $cookies.csrftoken;
		alert(sessionid);
		alert(csrf);
		//$http.defaults.headers.post.Cookies = 'sessionid='+sessionid;
		$http.defaults.headers.common['X-CSRFToken']= csrf;
		CheckLogin.check({token:token},{}).$promise.then(
				function(response){
					alert('response == '+JSON.stringify( response) );
					
				}
			);

	}

});