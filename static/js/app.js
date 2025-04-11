document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('prediction-form');
  if (form) {
      form.addEventListener('submit', handleSubmit);
  }
});

async function handleSubmit(event) {
  event.preventDefault();

  const elements = {
      form: document.getElementById('form-container'),
      loading: document.getElementById('loading-container'),
      result: document.getElementById('result-container'),
      error: document.querySelector('.error-container'),
      typewriter: document.getElementById('typewriter-text')
  };

  // Validar elementos
  if (!elements.form || !elements.loading || !elements.result) {
      console.error('Missing required elements');
      return;
  }

  // Mostrar carga
  elements.form.classList.add('hidden');
  elements.loading.classList.remove('hidden');

  try {
      const formData = new FormData(event.target);
      const response = await fetch(event.target.action, {
          method: 'POST',
          body: formData,
          headers: {
              'Accept': 'application/json'
          }
      });

      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

      const data = await response.json();

      if (data.error) throw new Error(data.error);
      if (!data.prediction) throw new Error('Invalid response format');

      // Actualizar resultados
      elements.loading.classList.add('hidden');
      elements.result.classList.remove('hidden');
      animateTyping(data.prediction.descripcion);

  } catch (error) {
      console.error('Error:', error);
      elements.loading.classList.add('hidden');
      elements.form.classList.remove('hidden');
      alert(`Error: ${error.message}`);
  }
}

function animateTyping(text) {
  const description = document.getElementById('typewriter-text');
  if (!description) {
      console.error('Typewriter element not found');
      return;
  }

  description.textContent = '';
  let i = 0;

  const typing = setInterval(() => {
      if (i < text.length) {
          description.textContent += text[i];
          i++;
      } else {
          clearInterval(typing);
      }
  }, 20);
}