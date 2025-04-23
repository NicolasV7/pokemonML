export function setupBackButton() {
  const backButton = document.getElementById('back-button');
  if (!backButton) return;

  backButton.addEventListener('click', () => {
      const formContainer = document.getElementById('form-container');
      const resultContainer = document.getElementById('result-container');
      const errorContainer = document.getElementById('error-container');

      resultContainer?.classList.add('hidden');
      errorContainer?.classList.add('hidden');
      formContainer?.classList.remove('hidden');
  });
}