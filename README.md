# 🤖 AI README Generator Agent

An LLM-powered documentation generator built using **FastAPI**, **LangChain**, and **Google Gemini**.

This system analyzes a full project folder, understands its structure, and automatically generates a professional `README.md` file ready for production use.

---

## 🚀 Problem Statement

Automatically generate structured project documentation from multi-file codebases using an LLM-based intelligent agent.

---

## 🧠 What This Project Does

- Traverses complete project folders
- Filters irrelevant directories (`venv`, `node_modules`, `.git`)
- Applies file-size and total-context safety limits
- Constructs a structured prompt for the LLM
- Uses Google Gemini to analyze architecture
- Generates a clean, production-ready `README.md`
- Provides auto-download functionality via frontend UI

---

## 🏗 Architecture

Frontend (HTML/CSS/JS)  
        ↓  
FastAPI Backend  
        ↓  
LangChain Prompt Orchestration  
        ↓  
Google Gemini (LLM)  
        ↓  
Generated README.md  

---

## 🛠 Tech Stack

- **Backend:** FastAPI  
- **LLM Framework:** LangChain  
- **Model:** Google Gemini (via Google AI Studio API)  
- **Frontend:** HTML, CSS, JavaScript  
- **Environment:** Python (venv)  

---

## 📂 Project Structure

```
.
├── app/
│   ├── __main__.py
│   ├── agents.py
│   ├── models.py
│   ├── config.py
│   └── tools.py
├── index.html
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User provides a project folder path.  
2. Backend traverses and reads project files.  
3. Applies filtering and size constraints.  
4. Constructs structured LLM prompt.  
5. Gemini analyzes project content.  
6. System returns a downloadable `README.md`.  

---

## ▶️ How To Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/chaitanyanaidug24-afk/ai-readme-generator-agent.git
cd ai-readme-generator-agent
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add your Google API key

Create a `.env` file in the root:

```
GOOGLE_API_KEY=your_api_key_here
```

### 5️⃣ Run backend

```bash
python -m uvicorn app.__main__:app --reload
```

### 6️⃣ Open frontend

Open `index.html` in your browser.

---

## 🛡 Safety Handling

- Ignores unnecessary folders  
- Skips large files  
- Applies total character limit to prevent token overflow  
- Structured prompt to ensure consistent README output  

---

## 🎯 Hackathon Context

Built as part of an AI-focused hackathon to demonstrate:

- LLM orchestration  
- Prompt engineering  
- Context management  
- AI-driven developer tooling  

---

## 🚀 Future Improvements

- Folder upload instead of path input  
- Multi-language support  
- File-wise summaries  
- Vector-based large project support  
- Multi-agent workflow  

---

## 👨‍💻 Author

**Chaitanya G**  
CSE Student | AI Systems Enthusiast  
GitHub: https://github.com/chaitanyanaidug24-afk
