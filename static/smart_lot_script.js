var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {

//$scope.fetch();
$scope.fetch = function(){

console.log("Inside Fetch");
var url = "http://134.124.131.54:5050/basicServer/services/getAllParkingData";
var url2 = "https://jsonplaceholder.typicode.com/posts/1";
  $http.get(url2).then(function(response){
    alert(response);
  });
};

$scope.floor1 = "12";
$scope.floor2 = "2";

$scope.change = function(){

  if(Number($scope.floor1) > 20) {
    $scope.floor1Col = "red";
    $scope.floor1Space = "No Vacancy";
  }

  if(Number($scope.floor1) <= 20) {
    $scope.floor1Col = "green";
    $scope.floor1Space = "Vacancy";
  }


  if(Number($scope.floor2) > 20) {
    $scope.floor2Col = "red";
    $scope.floor2Space = "No Vacancy";
  }

  if(Number($scope.floor2) <= 20) {
    $scope.floor2Col = "green";
    $scope.floor2Space = "Vacancy";
  }

  $scope.total_cars = Number($scope.floor1) + Number($scope.floor2);

}

});
