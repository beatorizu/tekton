/**
 * Created by Bea on 28/05/2015.
 */
var lessonModule = angular.module('lessonModule',['rest']);

lessonModule.directive('lessonform', function() {
   return {
       restrict: 'E',
       replace: true,
       templateUrl: '/static/lesson/html/lesson_form.html',
       scope: {
           lesson: '=',
           tituloLabel: '@',
           descricaoLabel: '@'
       },
       controller: function($scope, LessonApi) {
           $scope.savingFlag = false;
           $scope.salvar = function() {
               $scope.savingFlag = true;
               $scope.erros = {};
               var promisse = LessonApi.salvar($scope.lesson);
               promisse.success(function(lesson) {
                   console.log(lesson);
                   $scope.lesson.titulo = '';
                   $scope.lesson.descricao = '';
                   $scope.savingFlag = false;
               })
               promisse.error(function(erros) {
                   $scope.erros = erros;
                   console.log(erros);
                   $scope.savingFlag = false;
               });
           }
       }
   };
});

lessonModule.directive('lesson legal', function() {
   return {
       restrict: 'E',
       replace: true,
       templateUrl: '/static/lesson/html/lesson_form.html',
       scope: {
           lesson: '=',
           tituloLabel: '@',
           descricaoLabel: '@'
       },
       controller: function($scope, LessonApi) {
           $scope.savingFlag = false;
           $scope.salvar = function() {
               $scope.savingFlag = true;
               $scope.erros = {};
               var promisse = LessonApi.salvar($scope.lesson);
               promisse.success(function(lesson) {
                   console.log(lesson);
                   $scope.lesson.titulo = '';
                   $scope.lesson.descricao = '';
                   $scope.savingFlag = false;
               })
               promisse.error(function(erros) {
                   $scope.erros = erros;
                   console.log(erros);
                   $scope.savingFlag = false;
               });
           }
       }
   };
});