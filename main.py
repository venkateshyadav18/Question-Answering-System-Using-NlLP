from flask import Flask, request, render_template, jsonify
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import os

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')

document_chunks = []
faiss_index = None
chunk_embeddings = None

def split_text_into_chunks(text, chunk_size=512):
    sentences = text.split('\n')
    chunks = []
    current_chunk = []
    for sentence in sentences:
        if len(' '.join(current_chunk + [sentence])) > chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
        else:
            current_chunk.append(sentence)
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

def build_faiss_index(chunks):
    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype('float32')
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index, embeddings

def retrieve_answer(question, index, embeddings, chunks):
    q_emb = model.encode([question])
    q_emb = np.array(q_emb).astype('float32')
    _, indices = index.search(q_emb, k=1)
    return chunks[indices[0][0]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global document_chunks, faiss_index, chunk_embeddings
    file = request.files['file']
    text = file.read().decode('utf-8')
    document_chunks = split_text_into_chunks(text)
    faiss_index, chunk_embeddings = build_faiss_index(document_chunks)
    return render_template('index.html', message='✅ Document uploaded and indexed!')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    if faiss_index is None:
        return jsonify({'answer': 'Please upload a document first.'})
    answer = retrieve_answer(question, faiss_index, chunk_embeddings, document_chunks)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
