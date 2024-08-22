// desaparece contenido de tarjetas
$(document).ready(function(){
    $(".card-title").click(function(){
          $(".card-text").toggle();
    });
    });