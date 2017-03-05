var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http, $timeout) {

//$scope.fetch();
$scope.fetch = function(){

    console.log("Inside Fetch");
    var url = "http://134.124.131.54:5050/basicServer/services/getAllParkingData";
    var url2 = "https://jsonplaceholder.typicode.com/posts/1";
    $http.post(
                url,
                {},
                { cors: true }
                )
                .then(function (resp) {
                    // Success
                    console.log(resp);
                    $scope.totalCarsData = resp;
                    $scope.floor1 = resp.data["IN101"]["occupied"];
                    $scope.total = resp.data["IN101"]["total"];
                    $scope.floor2 = 6 + Number($scope.floor1);
                    $scope.floorTotal = Number($scope.floor1) + Number($scope.floor2);
                    $scope.garageTotal = 2 * Number($scope.total);
    //                alert("Success");
                },
                function (resp) {
//                    alert("failed");
                });
};

$scope.intervalFunction = function(){
    $timeout(function() {
      $scope.fetch();
      $scope.intervalFunction();
    }, 1000)
  };


$scope.intervalFunction();

});
