# 🐞 AI Code Debugger

An AI-powered code debugging tool that analyzes code, detects issues, explains them, and provides corrected versions — built using **FastAPI, LangChain, and Gemini API** with a **Streamlit frontend**.

---

## 🚀 Features

* 🔍 Detects bugs (syntax, logic, performance, security)
* 🧠 Explains issues in simple terms
* ✅ Provides corrected code
* ⚡ Suggests improvements & best practices
* 🎨 Clean UI with tabs (Issues, Explanation, Fix, Improvements)
* 📥 Download fixed code
* 🌐 Supports multiple languages (Python, JavaScript, Java, Go, C++)

---

## 🏗️ Tech Stack

### Backend

* FastAPI
* LangChain (LCEL)
* Gemini API (`gemini-1.5-flash`)
* Pydantic

### Frontend

* Streamlit

### Others

* Python 3.10+
* Uvicorn
* python-dotenv

---

## 📁 Project Structure

```
ai-code-debugger/
│
├── backend/
│   ├── main.py
│   ├── chains/
│   │   └── debugger_chain.py
│   ├── prompts/
│   │   └── debugger_prompt.py
│   ├── models/
│   │   └── request_models.py
│   ├── app.py   # Streamlit frontend
│   ├── .env
│   └── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rushyendra28/AI-Code-Debugger.git 
cd ai-code-debugger/backend
```

---

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### 3️⃣ Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

### 4️⃣ Setup environment variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

## ▶️ Running the Application

### 🖥️ Start Backend (FastAPI)

```bash
uvicorn main:app --reload
```

Access API docs:

```
http://127.0.0.1:8000/docs
```

---

### 🎨 Start Frontend (Streamlit)

Open a new terminal:

```bash
streamlit run app.py
```

Access UI:

```
http://localhost:8501
```

---

## 🧪 Example Usage

### Input

```python
def add(a, b):
    return a - b
```

---

### Output

```json
{
  "issues": ["Incorrect operator used"],
  "explanation": "The function subtracts instead of adding",
  "fixed_code": "def add(a, b): return a + b",
  "improvements": ["Add type hints", "Add docstring"]
}
```

---

## 🧠 How It Works

1. User inputs code via Streamlit UI
2. Request is sent to FastAPI backend
3. LangChain processes the prompt
4. Gemini API analyzes the code
5. Structured JSON response is returned
6. UI displays results in organized tabs

---

## 🔥 Future Enhancements

* 🧩 Multi-mode support (Debug / Optimize / Explain)
* 💬 Chat-based debugging (memory support)
* 🌐 Deploy on cloud (Render / AWS / Vercel)
* 🧠 Codebase-level debugging (multi-file support)
* 🔐 Authentication system
* 🎨 Advanced UI (React frontend)

---

## 🐛 Known Issues

* LLM may occasionally return invalid JSON (handled with fallback)
* Large code inputs may increase response time

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Submit a PR

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* LangChain
* Google Gemini API
* Streamlit
* FastAPI

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!

---
