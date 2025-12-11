# 🏗️ DocuMind Architecture

## System Overview

DocuMind is a modular, AI-powered document extraction system built with Python and Streamlit.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│                      (Streamlit - app.py)                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ File Upload  │  │ Mode Select  │  │   Results    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Configuration (config.py)                │   │
│  │  • API Keys  • File Limits  • Extraction Modes       │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Utilities (utils.py)                     │   │
│  │  • File Validation  • Data Formatting                │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Processing Layer                          │
│                                                               │
│  ┌────────────────────────────────────────────────────┐     │
│  │      Document Processor (document_processor.py)    │     │
│  │                                                      │     │
│  │  ┌──────────────┐         ┌──────────────┐        │     │
│  │  │ PDF Reader   │         │ TXT Reader   │        │     │
│  │  │  (PyPDF2)    │         │  (Built-in)  │        │     │
│  │  └──────────────┘         └──────────────┘        │     │
│  │                                                      │     │
│  │  Output: Plain Text                                 │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      AI Layer                                │
│                                                               │
│  ┌────────────────────────────────────────────────────┐     │
│  │         AI Extractor (extractor.py)                │     │
│  │                                                      │     │
│  │  ┌──────────────────────────────────────────────┐  │     │
│  │  │         Extraction Schemas                   │  │     │
│  │  │  • Resume Schema                             │  │     │
│  │  │  • Invoice Schema                            │  │     │
│  │  │  • Sentiment Schema                          │  │     │
│  │  └──────────────────────────────────────────────┘  │     │
│  │                                                      │     │
│  │  ┌──────────────────────────────────────────────┐  │     │
│  │  │         OpenAI API Integration               │  │     │
│  │  │  • GPT-3.5-turbo / GPT-4                     │  │     │
│  │  │  • JSON Response Parsing                     │  │     │
│  │  └──────────────────────────────────────────────┘  │     │
│  │                                                      │     │
│  │  Output: Structured JSON                            │     │
│  └────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Output Layer                              │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Table View   │  │  JSON View   │  │   Downloads  │      │
│  │  (Pandas)    │  │   (Native)   │  │  (CSV/JSON)  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. User Interface Layer (`app.py`)
**Responsibility**: User interaction and display
- File upload interface
- Mode selection
- Results visualization
- Download functionality

**Technologies**: Streamlit, Pandas

### 2. Configuration Layer (`config.py`)
**Responsibility**: Centralized configuration management
- API key management
- File size limits
- Extraction mode definitions
- Application settings

**Technologies**: Python, python-dotenv

### 3. Utilities Layer (`utils.py`)
**Responsibility**: Helper functions
- File validation
- Data formatting
- Common utilities

**Technologies**: Python

### 4. Document Processing Layer (`document_processor.py`)
**Responsibility**: Extract text from various file formats
- PDF text extraction
- TXT file reading
- Encoding detection
- Error handling

**Technologies**: PyPDF2, Python built-in

### 5. AI Extraction Layer (`extractor.py`)
**Responsibility**: AI-powered data extraction
- Schema definitions for each mode
- OpenAI API integration
- JSON parsing and validation
- Error handling

**Technologies**: OpenAI API, Python

## Data Flow

```
User Upload → File Validation → Text Extraction → AI Processing → JSON Output → Display/Download
```

### Detailed Flow:

1. **User uploads file** (PDF or TXT)
2. **Validation** checks file type and size
3. **Document Processor** extracts plain text
4. **AI Extractor** sends text to OpenAI with schema
5. **OpenAI** returns structured JSON
6. **Parser** validates and formats JSON
7. **UI** displays results in multiple formats
8. **User** can download as JSON or CSV

## Extraction Schemas

### Resume Schema
```json
{
  "Name": "string",
  "Email": "string",
  "Phone": "string",
  "Total_Years_Experience": "number",
  "Top_Skills": ["array"],
  "Education": "string",
  "Current_Role": "string"
}
```

### Invoice Schema
```json
{
  "Invoice_Number": "string",
  "Date": "string",
  "Total_Amount": "string",
  "Vendor_Name": "string",
  "Customer_Name": "string",
  "Due_Date": "string",
  "Items_Count": "number"
}
```

### Sentiment Schema
```json
{
  "Sentiment_Score": "number (0-10)",
  "Sentiment_Label": "string",
  "Main_Theme": "string",
  "Tone": "string",
  "Key_Phrases": ["array"]
}
```

## Security Considerations

1. **API Key Protection**
   - Stored in environment variables
   - Never committed to version control
   - Validated on startup

2. **File Upload Security**
   - File type validation
   - File size limits
   - No permanent storage

3. **Data Privacy**
   - Files processed in memory
   - No data persistence
   - No logging of sensitive information

## Scalability Considerations

### Current Limitations:
- Single-user application
- Synchronous processing
- No caching
- No database

### Future Enhancements:
- Multi-user support with authentication
- Asynchronous processing with queues
- Redis caching for repeated documents
- Database for history and analytics
- API endpoints for programmatic access

## Deployment Architecture

### Local Development
```
Developer Machine → Python/Streamlit → OpenAI API
```

### Streamlit Cloud
```
GitHub → Streamlit Cloud → OpenAI API
```

### Docker
```
Docker Container → Streamlit App → OpenAI API
```

### Heroku
```
Git Push → Heroku Dyno → Streamlit App → OpenAI API
```

## Technology Stack Summary

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Frontend | Streamlit | Web UI |
| Backend | Python 3.9+ | Application logic |
| AI Engine | OpenAI API | Data extraction |
| PDF Processing | PyPDF2 | PDF text extraction |
| Data Handling | Pandas | Data manipulation |
| Configuration | python-dotenv | Environment management |
| Deployment | Docker/Heroku/Streamlit Cloud | Hosting |

## Performance Characteristics

- **Average Processing Time**: 3-10 seconds per document
- **File Size Limit**: 10MB
- **Supported Formats**: PDF, TXT
- **API Model**: GPT-3.5-turbo (configurable to GPT-4)
- **Concurrent Users**: Depends on deployment platform

## Error Handling Strategy

1. **File Level**: Validation before processing
2. **Processing Level**: Try-catch with user-friendly messages
3. **API Level**: Retry logic and error messages
4. **UI Level**: Clear feedback and recovery options

---

**Architecture Version**: 1.0.0
**Last Updated**: December 11, 2024

