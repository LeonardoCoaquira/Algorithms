$(document).ready(function() {
    $('#my-form').submit(function(event) {
      // Detener la acción por defecto de enviar el formulario
      event.preventDefault();
  
      // Obtener los datos del formulario
      var formData = $('#my-form').serialize();
  
      // Hacer la petición AJAX
      $.ajax({
        type: 'POST',
        url: '/submit',
        data: formData,
        success: function(response) {
          $('#result').text(response);
        }
      });
    });
  });
  