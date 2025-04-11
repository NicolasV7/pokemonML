function handleSubmit(event) {
    event.preventDefault();

    const formContainer = document.getElementById('form-container');
    const loadingContainer = document.getElementById('loading-container');
    const resultContainer = document.getElementById('result-container');

    if (!formContainer || !loadingContainer || !resultContainer) {
        console.error('One or more elements are missing in the DOM.');
        return;
    }

    formContainer.classList.add('hidden');
    loadingContainer.classList.remove('hidden');

    setTimeout(() => {
        loadingContainer.classList.add('hidden');
        resultContainer.classList.remove('hidden');
        animateTyping();
    }, 1500);

    const formData = new FormData(event.target);
    fetch(event.target.action, {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            if (data.prediction) {
                resultContainer.classList.remove('hidden');
                document.getElementById('typewriter-text').innerText = data.prediction.descripcion;
            } else {
                console.error('Prediction data is missing');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
function animateTyping() {
    const description = document.getElementById('typewriter-text');
    const text = description.innerText;
    description.innerText = '';

    let i = 0;
    const typing = setInterval(() => {
        description.innerText += text[i];
        i++;
        if (i >= text.length) clearInterval(typing);
    }, 20);
}