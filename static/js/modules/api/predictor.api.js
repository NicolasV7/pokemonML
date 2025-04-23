import { showLoading, hideLoading } from '../ui/loader.ui.js';
import { showError } from '../ui/error.ui.js';
import { displayResults } from '../ui/results.ui.js';
import { animateTyping } from '../utils/typewriter.utils.js';

export function setupFormHandler() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', async (event) => {
            event.preventDefault();
            await handleFormSubmission(event.target);
        });
    }
}

async function handleFormSubmission(form) {
    try {
        showLoading();

        const formData = new FormData(form);
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            throw new Error(data.error || 'Failed to analyze Pokémon');
        }

        displayResults(data);
        animateTyping();
    } catch (error) {
        showError(error.message);
    } finally {
        hideLoading();
    }
}