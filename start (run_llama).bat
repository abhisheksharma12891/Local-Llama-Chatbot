@echo off
title 🦙 Local Llama Chatbot Launcher
color 0A

echo ===================================================
echo 🚀 Starting Local AI Chatbot (Powered by Ollama)
echo ===================================================
echo.

:: Step 1: Check if Ollama is running
echo [1/2] Checking Ollama Service...
tasklist /FI "IMAGENAME eq ollama_app.exe" 2>NUL | find /I /N "ollama_app.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo    - Ollama is already running. Good!
) else (
    echo    - Starting Ollama... (Make sure you installed it)
    start "" "ollama" serve
    timeout /t 3 >nul
)

:: Step 2: Run the Streamlit App
echo [2/2] Launching Chatbot Interface...
echo.
echo ---------------------------------------------------
echo 💡 Press Ctrl+C to stop the chatbot.
echo ---------------------------------------------------
echo.

:: Using the specific Python path we found earlier to avoid errors
"C:\Users\abhis\AppData\Local\Programs\Python\Python311\python.exe" -m streamlit run local_llm.py

pause