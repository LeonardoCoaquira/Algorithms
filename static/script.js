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
        data: $('#formulario').serialize(),
        success: function(response) {
          $('#result').html(response.tabla);
        }
      });
    });
  });
  