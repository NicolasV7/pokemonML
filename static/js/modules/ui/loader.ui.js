export function showLoading() {
  const formContainer = document.getElementById('form-container');
  const loadingContainer = document.getElementById('loading-container');
  const errorContainer = document.getElementById('error-container');

  formContainer?.classList.add('hidden');
  errorContainer?.classList.add('hidden');
  loadingContainer?.classList.remove('hidden');
}

export function hideLoading() {
  const loadingContainer = document.getElementById('loading-container');
  loadingContainer?.classList.add('hidden');
}