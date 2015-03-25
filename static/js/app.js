function TutoCtrl($scope, $http) {

    $scope.send = function() {
        $http.post('/query', $scope.query)
             .success(function(){alert('ok')})
             .error(function(){alert('fail')});
    }

}
