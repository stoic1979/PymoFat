function myFunction() {
    var x = document.getElementById('myDIV');
    if (x.style.display === 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}


var app = angular.module('myApp', [])
    .controller('todoCtrl', function($scope) {
        $scope.todoList = [{ text:'day work ',done: false }
            ];

        $scope.todoAdd = function() 
        {
            $scope.todoList.push({text:$scope.todoInput, done:false});
                $scope.todoInput = "";
        };

        $scope.remove = function() {
            var oldList = $scope.todoList;
            $scope.todoList = [];
            angular.forEach(oldList, function(x) {
                if (!x.done) $scope.todoList.push(x);
            });
        };
    })
    .config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('[[').endSymbol(']]');
    });