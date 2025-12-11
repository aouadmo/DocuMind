"""
Document processing module for handling PDF and TXT files.
"""
import os
from typing import Optional
from PyPDF2 import PdfReader
import streamlit as st


class DocumentProcessor:
    """Handles reading and processing of uploaded documents."""
    
    @staticmethod
    def extract_text_from_pdf(file) -> str:
        """
        Extract text content from a PDF file.
        
        Args:
            file: Uploaded PDF file object
            
        Returns:
            Extracted text as string
            
        Raises:
            Exception: If PDF reading fails
        """
        try:
            pdf_reader = PdfReader(file)
            text = ""
            
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            
            if not text.strip():
                raise Exception("No text could be extracted from the PDF")
            
            return text.strip()
            
        except Exception as e:
            raise Exception(f"Failed to read PDF: {str(e)}")
    
    @staticmethod
    def extract_text_from_txt(file) -> str:
        """
        Extract text content from a TXT file.
        
        Args:
            file: Uploaded TXT file object
            
        Returns:
            File content as string
            
        Raises:
            Exception: If file reading fails
        """
        try:
            # Try different encodings
            encodings = ['utf-8', 'latin-1', 'cp1252']
            
            for encoding in encodings:
                try:
                    file.seek(0)  # Reset file pointer
                    text = file.read().decode(encoding)
                    if text.strip():
                        return text.strip()
                except UnicodeDecodeError:
                    continue
            
            raise Exception("Could not decode text file with supported encodings")
            
        except Exception as e:
            raise Exception(f"Failed to read TXT file: {str(e)}")
    
    @staticmethod
    def process_file(file) -> str:
        """
        Process uploaded file and extract text content.
        
        Args:
            file: Uploaded file object from Streamlit
            
        Returns:
            Extracted text content
            
        Raises:
            Exception: If file processing fails
        """
        file_ext = os.path.splitext(file.name)[1].lower()
        
        if file_ext == '.pdf':
            return DocumentProcessor.extract_text_from_pdf(file)
        elif file_ext == '.txt':
            return DocumentProcessor.extract_text_from_txt(file)
        else:
            raise Exception(f"Unsupported file type: {file_ext}")

