# ⚡ DocuMind Quick Start Guide

Get DocuMind up and running in 5 minutes!

## 🚀 Fastest Way to Start

### Option 1: Using Quick Start Scripts (Recommended)

**On macOS/Linux:**
```bash
./run.sh
```

**On Windows:**
```bash
run.bat
```

That's it! The script will:
- Create a virtual environment
- Install dependencies
- Check for .env file
- Launch the application

---

### Option 2: Manual Setup

**Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Set Up Environment**
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-key-here
```

**Step 3: Run the App**
```bash
streamlit run app.py
```

**Step 4: Open Browser**
Navigate to: `http://localhost:8501`

---

## 🎯 First Test

1. **Select Mode**: Choose "Resume Parsing" from the sidebar
2. **Upload File**: Upload `sample_files/sample_resume.txt`
3. **Analyze**: Click the "🔍 Analyze Document" button
4. **View Results**: See extracted data in the Table View tab
5. **Download**: Try downloading as JSON or CSV

---

## 🔑 Getting an OpenAI API Key

1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key and paste it in your `.env` file

**Note**: You'll need to add billing information to use the API.

---

## 📁 Test Files Included

Try these sample files to test each mode:

| File | Mode | Description |
|------|------|-------------|
| `sample_files/sample_resume.txt` | Resume Parsing | Software engineer resume |
| `sample_files/sample_invoice.txt` | Invoice Data | Technology services invoice |
| `sample_files/sample_review.txt` | Sentiment Analysis | Product review |

---

## 🐳 Docker Quick Start

**Build and Run:**
```bash
docker-compose up
```

**Or manually:**
```bash
docker build -t documind .
docker run -p 8501:8501 -e OPENAI_API_KEY=your-key documind
```

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. **Push to GitHub:**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy:**
- Go to [share.streamlit.io](https://share.streamlit.io)
- Click "New app"
- Select your repository
- Add `OPENAI_API_KEY` in Secrets
- Deploy!

---

## 🆘 Troubleshooting

### "OPENAI_API_KEY not found"
**Solution**: Make sure you created `.env` file and added your API key

### "Module not found"
**Solution**: Run `pip install -r requirements.txt`

### "Port already in use"
**Solution**: Run with different port:
```bash
streamlit run app.py --server.port=8502
```

### PDF extraction fails
**Solution**: Ensure PDF is not password-protected or scanned image

---

## 📚 Learn More

- **Full Documentation**: See [README.md](README.md)
- **Deployment Guide**: See [DEPLOYMENT.md](DEPLOYMENT.md)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)
- **Project Status**: See [PROJECT_STATUS.md](PROJECT_STATUS.md)

---

## 💡 Tips

- Start with the sample files to understand the output format
- Use clear, well-formatted documents for best results
- Check the sidebar for mode descriptions
- Download results in both JSON and CSV to see the difference
- Try different extraction modes with the same document

---

## 🎉 You're Ready!

DocuMind is now running. Upload a document and see the AI magic happen!

**Need help?** Open an issue on GitHub or check the documentation.

---

**Happy Extracting! 🚀**

