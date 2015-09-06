/**
 * Created by bea on 06/09/15.
 */
var cardModule = angular.module('cardModule', []);

cardModule.directive('cardform', function () {
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/card/html/card_form.html'
    };
});