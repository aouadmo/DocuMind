"""
Configuration management for DocuMind application.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration."""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # File Upload Configuration
    MAX_FILE_SIZE_MB = 10
    ALLOWED_EXTENSIONS = ['.pdf', '.txt']
    
    # Extraction Modes
    EXTRACTION_MODES = {
        "Resume Parsing": "Resume",
        "Invoice Data": "Invoice",
        "Sentiment Analysis": "Sentiment"
    }
    
    # Application Settings
    APP_TITLE = "DocuMind: Universal AI Document Extraction & Analysis Dashboard"
    APP_DESCRIPTION = "Upload unstructured files to generate structured CSVs/JSON."
    
    @staticmethod
    def validate():
        """Validate required configuration."""
        if not Config.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found. Please set it in your .env file."
            )
        return True

