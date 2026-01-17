# 🦙 Local AI Chatbot (Ollama + Llama 3)

<div align="center">
  <img src="https://media.giphy.com/media/L1R1TVThqcebetFv8u/giphy.gif" width="200" alt="AI Chatbot GIF" />
  <h2>Your Personal, Private, and Offline AI Assistant</h2>

  <p>
    <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
    <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" />
    <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  </p>
</div>

---

## 🧐 About The Project

This is a **privacy-first AI Chatbot** that runs entirely on your local machine. It uses **Ollama** to run the powerful **Meta Llama 3** model, ensuring that your data never leaves your device.

**No internet connection is required after setup!**

### Why use this?

* 🔒 **100% Privacy** – Your chats stay on your laptop
* ✈️ **Offline Capable** – Works without Wi‑Fi
* ⚡ **Zero Latency** – No waiting for cloud APIs
* 💸 **Free** – No token or subscription cost

---

## 🛠️ Tech Stack

| Component    | Technology                   |
| ------------ | ---------------------------- |
| Frontend     | Streamlit (Python)           |
| Model Runner | Ollama (Local LLM Inference) |
| AI Model     | Meta Llama 3 (8B)            |
| Logic        | LangChain                    |

---

## ⚙️ Installation Guide

### 1️⃣ Install Ollama

Download and install Ollama from:

👉 [https://ollama.com/](https://ollama.com/)

Then pull the Llama 3 model:

```bash
ollama run llama3
```

---

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Local-Llama-Chatbot.git
cd Local-Llama-Chatbot
```

---

### 3️⃣ Install Dependencies

Create `requirements.txt`:

```txt
streamlit
langchain
langchain-community
```

Install them:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Option A: One‑Click (Windows)

Double‑click `run_llama.bat`

### Option B: Terminal

```bash
streamlit run start (local_llm).py
```

---

## 📸 Screenshots

```md

![Chatbot UI](https://github.com/abhisheksharma12891/Local-Llama-Chatbot/tree/main/assets/chatbot.png)

```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Push and open a Pull Request

Ideas:

* Chat with PDF (RAG)
* Voice Assistant Mode
* Memory Support

---

## 👨‍💻 Author

**Abhishek Kumar Sharma**
Aspiring AI Engineer & Full Stack Developer

---

<div align="center">
<b>Made with ❤️ using Llama 3 & Python 🐍</b>
</div>

Then pull the model:

```bash
ollama run llama3
