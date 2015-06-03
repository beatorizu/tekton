/**
 * Created by Bea on 28/05/2015.
 */
var temaModule = angular.module('temaModule',['rest']);

temaModule.directive('temaform', function() {
   return {
       restrict: 'E',
       replace: true,
       templateUrl: '/static/tema/html/tema_form.html',
       scope: {
           tema: '=',
           tituloLabel: '@',
           descricaoLabel: '@'
       },
       controller: function($scope, TemaApi) {
           $scope.savingFlag = false;
           $scope.salvar = function() {
               $scope.savingFlag = true;
               $scope.erros = {};
               var promisse = TemaApi.salvar($scope.tema);
               promisse.success(function(tema) {
                   console.log(tema);
                   $scope.tema.titulo = '';
                   $scope.tema.descricao = '';
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

temaModule.directive('temalinha', function() {
   return {
       restrict: 'E',
       replace: true,
       templateUrl: '/static/tema/html/tema_linha_tabela.html',
       scope: {
           tema: '='
       },
       controller: function($scope, TemaApi) {
           $scope.savingFlag = false;
           $scope.salvar = function() {
               $scope.savingFlag = true;
               $scope.erros = {};
               var promisse = TemaApi.salvar($scope.tema);
               promisse.success(function(tema) {
                   console.log(tema);
                   $scope.tema.titulo = '';
                   $scope.tema.descricao = '';
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