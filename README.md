Absolutely — the version I gave you is already fully Markdown-compatible! But just to be sure, here’s a clean version of the entire README as pure Markdown, ready to copy and paste into a file named README.md:

⸻



# Gemini Proxy Server 🔁✨

A FastAPI-powered proxy that forwards requests to the Gemini API (Google’s LLM), enriched with custom context like MapsIndoors data. Designed for easy integration with other systems like ChatThing or web frontends.

---

## 🚀 Features

- Stateless HTTP POST endpoint for querying Gemini
- Injects persistent context (e.g. from `mapsindoors.txt`)
- Designed to be deployed on **Cloud Run** with **CI/CD via Cloud Build**
- CORS-enabled for use from web clients
- Environment variable support for secure API key injection

---

## 📦 Project Structure

gemini-proxy/
├── main.py              # FastAPI app
├── mapsindoors.txt      # (Optional) Context injected into prompts
├── Dockerfile           # Container build file
├── requirements.txt     # Python dependencies
└── cloudbuild.yaml      # CI/CD pipeline config

---

## 🛠️ Requirements

- Python 3.10+
- Google Cloud CLI (`gcloud`)
- Google Cloud Project with Cloud Run + Cloud Build enabled
- A Gemini API key from Google AI Studio

---

## 🌐 How It Works

The proxy exposes a `/` POST endpoint:

### Request
```json
{
  "prompt": "What’s a good example of a flexible office layout?"
}

Response

{
  "content": "A flexible office layout might include..."
}

Optionally, static context is prepended to all prompts (e.g. MapsIndoors instructions or documentation).

⸻

🔐 Environment Variables

The proxy expects the following env variable:
	•	GEMINI_API_KEY: Your Gemini API key (set via .env, Secret Manager, or Cloud Run)

⸻

🚀 Deploy to Cloud Run

From your terminal:

gcloud run deploy gemini-proxy \
  --source . \
  --region us-central1 \
  --allow-unauthenticated

Or use CI/CD by pushing to GitHub — see cloudbuild.yaml.

⸻

🧪 Local Testing

pip install -r requirements.txt
uvicorn main:app --reload

Then POST to:

http://localhost:8000/



⸻

🔄 CI/CD with Cloud Build
	•	On each push to main, your code is built and deployed automatically to Cloud Run.
	•	Configured using cloudbuild.yaml
	•	Revisions can be managed in the Cloud Run console

⸻

🔐 Optional: Secure with Secret Manager

Replace direct os.environ loading with a call to Google’s Secret Manager API for improved security in production environments.

⸻

📄 License

MIT — free to use, extend, and remix.

---

✅ Paste this into a file named `README.md`, save, and push to GitHub:
```bash
git add README.md
git commit -m "Add clean markdown README"
git push

