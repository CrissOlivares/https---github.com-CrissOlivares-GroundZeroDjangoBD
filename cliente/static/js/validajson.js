// Agrega un event listener
// Agrega un evento "DOMContentLoaded" al documento. Este evento se dispara cuando el DOM (Document Object Model)
// ha sido completamente cargado y parseado, sin necesidad de esperar a que se carguen otros recursos. 
// Cualquier código que quiero ejecutar una vez que el DOM esté listo.
// que es doom El Dom Representa la relación entre las etiquetas HTML

//addEventListener= le agrego un evento
//getElementById=obtener elemento de aqui
// document: Es un objeto global en JavaScript que representa el documento actual en el que se está ejecutando el código.

document.addEventListener('DOMContentLoaded', function() {
    // Selecciona el formulario , queryselector= seleccionar elementos del DOM (Document Object Model) utilizando un selector CSS
    const form = document.querySelector('.needs-validation');
  
    // Selecciona el botón de pago
    const botonPago = document.getElementById('botonPago');
  
    // Agrega un evento de escucha para el clic en el botón de pago
    botonPago.addEventListener('click', function(event) {
        // Verifica si el formulario es válido
        if (!form.checkValidity()) {
            // Si el formulario no es válido, evita que se envíe
            event.preventDefault(); // se detiene
            event.stopPropagation();//y se detiene la propagacion
        }
  
        // Agrega las clases de validación de Bootstrap para activar estilos específicos, mostrar mensajes de error, o resaltar los campos inválidos.
        form.classList.add('was-validated');
    });
});

// Agrega un evento de escucha al input del número de tarjeta de crédito para dar formato
document.getElementById('validationCustom02').addEventListener('input', function (e) {
    var target = e.target;//e.target es una propiedad de este objeto evento que hace referencia al elemento en el DOM que desencadenó el evento.
    // Obtiene solo los dígitos numéricos del valor actual del campo, eliminando todos los caracteres que no sean dígitos de la cadena
    var input = target.value.replace(/\D/g, '');
    // Si el valor es un número de tarjeta de crédito válido (16 dígitos), lo formatea
    if (/^\d{16}$/.test(input)) {
        var formattedInput = input.replace(/(\d{4})/g, '$1 ');
        target.value = formattedInput.trim();
    }
});
