var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {

$scope.floor1 = "12";
$scope.floor2 = "2";

$scope.myCol = "green";

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
