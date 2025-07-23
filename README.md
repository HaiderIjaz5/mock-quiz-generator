---
title: Mock Quiz Generator
emoji: 📉
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: 5.38.0
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# 🧠 Mock Quiz Generator from PDFs

Generate high-quality Multiple Choice Questions (MCQs) from any PDF-based study material using LLaMA 3, sentence-transformers, vector embeddings, and a clean Gradio UI. Ideal for educators, students, and content creators preparing for exams or quizzes!

[![Hugging Face Space](https://img.shields.io/badge/HuggingFace-Live%20Demo-blue?logo=huggingface)](https://huggingface.co/spaces/haiderijaz/mock-quiz-generator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🚀 Features

✅ Upload any educational PDF  
✅ Generate MCQs in seconds  
✅ Choose number of questions (max 50)  
✅ Export quiz as PDF or TXT  
✅ Clean Gradio UI with themes and layout  
✅ Uses sentence-transformers for semantic chunking  
✅ Vector DB-based RAG (Retrieval-Augmented Generation)  
✅ Powered by **Meta's LLaMA 3 (via Groq API)** for blazing-fast generation

---

## 🛠️ Tech Stack

- 🔍 **LLaMA 3 (8B)** via [Groq API](https://console.groq.com/)
- 🧠 `sentence-transformers` for intelligent chunking
- 🧭 FAISS Vector Database for retrieval
- 🎨 Gradio UI (Soft Theme)
- 🐍 Python, `pdfminer.six`, `reportlab`, `dotenv`

---

## 🖼️ UI Preview

![App Screenshot](<src="https://github.com/user-attachments/assets/5108cd1a-d1a0-4aae-a168-a5bd3851ffb7" />
)

---


## 💡 How It Works

1. 📄 **Upload PDF:** The tool extracts and chunks the text.
2. 🧠 **Embed & Store:** Each chunk is embedded and stored in FAISS DB.
3. 🔍 **Search Top Chunks:** Relevant chunks are retrieved using semantic similarity.
4. 🤖 **MCQ Generation:** Top content is passed to LLaMA 3 for MCQ generation.
5. 💾 **Download Options:** Get your quiz in PDF or TXT format.

---

## 🔧 Local Setup

```bash
git clone git@github.com:HaiderIjaz5/mock-quiz-generator.git
cd mock-quiz-generator
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Then run:

```bash
python app.py
```

---

## 🌐 Live Demo

➡️ **[Try the App on Hugging Face 🚀](https://huggingface.co/spaces/haiderijaz/mock-quiz-generator)**

---

## 🤝 Acknowledgements

Big thanks to:

- 🇵🇰 **PAK Angels** – [Generative AI Training Cohort 6](https://pakangels.com/)
- 👨‍🏫 **iCodeGuru**
- 🚀 **Aspire Pakistan**

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Connect with Me

**Haider Ijaz**  
📧 haiderijaz529@gmail.com  
🌐 [LinkedIn](https://www.linkedin.com/in/m-haider-ijaz/)  
🐙 [GitHub](https://github.com/HaiderIjaz5)
