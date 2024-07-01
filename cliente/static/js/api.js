// URL de la API de REST Countries
const url = 'https://restcountries.com/v3/all';

// Función para obtener información de los países
async function obtenerInformacionPaises() {
  try {
    // Realizar una solicitud GET a la API de REST Countries
    const response = await fetch(url);

    // Convertir la respuesta a formato JSON
    const data = await response.json();

    // Devolver los datos de los países
    return data;
  } catch (error) {
    console.error('Error al obtener información de los países:', error);
    return null;
  }
}

// Función para mostrar la información de los países en el HTML
function mostrarInformacionPaises(paises) {
  const countriesDiv = document.getElementById('countries');
  let countriesHTML = '';

  // Recorrer los países y construir el HTML
  paises.forEach((pais) => {
    countriesHTML += `
      <div class="pais">
        <h2>${pais.name.common}</h2>
        <p>Capital: ${pais.capital}</p>
      </div>
    `;
  });

  // Agregar el HTML al elemento en el DOM
  countriesDiv.innerHTML = countriesHTML;
}

// Llamar a la función para obtener la información de los países y mostrarla en el HTML
obtenerInformacionPaises()
  .then((paises) => {
    if (paises) {
      mostrarInformacionPaises(paises);
    } else {
      console.log('No se pudieron obtener los datos de los países.');
    }
  })
  .catch((error) => {
    console.error('Error al obtener información de los países:', error);
  });