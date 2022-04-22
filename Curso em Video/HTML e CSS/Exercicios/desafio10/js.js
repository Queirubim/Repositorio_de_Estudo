$(document).ready(function() {
    var botao = $('.bt1'); //classe que vai ser clicada
    var dropDown = $('.ul-not');  //classe que vai abrir  
   
       botao.on('click', function(event){
           dropDown.stop(true,true).slideToggle();
           event.stopPropagation();
       });
   });
   //Subtituir as 2 classes

   $(document).ready(function() {
    var botao = $('.bt2'); //classe que vai ser clicada
    var dropDown = $('.ul-cur');  //classe que vai abrir  
   
       botao.on('click', function(event){
           dropDown.stop(true,true).slideToggle();
           event.stopPropagation();
       });

   });$(document).ready(function() {
    var botao = $('.bt3'); //classe que vai ser clicada
    var dropDown = $('.ul-fal');  //classe que vai abrir  
   
       botao.on('click', function(event){
           dropDown.stop(true,true).slideToggle();
           event.stopPropagation();
       });
   });