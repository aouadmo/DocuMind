@echo off
REM Quick start script for DocuMind (Windows)

echo 🚀 Starting DocuMind...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -q -r requirements.txt

REM Check for .env file
if not exist ".env" (
    echo ⚠️  Warning: .env file not found!
    echo 📝 Creating .env from template...
    copy .env.example .env
    echo.
    echo ⚠️  Please edit .env and add your OPENAI_API_KEY before running the app.
    echo.
    pause
)

REM Run the application
echo.
echo ✨ Launching DocuMind...
echo 🌐 The app will open in your browser at http://localhost:8501
echo.
streamlit run app.py

