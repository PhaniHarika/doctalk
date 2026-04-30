# 📄 DocTalk — Chat with Any PDF using RAG

> Upload any PDF and ask questions in plain English. Powered by LangChain, Groq (LLaMA 3.3), HuggingFace Embeddings, and FAISS.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-latest-green?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.3-orange?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)

---

## 🚀 Live Demo
👉 **[Try DocTalk here](#)** ← add your Streamlit Cloud URL

---

## 📌 What is DocTalk?

DocTalk is a Retrieval-Augmented Generation (RAG) application that lets you upload one or more PDF files and have a conversation with them. Instead of reading through long documents, just ask your question and get an instant, accurate answer grounded in the document content.

**Use cases:**
- Chat with research papers
- Ask questions about textbooks or notes
- Summarize project reports
- Extract key information from legal or technical documents

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| LLM | Groq API (LLaMA 3.3 70B) |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` (local, free) |
| Vector Store | FAISS |
| Orchestration | LangChain |
| PDF Parsing | PyPDF |
| Environment | Python 3.11, venv |

---

## ⚙️ How It Works

```
PDF Upload → Text Extraction → Chunking (1000 chars, 200 overlap)
    → HuggingFace Embeddings → FAISS Vector Store
    → User Question → Semantic Search → Top 4 Chunks Retrieved
    → LangChain Prompt → Groq LLaMA 3.3 → Answer
```

1. **PDF Parsing** — PyPDF extracts raw text from uploaded files
2. **Chunking** — Text split into 1000-character chunks with 200-char overlap to preserve context
3. **Embeddings** — HuggingFace `all-MiniLM-L6-v2` converts chunks to semantic vectors locally
4. **Vector Store** — FAISS indexes all vectors for fast similarity search
5. **RAG Chain** — LangChain retrieves top 4 relevant chunks and passes them to Groq LLaMA 3.3 with a grounded prompt
6. **Response** — Model answers strictly based on document context

---

## 🖥️ Screenshots

> *(Add screenshots of your app here after deployment)*

---

## 📦 Installation & Setup

### 1. Clone the repo
```bash
git clone https://github.com/PhaniHarika/doctalk.git
cd doctalk
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your free Groq API key at: https://console.groq.com

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
doctalk/
├── app.py              # Streamlit UI
├── rag_engine.py       # RAG pipeline (embeddings, vector store, chain)
├── requirements.txt    # Dependencies
├── .env                # API keys (not committed)
├── .gitignore          # Ignores venv, .env, __pycache__
└── README.md           # This file
```

---

## 🔑 Key Design Decisions

- **Local embeddings over API** — HuggingFace `all-MiniLM-L6-v2` runs locally, avoiding API quota limits and latency
- **FAISS over cloud vector DB** — Lightweight, no setup, perfect for demo and single-user apps
- **Groq over OpenAI** — Free tier, faster inference, LLaMA 3.3 70B is highly capable
- **Chunk overlap of 200** — Prevents context loss at chunk boundaries during retrieval

---

## 🌱 Future Enhancements

- [ ] Add chat memory so follow-up questions work better
- [ ] Support DOCX and TXT files
- [ ] Show source page numbers with answers
- [ ] Add multi-user session support
- [ ] Deploy with Docker

---

## 👩‍💻 Author

**Phani Harika Soma**
- GitHub: [@PhaniHarika](https://github.com/PhaniHarika)
- LinkedIn: [phaniharikasoma](https://www.linkedin.com/in/phaniharikasoma)

---

## 📄 License

MIT License — feel free to use and build on this project.
