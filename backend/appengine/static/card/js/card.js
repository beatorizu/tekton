/**
 * Created by bea on 06/09/15.
 */
var cardModule = angular.module('cardModule', ['rest']);

cardModule.directive('cardform', function () {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/card/html/card_form.html',
        scope: {
            card: '=',
            fraseLabel: '@',
            respostaLabel: '@',
            alternativa0Label: '@',
            alternativa1Label: '@',
            alternativa2Label: '@',
            saveComplete: '&',
        },
        controller: function($scope, CardApi) {
            $scope.savingFlag = false;
            $scope.salvar = function () {
                $scope.savingFlag = true;
                $scope.erros = {};
                var promisse = CardApi.salvar($scope.card);
                promisse.success(function (card) {
                    console.log(card);
                    if ($scope.saveComplete != undefined) {
                        $scope.saveComplete({'card': card});
                    }
                    $scope.card.frase = '';
                    $scope.card.resposta = '';
                    $scope.card.alternativa0 = '';
                    $scope.card.alternativa1= '';
                    $scope.card.alternativa2 = '';
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

cardModule.directive('cardblock', function() {
    return {
        restrict: 'A',
        replace: true,
        templateUrl: '/static/card/html/card_grid_block.html',
        scope: {
            card: '=',
            deleteComplete: '&'
        },
        controller: function($scope, CardApi) {
            $scope.cardEdicao = {};
            $scope.editar = function() {
                $scope.cardEdicao.id = $scope.card.id;
                $scope.cardEdicao.frase = $scope.card.frase;
                $scope.cardEdicao.resposta = $scope.card.resposta;
                $scope.cardEdicao.alternativa0 = $scope.card.alternativa0;
                $scope.cardEdicao.alternativa1 = $scope.card.alternativa1;
                $scope.cardEdicao.alternativa2 = $scope.card.alternativa2;

            }
        }
    }
});