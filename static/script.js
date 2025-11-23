document.addEventListener('DOMContentLoaded', () => {
    const settingsBtn = document.getElementById('settings-btn');
    const settingsPanel = document.getElementById('settings-panel');
    const translateBtn = document.getElementById('translate-btn');
    const inputText = document.getElementById('input-text');
    const outputText = document.getElementById('output-text');
    const loadingSpinner = document.getElementById('loading-spinner');

    // Inputs
    const apiKeyInput = document.getElementById('api-key');
    const baseUrlInput = document.getElementById('base-url');
    const modelInput = document.getElementById('model');
    const skipSslInput = document.getElementById('skip-ssl');
    const sourceLangSelect = document.getElementById('source-lang');
    const targetLangSelect = document.getElementById('target-lang');

    // Load saved settings
    apiKeyInput.value = localStorage.getItem('api_key') || '';
    baseUrlInput.value = localStorage.getItem('base_url') || '';
    modelInput.value = localStorage.getItem('model') || 'gpt-3.5-turbo';
    skipSslInput.checked = localStorage.getItem('skip_ssl') === 'true';

    // Toggle Settings
    settingsBtn.addEventListener('click', () => {
        settingsPanel.classList.toggle('hidden');
    });

    // Save settings on change
    [apiKeyInput, baseUrlInput, modelInput].forEach(input => {
        input.addEventListener('change', () => {
            localStorage.setItem(input.id.replace('-', '_'), input.value);
        });
    });
    skipSslInput.addEventListener('change', () => {
        localStorage.setItem('skip_ssl', skipSslInput.checked);
    });

    // Translate Function
    async function translate() {
        const text = inputText.value.trim();
        if (!text) return;

        const apiKey = apiKeyInput.value.trim();
        if (!apiKey) {
            alert('Please enter your API Key in settings.');
            settingsPanel.classList.remove('hidden');
            return;
        }

        // UI State: Loading
        outputText.textContent = '';
        loadingSpinner.classList.remove('hidden');
        translateBtn.disabled = true;

        try {
            const response = await fetch('/translate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    text: text,
                    source_lang: sourceLangSelect.value,
                    target_lang: targetLangSelect.value,
                    config: {
                        api_key: apiKey,
                        base_url: baseUrlInput.value.trim() || null,
                        model: modelInput.value.trim(),
                        skip_ssl_verify: skipSslInput.checked
                    }
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Translation failed');
            }

            const data = await response.json();
            outputText.textContent = data.translated_text;
            outputText.classList.remove('output-placeholder');

        } catch (error) {
            outputText.textContent = `Error: ${error.message}`;
            outputText.style.color = 'red';
        } finally {
            loadingSpinner.classList.add('hidden');
            translateBtn.disabled = false;
        }
    }

    translateBtn.addEventListener('click', translate);

    // Allow Ctrl+Enter to translate
    inputText.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'Enter') {
            translate();
        }
    });
});
