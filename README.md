# ⚗️ Prompt Engineering Playground

An interactive Gradio app that helps you create, compare, and auto-optimize prompts using seven common prompt-engineering patterns. Build prompt variants, test them against sample input, and get a recommended optimized prompt.

**Key features**
- Generate 7 prompt variants (Zero-shot, Few-shot, Chain-of-Thought, Role-Based, Structured Output, Reverse Prompting, Socratic)
- Test each variant against a sample input using an LLM
- Side-by-side comparison and an auto-optimized recommendation
- Theme-aware, responsive UI (see `style.py`)

---

## Prerequisites
- Python 3.10+ recommended
- Windows (PowerShell) or other OS with Python installed
- A Hugging Face API token with inference access (set in `.env` as `HUGGINGFACE_API_TOKEN`)

## Quick Setup (Windows PowerShell)
Open PowerShell in the project folder `e:\prompt-playground` and run:

```powershell
# Create and activate venv (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the project root with your Hugging Face token:

```text
HUGGINGFACE_API_TOKEN=hf_xxxREPLACE_WITH_YOURSxxx
```

## Run the App
Start the Gradio app:

```powershell
python .\app.py
```

Gradio will print a local URL (usually `http://127.0.0.1:7860`) — open it in your browser.

---

## About the UI & Theme (`style.py`)
- The `CSS` export in `style.py` now includes:
  - CSS variables and `@media (prefers-color-scheme: ...)` blocks so the UI automatically adapts to the OS/browser light or dark theme.
  - Responsive base font sizes via media queries (mobile/tablet/desktop breakpoints).
  - A small JavaScript fallback that adds `.device-small` / `.device-medium` / `.device-large` classes to the `<html>` element and sets a `data-theme` attribute. This improves compatibility for browsers that need the JS hook.
- No changes are required in `app.py` — it already injects `CSS` via `gr.HTML(...)`.

### Optional: Add a manual theme toggle
If you want a UI switch to toggle light/dark manually, I can add a small button to the Gradio controls that calls `document.documentElement.setAttribute('data-theme', 'light'|'dark')` and optionally persist preference to `localStorage`.

---

## Notes & Troubleshooting
- If you get API errors, verify your `HUGGINGFACE_API_TOKEN` value and network connectivity.
- If the app does not appear, confirm the Python environment is activated and dependencies installed.
- The app uses the `InferenceClient` from `huggingface_hub` and the `chat_completion` method — check package versions in `requirements.txt` if behaviour differs.

## Development & Contribution
- Feel free to tweak colors and breakpoints in `style.py`.
- To change the model or inference settings, edit `client = InferenceClient(...)` and the `client.chat_completion(...)` call in `app.py`.

---

If you'd like, I can also:
- Add a manual theme toggle in the UI
- Add a `--share` option to `demo.launch()` for quick remote sharing
- Add a simple test harness that exercises `generate_variants()` with canned inputs

Enjoy — want me to add the manual theme toggle now?