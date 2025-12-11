#!/bin/bash

# Quick start script for DocuMind

echo "🚀 Starting DocuMind..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "📝 Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "⚠️  Please edit .env and add your OPENAI_API_KEY before running the app."
    echo ""
    read -p "Press Enter to continue or Ctrl+C to exit..."
fi

# Run the application
echo ""
echo "✨ Launching DocuMind..."
echo "🌐 The app will open in your browser at http://localhost:8501"
echo ""
streamlit run app.py

