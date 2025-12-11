"""
Utility functions for DocuMind application.
"""
import os
from typing import Optional
from config import Config


def validate_file(file) -> tuple[bool, Optional[str]]:
    """
    Validate uploaded file.
    
    Args:
        file: Uploaded file object from Streamlit
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if file is None:
        return False, "No file uploaded"
    
    # Check file extension
    file_ext = os.path.splitext(file.name)[1].lower()
    if file_ext not in Config.ALLOWED_EXTENSIONS:
        return False, f"Invalid file type. Allowed types: {', '.join(Config.ALLOWED_EXTENSIONS)}"
    
    # Check file size
    file_size_mb = file.size / (1024 * 1024)
    if file_size_mb > Config.MAX_FILE_SIZE_MB:
        return False, f"File too large. Maximum size: {Config.MAX_FILE_SIZE_MB}MB"
    
    return True, None


def format_json_for_display(data: dict) -> dict:
    """
    Format extracted data for better display.
    
    Args:
        data: Raw extracted data dictionary
        
    Returns:
        Formatted dictionary
    """
    # Remove None values and empty strings
    return {k: v for k, v in data.items() if v is not None and v != ""}

