function handleSubmit(event) {
  event.preventDefault();

  const formContainer = document.getElementById('form-container');
  const loadingContainer = document.getElementById('loading-container');
  const resultContainer = document.getElementById('result-container');
  const errorContainer = document.getElementById('error-container');

  formContainer.classList.add('hidden');
  loadingContainer.classList.remove('hidden');
  if (errorContainer) errorContainer.classList.add('hidden');

  const formData = new FormData(event.target);

  fetch(event.target.action, {
      method: 'POST',
      body: formData,
  })
      .then(response => response.json())
      .then(data => {
          if (data.error) {
              throw new Error(data.error);
          }

          updateResults(data);
          loadingContainer.classList.add('hidden');
          resultContainer.classList.remove('hidden');
          animateTyping();
      })
      .catch(error => {
          handleError(error, loadingContainer, resultContainer);
      });
}

function updateResults(data) {
  document.getElementById('typewriter-text').innerText = data.prediction.descripcion;
  document.getElementById('cluster-name').innerText = data.prediction.nombre;

  updatePokemonList('famous-examples', data.prediction.ejemplos);
  updatePokemonList('similar-pokemon', data.examples);
}

function updatePokemonList(elementId, pokemonList) {
  const container = document.getElementById(elementId);
  container.innerHTML = pokemonList.map(pokemon => `
      <div class="flex items-center gap-1 px-2 py-0.5 bg-red-100 text-red-700
               rounded-full text-xs sm:px-3 sm:py-1 sm:text-sm">
          <img src="/static/images/${pokemon.image}" class="w-5 h-5 object-contain sm:w-6 sm:h-6">
          ${pokemon.name}
      </div>
  `).join('');
}

function handleError(error, loadingContainer, resultContainer) {
  console.error('Error:', error);
  loadingContainer.classList.add('hidden');
  resultContainer.classList.add('hidden');

  const errorHtml = `
      <div class="flex items-center gap-3">
          <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <!-- Icono de error -->
          </svg>
          <span class="text-red-700 font-medium">${error.message}</span>
      </div>
  `;

  let errorContainer = document.getElementById('error-container');
  if (!errorContainer) {
      errorContainer = document.createElement('div');
      errorContainer.id = 'error-container';
      errorContainer.className = 'mt-6 p-4 bg-red-50 border-l-4 border-red-400 rounded-xl animate-shake';
      errorContainer.innerHTML = errorHtml;
      document.querySelector('.container-wrapper').appendChild(errorContainer);
  } else {
      errorContainer.innerHTML = errorHtml;
      errorContainer.classList.remove('hidden');
  }
}

function animateTyping() {
  const description = document.getElementById('typewriter-text');
  const text = description.textContent;
  description.textContent = '';

  let i = 0;
  const typing = setInterval(() => {
      description.textContent += text[i];
      i++;
      if (i >= text.length) clearInterval(typing);
  }, 20);
}

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('back-button')?.addEventListener('click', () => {
      const formContainer = document.getElementById('form-container');
      const resultContainer = document.getElementById('result-container');

      resultContainer.classList.add('hidden');
      formContainer.classList.remove('hidden');
  });
});