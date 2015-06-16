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
           descricaoLabel: '@',
           temaLabel: '@',
           temas: '=',
           saveComplete: '&'
       },
       controller: function ($scope, LessonApi) {
            $scope.savingFlag = false;
            $scope.salvar = function () {
                $scope.savingFlag = true;
                $scope.erros = {};
                var promisse = LessonApi.salvar($scope.lesson);
                promisse.success(function (lesson) {
                    console.log(lesson);
                    if ($scope.saveComplete != undefined) {
                        $scope.saveComplete({'lesson': lesson});
                    }
                    $scope.lesson.titulo = '';
                    $scope.lesson.descricao = '';
                    $scope.lesson.tema = '';
                    $scope.savingFlag = false;
                })
                promisse.error(function (erros) {
                    $scope.erros = erros;
                    console.log(erros);
                    $scope.savingFlag = false;
                });
            }
        }
   };
});

lessonModule.directive('lessonlinha', function () {
    return {
        restrict: 'A',
        replace: true,
        templateUrl: '/static/lesson/html/lesson_linha_tabela.html',
        scope: {
            lesson: '=',
            deleteComplete: '&'
        },
        controller: function ($scope, LessonApi) {
            $scope.ajaxComplete = false;
            $scope.editFlag = false;
            $scope.lessonEdicao = {};
            $scope.deletar = function() {
                $scope.ajaxComplete = true;
                LessonApi.deletar($scope.lesson.id).success(function() {
                    $scope.deleteComplete({'lesson':$scope.lesson});
                });
            }
            $scope.editar = function() {
                $scope.editFlag = true;
                $scope.lessonEdicao.id = $scope.lesson.id;
                $scope.lessonEdicao.titulo = $scope.lesson.titulo;
                $scope.lessonEdicao.descricao = $scope.lesson.descricao;
                $scope.lessonEdicao.tema = $scope.lesson.tema;
            }
            $scope.cancelarEdicao = function() {
                $scope.editFlag = false;
            }
            $scope.completarEdicao = function() {
                LessonApi.editar($scope.lessonEdicao).success(function(lesson) {
                    $scope.lesson = lesson;
                    $scope.editFlag = false;
                    console.log(lesson);
                }).error(function(erros) {
                    $scope.erros = erros;
                });
            }
        }
    };
});

lessonModule.directive('lessonfilter', function() {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/lesson/html/lesson_filter_form.html',
        scope: {
            temas: '='
        },
        controller: function($scope, LessonApi) {
            $scope.filtrandoFlag = false;
            $scope.tema = '';
            $scope.filtrar = function() {
                $scope.filtrandoFlag = true;
                LessonApi.filtrar($scope.tema).success(function(lessons) {
                    $scope.lessonLista = lessons;
                    console.log($scope.lessonLista);
                    $scope.filtrandoFlag = false;
                })
            }
        }
    };
});