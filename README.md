
# 🔍 Closed-Domain Question Answering System (Flask + FAISS + SBERT)

This project is a web-based **Question Answering (QA) system** that allows users to upload a `.txt` document and ask questions related to its content. It uses **semantic search** with Sentence-BERT and **FAISS** indexing to find the most relevant chunk of text that answers the user's question.

---

## 📦 Features

- ✅ Upload plain-text documents (`.txt`)
- 🔍 Ask natural language questions about the uploaded content
- 💡 Retrieves the most relevant passage using Sentence Embeddings and FAISS
- 🌐 Clean Bootstrap-powered interface

---

## 🧠 How It Works

1. **Text Chunking**: The uploaded text is split into manageable chunks based on sentence boundaries.
2. **Embedding Generation**: Each chunk is embedded using [SentenceTransformer (`all-MiniLM-L6-v2`)](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).
3. **Indexing**: FAISS (Facebook AI Similarity Search) is used to store and search embeddings.
4. **Question Answering**: User's question is embedded and the nearest chunk from the document is returned as the "answer".

---

## 🛠 Tech Stack

- **Flask** – Web framework
- **Sentence-Transformers** – Semantic embeddings
- **FAISS** – Fast similarity search
- **Bootstrap 5** – UI styling
- **HTML/JS** – User interaction

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo_url>
cd closed-domain-qa
```

### 2. Install Requirements

```bash
pip install flask faiss-cpu sentence-transformers numpy
```

### 3. Run the Application

```bash
python main.py
```

### 4. Access in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 Usage

1. Upload a `.txt` file (e.g., `doc.txt` about Chemistry).
2. Ask a natural language question, like:
   - “What does chemistry study?”
   - “What is matter theory?”
3. The system returns the closest matching passage from the uploaded document.

---

## 📁 Project Structure

```
closed-domain-qa/
│
├── main.py          # Flask backend with FAISS and SBERT
├── index.html       # Frontend page
├── doc.txt          # Sample document
```

---

## 📌 Example

**Uploaded Document (Excerpt):**

> "Chemistry is the study of the composition of matter and its transformation..."

**User Question:**

> "What is chemistry?"

**Answer Returned:**

> "Chemistry is the study of the composition of matter and its transformation..."

