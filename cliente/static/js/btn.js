//getElementById=obtener elemento de aqui
const botonPago = document.getElementById('botonPago');
const boton1 = document.getElementById('boton1');
const boton2 = document.getElementById('boton2');
const textoMostrado1 = document.getElementById('textoMostrado1');
const textoMostrado2 = document.getElementById('textoMostrado2');

const numeroFijo = 10; // Número fijo que deseas mostrar en el texto
const numer = 900;

//addEventListener= le agrego un evento


boton1.addEventListener('click', function() {
  const total = numer + numeroFijo;
  textoMostrado1.textContent = "Envío: $" + numeroFijo;
  textoMostrado2.textContent = "Total: $" + total;
  actualizarTextoPago(total);
});

boton2.addEventListener('click', function() {
  const total = numer;
  textoMostrado1.textContent = "Retiro en tienda: Viña del mar";
  textoMostrado2.textContent = "Total: $" + numer;
  actualizarTextoPago(total);
});

function actualizarTextoPago(total) {
  botonPago.textContent = "Pagar = $" + total;
}