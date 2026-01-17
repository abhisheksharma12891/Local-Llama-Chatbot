<!-- Project Header -->

<div align="center">
<img src="https://www.google.com/search?q=https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbm95bDN2aXo5bDN2aXo5bDN2aXo5bDN2aXo5bDN2aXo5bDN2aXo5JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/L1R1TVThqcebetFv8u/giphy.gif" width="200" alt="AI Chatbot GIF">

<h1>🦙 Local AI Chatbot (Ollama + Llama 3)</h1>

<p>
<b>Your Personal, Private, and Offline AI Assistant.</b>
</p>

<!-- Badges -->

<p>
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Python-3.11-blue%3Fstyle%3Dfor-the-badge%26logo%3Dpython%26logoColor%3Dwhite" alt="Python">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Streamlit-FF4B4B%3Fstyle%3Dfor-the-badge%26logo%3Dstreamlit%26logoColor%3Dwhite" alt="Streamlit">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/Ollama-000000%3Fstyle%3Dfor-the-badge%26logo%3Dollama%26logoColor%3Dwhite" alt="Ollama">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/LangChain-1C3C3C%3Fstyle%3Dfor-the-badge%26logo%3Dlangchain%26logoColor%3Dwhite" alt="LangChain">
</p>
</div>

🧐 About The Project

This is a privacy-first AI Chatbot that runs entirely on your local machine. It uses Ollama to run the powerful Meta Llama 3 model, ensuring that your data never leaves your device. No internet connection is required after setup!

Why use this?

🔒 100% Privacy: Your chats stay on your laptop.

✈️ Offline Capable: Works without Wi-Fi.

⚡ Zero Latency: No waiting for API responses from the cloud.

💸 Free: No subscription fees for tokens.

🛠️ Tech Stack

Component

Technology

Frontend

Streamlit (Python)

Model Runner

Ollama (Local LLM Inference)

AI Model

Meta Llama 3 (8B Parameters)

Logic/Chain

LangChain

⚙️ Installation Guide

Follow these simple steps to set up your own local AI.

1️⃣ Install Ollama

Download and install Ollama from the official website: https://ollama.com/

Once installed, open your terminal (cmd) and pull the Llama 3 model:

ollama run llama3


(This will download the model, approx 4.7 GB)

2️⃣ Clone the Repository

git clone [https://github.com/YOUR_USERNAME/Local-Llama-Chatbot.git](https://github.com/YOUR_USERNAME/Local-Llama-Chatbot.git)
cd Local-Llama-Chatbot


3️⃣ Install Dependencies

pip install -r requirements.txt


Note: Create a requirements.txt with: streamlit, langchain, langchain-community.

🚀 How to Run

You have two easy ways to launch your AI companion:

Option A: The "One-Click" Way (Windows) 🖱️

Double-click the run_llama.bat file included in this folder. It will automatically start the backend and open the chatbot in your browser.

Option B: The "Terminal" Way 💻

Open your terminal in the project folder and type:

streamlit run local_llm.py


📸 Screenshots

<!-- Upload your screenshots to an "assets" folder or imgur and link them here -->

<div align="center">
<img src="https://www.google.com/search?q=https://via.placeholder.com/800x400%3Ftext%3DChatbot%2BInterface%2BScreenshot" alt="Chatbot UI">
</div>

🤝 Contributing

Contributions are welcome! If you want to add features like "Chat with PDF" (RAG) or "Voice Mode", feel free to fork this repo and submit a PR.

Fork the Project

Create your Feature Branch

Commit your Changes

Push to the Branch

Open a Pull Request

👨‍💻 Author

Abhishek Kumar Sharma
Aspiring AI Engineer & Full Stack Developer

<div align="center">
<b>Made with ❤️ using Llama 3 & Python 🐍</b>
</div>
