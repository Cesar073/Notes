function change_page(){
    $.ajax({
        url: "/",
        type: "post",
        dataType: "json",
        success: function(response){
            
        }
    });
}

$(document).ready(function() {
    $('{{ page.id }}').click(function() {
      var id = $(this).data('id'); // Accede al atributo data-id del elemento clicado
      $.ajax({
        url: '/', // Reemplaza '/backend-url' con la URL de tu backend
        type: 'POST',
        data: { id: id }, // Pasa el ID al backend como parte de los datos
        success: function(response) {
          console.log(response); // Haz algo con la respuesta del backend
        },
        error: function() {
          console.error("No es posible completar la operación");
        }
      });
    });
  });