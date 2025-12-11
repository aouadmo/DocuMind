# 📁 Sample Files

This directory contains sample files for testing the DocuMind application.

## Files Included

### 1. `sample_resume.txt`
A sample resume for testing the **Resume Parsing** mode.

**Contains:**
- Candidate name and contact information
- Work experience (8+ years)
- Education details
- Technical skills
- Certifications

**Expected Extraction:**
- Name: John Doe
- Email: john.doe@email.com
- Phone: +1 (555) 123-4567
- Total Years Experience: 8+
- Top Skills: Python, JavaScript, React, AWS, Docker
- Education: Bachelor of Science in Computer Science
- Current Role: Senior Software Engineer

---

### 2. `sample_invoice.txt`
A sample invoice for testing the **Invoice Data** mode.

**Contains:**
- Invoice number and dates
- Vendor and customer information
- Itemized services
- Payment details

**Expected Extraction:**
- Invoice Number: INV-2024-001234
- Date: December 1, 2024
- Total Amount: $38,517.50
- Vendor Name: ABC Technology Solutions Inc.
- Customer Name: XYZ Corporation
- Due Date: December 31, 2024

---

### 3. `sample_review.txt`
A sample product review for testing the **Sentiment Analysis** mode.

**Contains:**
- Positive product review
- Detailed feedback on various aspects
- Overall recommendation

**Expected Extraction:**
- Sentiment Score: 9-10 (Very Positive)
- Sentiment Label: Very Positive
- Main Theme: Product review for wireless headphones
- Tone: Enthusiastic, Happy, Professional
- Key Phrases: "absolutely amazing", "exceeded expectations", "worth every penny"

---

## How to Use

1. Launch the DocuMind application
2. Select the appropriate extraction mode
3. Upload one of these sample files
4. Click "Analyze Document"
5. Review the extracted data

## Creating Your Own Test Files

You can create your own test files following these guidelines:

### For Resumes:
- Include name, contact info, work history, skills, education
- Use clear section headers
- List years of experience
- Include specific skills and technologies

### For Invoices:
- Include invoice number and dates
- List vendor and customer names
- Show itemized charges
- Include total amount with currency

### For Sentiment Analysis:
- Use any text with clear sentiment (reviews, feedback, comments)
- Include emotional language
- Express clear opinions or feelings
- Can be positive, negative, or neutral

---

## File Formats Supported

- **TXT**: Plain text files (recommended for testing)
- **PDF**: PDF documents (ensure text is extractable, not scanned images)

---

## Tips for Best Results

1. **Clear formatting**: Well-structured documents produce better results
2. **Readable text**: Avoid handwritten or scanned documents
3. **Appropriate length**: 1-10 pages works best
4. **Relevant content**: Match the document type to the extraction mode

---

## Need Help?

If you encounter issues with these sample files or want to test with your own documents, please refer to the main README.md or open an issue on GitHub.

