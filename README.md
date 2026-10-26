# PromptLab — Prompt Engineering Playground

A Streamlit app to generate, test, compare, and refine prompts using seven patterns. It uses Gemini through `google-genai`.

## Features
- Zero-shot, Few-shot, Chain-of-Thought-style, Role-Based, Structured Output, Reverse Prompting, and Socratic variants.
- Review and edit variants before testing.
- Run every selected prompt against the same sample input.
- Compare outputs side by side.
- Generate an optimized prompt recommendation.
- Download individual results, all comparisons, and the optimized prompt.

## Files
`app.py`, `prompts.py`, `style.py`, `.env`, `README.md`, `requirements.txt`

## Setup
Use Python 3.10+ and a Google AI Studio API key. Configure `.env`:
```dotenv
GOOGLE_API_KEY=your_google_ai_studio_api_key
GEMINI_MODEL=gemini-3.5-flash
```
Then run:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

## Calls and cost
Generating variants uses one model call, testing uses one call per selected pattern, and optimization uses one additional call. Selecting all seven patterns requires up to nine calls. Quotas and free-tier availability vary.

## Deploy
Push `app.py`, `prompts.py`, `style.py`, `requirements.txt`, and `README.md` to GitHub. Do not commit `.env`. In Streamlit Community Cloud secrets, set:
```toml
GOOGLE_API_KEY = "your_key"
GEMINI_MODEL = "gemini-3.5-flash"
```

## Evaluation notes
One sample is not a statistically reliable benchmark. Test multiple representative examples. Chain-of-Thought is implemented as careful task processing with a concise rationale or verifiable summary, not a request for hidden private reasoning. The optimized prompt is a model-generated recommendation, not a guaranteed optimum. Do not submit secrets, personal data, or confidential information.
