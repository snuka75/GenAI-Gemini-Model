

# 🚀 GenAI-Gemini-Model

🔍 **AI-Powered Web Applications with Streamlit + Gemini Pro + Groq**

This project showcases a suite of intelligent and interactive web applications built using **Streamlit**, powered by **Google’s Gemini Pro**, **Gemma**, **Groq**, and **FAISS**. Each app demonstrates real-world capabilities of large language models (LLMs) across different modalities including text, documents, and images.

---

## 🧠 Applications Overview

### 💬 Gemini Q&A Chatbot
- Real-time conversational interface powered by **Gemini 2.0 Flash**.
- Maintains **chat history** and supports contextual question-answering.
- Ideal for dynamic, ongoing user interactions.

---

### 📄 PDF Q&A with Groq + Gemma + FAISS
- Upload any **PDF file** and query it in **natural language**.
- Uses **FAISS** for semantic vector search.
- Combines **Groq's ultra-fast inference** with **Gemma’s LLM** to deliver instant responses from document content.

---

### 🧠 Text-to-SQL Translator
- Convert **plain English questions** into SQL queries.
- Automatically builds and queries an **SQLite** database.
- Powered by Gemini’s language understanding capabilities to interpret user intent and generate accurate results.

---

### 🖼️ Vision-Based Q&A
- Upload an image and ask contextual questions.
- Uses **Gemini 1.5 Flash** to extract insights from images.
- Enables visual understanding and reasoning with optional text prompts.

---

## ⚙️ Tech Stack

| Technology       | Purpose                                           |
|------------------|---------------------------------------------------|
| Streamlit        | Interactive and lightweight web UI               |
| Gemini Pro/Flash | LLMs for text and vision tasks (by Google)       |
| Groq             | Ultra-fast inference runtime                     |
| Gemma            | Lightweight open-source language model           |
| FAISS (CPU)      | Vector search for semantic similarity            |
| SQLite           | Backend database for text-to-SQL application     |

---

## 🗂️ Project Structure (Example)

```
📁 genai-gemini-model/
├── app/
│   ├── chatbot_app.py
│   ├── pdf_qa_app.py
│   ├── text_to_sql_app.py
│   └── vision_qa_app.py
├── assets/
│   └── sample_images, pdfs, icons
├── utils/
│   └── faiss_utils.py, gemini_utils.py
├── README.md
└── requirements.txt
```

---

## 📦 Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/genai-gemini-model.git
cd genai-gemini-model
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Run the app**  
Choose an application to run (e.g., Chatbot):
```bash
streamlit run app/chatbot_app.py
```

---

## 🔐 API Keys & Configuration

Make sure to add your **Gemini**, **Groq**, or other model API keys in a `.env` file or as environment variables:
```
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key
```

---

## 📌 Roadmap

- ✅ Integrate Gemini for text and vision tasks
- ✅ Add semantic PDF search with FAISS
- ✅ Include Text-to-SQL app with auto SQLite schema
- ⏳ Add authentication and user session tracking
- ⏳ Dockerize for cloud deployment

---

## 💡 Inspiration

This project is inspired by the rapidly evolving GenAI ecosystem and aims to showcase practical, fast, and creative ways to integrate LLMs in daily data workflows.

---

## 📄 License

MIT License. See `LICENSE` file for more details.

---

## 🙌 Contributions

Contributions, feedback, and suggestions are welcome! Feel free to open an issue or submit a pull request.

---


