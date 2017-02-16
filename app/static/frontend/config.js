function config($stateProvider, $urlRouterProvider, $locationProvider) {
  $locationProvider.html5Mode(true);

  $urlRouterProvider.otherwise("/");

  $stateProvider
    .state('main', {
      url: '#/main',
      template: require('./areas/main-tpl.html'),
      controller: 'MainCtrl as vm',
      title: '',
    })
    .state('loading',{
      url:'/',
      template: require('./areas/loading-tpl.html'),
      // controller: "LoadingCtrl",
      resolve:{
        deps:['$rootScope','MainService',"$state",function($rootScope,MainService,$state){
          setTimeout(function () {
            $state.go('main')
          }, 1000);
        }]
      }
    })

}

export default ['$stateProvider', '$urlRouterProvider', '$locationProvider', config];
