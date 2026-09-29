# 🤖 GenAI Chatbot

A beginner-friendly Generative AI chatbot built with:

- **Python** — core language
- **Streamlit** — web UI framework
- **Google Gemini API** — AI model backend
- **google-genai** — official Google GenAI SDK
- **python-dotenv** — secure API key management

---

## 🚀 Complete Setup & Run Guide

### ✅ Prerequisites

Make sure the following are installed on your system:

| Tool | Check Command | Download |
|------|---------------|----------|
| Python 3.10+ | `python --version` | [python.org](https://www.python.org/downloads/) |
| Git | `git --version` | [git-scm.com](https://git-scm.com/) |
| pip | `pip --version` | Comes with Python |

---

### Step 1 — Clone or Download the Project

**Option A — Clone via Git:**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

**Option B — Download ZIP:**
- Download and extract the ZIP file
- Open the extracted `GenAI_Chatbot` folder in your terminal or VS Code

---

### Step 2 — Create a Virtual Environment

A virtual environment keeps your project dependencies isolated.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> You should see `(venv)` appear at the start of your terminal prompt — this means the virtual environment is active.

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `streamlit` — web UI
- `google-genai` — Gemini API SDK
- `python-dotenv` — loads `.env` variables

---

### Step 4 — Get Your Gemini API Key

1. Go to [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key

---

### Step 5 — Set Up Your `.env` File

In the project folder, create a file named `.env` (copy from `.env.example`):

**Windows:**
```bash
copy .env.example .env
```

**Mac / Linux:**
```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your actual API key:

```text
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE
```

> ⚠️ **Never share your `.env` file or upload it to GitHub. It is already listed in `.gitignore` to prevent accidental commits.**

---

### Step 6 — Run the Chatbot

```bash
streamlit run app.py
```

The app will automatically open in your default browser at:

```
http://localhost:8501
```

If it doesn't open automatically, copy and paste the URL into your browser.

---

### Step 7 — Use the Chatbot

- Type any message in the chat input at the bottom and press **Enter**
- The AI will respond using the Google Gemini model
- The full conversation history is kept during the session
- Use the **"Clear chat"** button in the sidebar to reset the conversation

---

## 📁 Project Structure

```
GenAI_Chatbot/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .env                 # Your API key (NOT uploaded to GitHub)
├── .env.example         # Template for the .env file
├── .gitignore           # Files excluded from Git
└── README.md            # This file
```

---

## ⚙️ How It Works

```
User types a message
        ↓
Streamlit Chat UI (app.py)
        ↓
Conversation history is built
        ↓
Google Gemini API is called
        ↓
Gemini Generative AI Model processes it
        ↓
AI response is displayed in the chat
```

---

## ✨ Features

- 💬 Real-time Generative AI responses
- 🧠 Full conversation history (context-aware)
- 🔒 Secure API key via `.env` file
- 🗑️ Clear chat button in the sidebar
- ⚡ Fast and lightweight Streamlit UI

---

## 🛠️ Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `GEMINI_API_KEY is missing` | `.env` file not found or key not set | Create `.env` and paste your API key |
| `404 NOT_FOUND` | Model name is outdated | Update model name in `app.py` |
| `429 RESOURCE_EXHAUSTED` | Free tier quota (20 req/day) exceeded | Wait 24 hours or enable billing at [aistudio.google.com](https://aistudio.google.com) |
| `ModuleNotFoundError` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `(venv)` not showing | Virtual environment not activated | Run `venv\Scripts\activate` (Windows) |

---

## 🔮 Suggested Next Upgrades

1. 📄 PDF Chatbot using RAG
2. 📊 Excel/CSV Data Analyst chatbot
3. 💾 Persistent chat history (database)
4. 🎙️ Voice input/output
5. ☁️ Deploy on Streamlit Cloud

---

## ⚠️ Important

The API key is **NOT** included in this project. You must create your own key at [Google AI Studio](https://aistudio.google.com/app/apikey) and place it in the `.env` file.
