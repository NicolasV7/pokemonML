export function displayResults(data) {
  const resultContainer = document.getElementById('result-container');
  const clusterName = document.getElementById('cluster-name');
  const typewriterText = document.getElementById('typewriter-text');

  if (!resultContainer || !clusterName || !typewriterText) return;

  clusterName.textContent = data.prediction.nombre;
  typewriterText.textContent = data.prediction.descripcion;

  updatePokemonList('famous-examples', data.prediction.ejemplos);
  updatePokemonList('similar-pokemon', data.examples);

  resultContainer.classList.remove('hidden');
}

function updatePokemonList(elementId, pokemonList) {
  const container = document.getElementById(elementId);
  if (!container) return;

  container.innerHTML = pokemonList.map(pokemon => `
      <div class="flex items-center gap-1 px-2 py-0.5 bg-red-100 text-red-700
               rounded-full text-xs sm:px-3 sm:py-1 sm:text-sm">
          <img src="/static/images/${pokemon.image}"
               alt="${pokemon.name}"
               class="w-5 h-5 object-contain sm:w-6 sm:h-6">
          ${pokemon.name}
      </div>
  `).join('');
}