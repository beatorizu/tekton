/**
 * Created by Bea on 01/06/2015.
 */
var rest = angular.module('rest',[]);
rest.factory('TemaApi',function($rootScope) {
       return {
           salvar: function(tema) {
               var obj = {};
               obj.success = function(fcnSuccess) {
                   obj.fcnSuccess = fcnSuccess;
               };
               obj.error = function(fcnError) {
                   obj.fcnError = fcnError;
               };
               setTimeout(function() {
                   tema.id = 1;
                   obj.fcnSuccess(tema);
                   $rootScope.$digest();
               }, 1000);
               return obj;
           }
       };
    });