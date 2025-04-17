# 🧠 End-to-End Medical Chatbot (RAG-based)

This repository is my follow-through project based on [Euron's YouTube tutorial](https://www.youtube.com/watch?v=SCZ0BZq-jqY). It implements a **Retrieval-Augmented Generation (RAG)** pipeline using **LangChain**, **Pinecone**, and **OpenAI**, enhanced with a Flask frontend for interaction.

---

## 📌 What I Did Differently

While the core idea was inspired by the video, I implemented this project using **the latest and modular versions** of the libraries which are significantly different from those in the video.

I've listed below the key differences of the libraries:

| Component        | Video Version         | My Implementation (April 2025)         |
|------------------|------------------------|-----------------------------------------|
| `langchain`      | ~0.0.x                 | `langchain==0.3.23`                     |
| `langchain-openai` | Not modularized       | `langchain-openai==0.3.13`              |
| `langchain-core` | N/A                    | `langchain-core==0.3.52`                |
| `langchain-community` | N/A              | `langchain-community==0.3.21`           |
| `pinecone-client`| Legacy                 | `pinecone-client[grpc]==3.0.0`          |
| `sentence-transformers` | Legacy         | `sentence-transformers==2.2.2`          |
| `pydantic`       | 1.x                    | `pydantic==2.11.3`                      |

> 📦 You can find all the extensive dependencies I used in [`requirements.txt`](./requirements.txt).

---

## 🔐 Environment Variables

This project uses a `.env` file to store secret credentials:

```
OPENAI_API_KEY=your-openai-api-key
PINECONE_API_KEY=your-pinecone-api-key
```

> 🛑 **Note**: The actual `.env` file is not included in this repository  since it would require me to disclose my own API Keys.

---

## 🧠 Skills I've Demonstrated and Acquired

By completing this project, I developed and practiced the following skills...

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs) via OpenAI API
- Prompt Engineering via `ChatPromptTemplate`
- Semantic Search using Vector Databases (Pinecone)
- Document Parsing and Text Splitting
- Embedding Creation (via HuggingFace)
- Flask App Creation (API + UI routing)
- Environment and Dependency Management
- Debugging versioning and compatibility issues

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/End-to-end-Medical-Chatbot.git
   cd End-to-end-Medical-Chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your `.env`:
   ```
   OPENAI_API_KEY=sk-...
   PINECONE_API_KEY=...
   ```

4. Populate the Pinecone index (only once):
   ```bash
   python store_index.py
   ```

5. Run the Flask app:
   ```bash
   python app.py
   ```

---

## ✨ Acknowledgements

- Thanks to [Euron's video](https://www.youtube.com/watch?v=SCZ0BZq-jqY) for the foundational walkthrough.
- HuggingFace, LangChain, Pinecone, and OpenAI for powerful, flexible APIs.
- ChatGPT for helping me figure out the latest versions and improving on this project.