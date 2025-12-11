# 📄 DocuMind: Universal AI Document Extraction & Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A powerful web-based dashboard that leverages AI to automatically extract structured data from unstructured documents. Upload a PDF or text file, select an extraction mode, and get clean, structured data in seconds.

## 🌟 Features

- **📝 Resume Parsing**: Extract candidate information, skills, experience, and education
- **🧾 Invoice Processing**: Extract invoice numbers, amounts, dates, and vendor details
- **💭 Sentiment Analysis**: Analyze text sentiment, tone, and key themes
- **📊 Multiple Export Formats**: Download results as JSON or CSV
- **🎨 Beautiful UI**: Clean, intuitive interface built with Streamlit
- **⚡ Fast Processing**: Powered by OpenAI's GPT models

## 🎯 Use Cases

- **HR & Recruitment**: Automatically parse resumes to extract candidate information
- **Finance & Accounting**: Extract data from invoices for automated bookkeeping
- **Marketing & Customer Service**: Analyze customer reviews and feedback sentiment
- **Data Processing**: Convert unstructured documents into structured databases

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/aouadmo/DocuMind.git
cd DocuMind
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
Navigate to `http://localhost:8501`

## 📖 How to Use

1. **Select Extraction Mode**: Choose from Resume Parsing, Invoice Data, or Sentiment Analysis
2. **Upload Document**: Upload a PDF or TXT file (max 10MB)
3. **Analyze**: Click the "Analyze Document" button
4. **View Results**: See extracted data in table or JSON format
5. **Download**: Export results as CSV or JSON

## 🏗️ Project Structure

```
DocuMind/
├── app.py                  # Main Streamlit application
├── extractor.py            # AI extraction engine
├── document_processor.py   # PDF/TXT file processing
├── config.py              # Configuration management
├── utils.py               # Utility functions
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Engine**: OpenAI GPT-3.5/GPT-4
- **PDF Processing**: PyPDF2
- **Data Handling**: Pandas
- **Language**: Python 3.9+

## 📊 Extraction Schemas

### Resume Parsing
Extracts: Name, Email, Phone, Total Years Experience, Top Skills, Education, Current Role

### Invoice Data
Extracts: Invoice Number, Date, Total Amount, Vendor Name, Customer Name, Due Date, Items Count

### Sentiment Analysis
Extracts: Sentiment Score (0-10), Sentiment Label, Main Theme, Tone, Key Phrases

## 🔒 Security & Privacy

- API keys are stored in environment variables (never committed to git)
- Uploaded files are processed in memory (not stored on disk)
- All data processing happens in real-time

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Add your `OPENAI_API_KEY` in Secrets management
5. Deploy!

### Deploy to Other Platforms

- **Heroku**: Use the included `requirements.txt`
- **AWS/GCP/Azure**: Deploy as a containerized application
- **Docker**: Create a Dockerfile with Python and Streamlit

## 📝 Configuration

Edit `config.py` to customize:
- Maximum file size
- Allowed file extensions
- OpenAI model selection
- Extraction schemas

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Aouad Mohamed**
- GitHub: [@aouadmo](https://github.com/aouadmo)

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- Streamlit for the amazing web framework
- The open-source community

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ for the Upwork community**

