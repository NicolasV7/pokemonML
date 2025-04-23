import { setupFormHandler } from './modules/api/predictor.api.js';
import { setupBackButton } from './modules/ui/transitions.ui.js';

export function initApp() {
    setupFormHandler();
    setupBackButton();
}