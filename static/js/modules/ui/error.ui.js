export function showError(message) {
  const resultContainer = document.getElementById('result-container');
  resultContainer?.classList.add('hidden');

  let errorContainer = document.getElementById('error-container');

  if (!errorContainer) {
      errorContainer = document.createElement('div');
      errorContainer.id = 'error-container';
      errorContainer.className = 'mt-6 p-4 bg-red-50 border-l-4 border-red-400 rounded-xl animate-shake';
      document.querySelector('.container-wrapper')?.appendChild(errorContainer);
  }

  errorContainer.innerHTML = `
      <div class="flex items-center gap-3">
          <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
          <span class="text-red-700 font-medium">${message}</span>
      </div>
  `;
  errorContainer.classList.remove('hidden');
}