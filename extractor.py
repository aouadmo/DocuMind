"""
AI-powered data extraction engine using OpenAI API.
"""
import json
from typing import Dict, Any
from openai import OpenAI
from config import Config


class DocumentExtractor:
    """Handles AI-powered document data extraction."""
    
    # Define extraction schemas and prompts
    EXTRACTION_SCHEMAS = {
        "Resume": {
            "system_prompt": "You are a professional resume parser. Extract structured data from resumes accurately.",
            "user_prompt": """Extract the following information from this resume and return ONLY valid JSON:
- Name (full name of the candidate)
- Email (email address)
- Phone (phone number if available)
- Total_Years_Experience (estimated total years, as a number)
- Top_Skills (array of top 3-5 skills)
- Education (highest degree)
- Current_Role (most recent job title)

Text: {text}

Return only valid JSON with these exact field names.""",
            "fields": ["Name", "Email", "Phone", "Total_Years_Experience", "Top_Skills", "Education", "Current_Role"]
        },
        
        "Invoice": {
            "system_prompt": "You are an invoice data extraction specialist. Extract structured data from invoices accurately.",
            "user_prompt": """Extract the following information from this invoice and return ONLY valid JSON:
- Invoice_Number (invoice ID or number)
- Date (invoice date)
- Total_Amount (total amount with currency)
- Vendor_Name (company/vendor name)
- Customer_Name (customer/client name if available)
- Due_Date (payment due date if available)
- Items_Count (number of line items, as a number)

Text: {text}

Return only valid JSON with these exact field names.""",
            "fields": ["Invoice_Number", "Date", "Total_Amount", "Vendor_Name", "Customer_Name", "Due_Date", "Items_Count"]
        },
        
        "Sentiment": {
            "system_prompt": "You are a sentiment analysis expert. Analyze text and provide structured insights.",
            "user_prompt": """Analyze this text for sentiment and return ONLY valid JSON:
- Sentiment_Score (0-10, where 0 is very negative, 5 is neutral, 10 is very positive)
- Sentiment_Label (one of: Very Negative, Negative, Neutral, Positive, Very Positive)
- Main_Theme (brief description of the main topic/theme)
- Tone (overall tone: Professional, Casual, Angry, Happy, Sad, etc.)
- Key_Phrases (array of 3-5 important phrases or keywords)

Text: {text}

Return only valid JSON with these exact field names.""",
            "fields": ["Sentiment_Score", "Sentiment_Label", "Main_Theme", "Tone", "Key_Phrases"]
        }
    }
    
    def __init__(self):
        """Initialize the extractor with OpenAI client."""
        Config.validate()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
    
    def extract_data(self, text: str, extraction_type: str) -> Dict[str, Any]:
        """
        Extract structured data from text using AI.
        
        Args:
            text: The document text to analyze
            extraction_type: Type of extraction (Resume, Invoice, Sentiment)
            
        Returns:
            Dictionary containing extracted data
            
        Raises:
            ValueError: If extraction type is invalid
            Exception: If API call fails
        """
        if extraction_type not in self.EXTRACTION_SCHEMAS:
            raise ValueError(f"Invalid extraction type: {extraction_type}")
        
        schema = self.EXTRACTION_SCHEMAS[extraction_type]
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": schema["system_prompt"]},
                    {"role": "user", "content": schema["user_prompt"].format(text=text)}
                ],
                temperature=0.3,  # Lower temperature for more consistent extraction
                max_tokens=1000
            )
            
            # Extract and parse JSON response
            content = response.choices[0].message.content.strip()
            
            # Try to extract JSON if wrapped in markdown code blocks
            if content.startswith("```"):
                content = content.split("```")[1]
                if content.startswith("json"):
                    content = content[4:]
                content = content.strip()
            
            data = json.loads(content)
            return data
            
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse AI response as JSON: {str(e)}")
        except Exception as e:
            raise Exception(f"Extraction failed: {str(e)}")

