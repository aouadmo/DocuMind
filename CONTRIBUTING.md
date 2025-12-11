# 🤝 Contributing to DocuMind

Thank you for your interest in contributing to DocuMind! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)

---

## 📜 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- OpenAI API key
- Basic knowledge of Python and Streamlit

### Areas for Contribution
- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- 🧪 Tests
- 🌐 Translations

---

## 💻 Development Setup

1. **Fork the repository**
   - Click the "Fork" button on GitHub

2. **Clone your fork**
```bash
git clone https://github.com/YOUR_USERNAME/DocuMind.git
cd DocuMind
```

3. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

6. **Create a new branch**
```bash
git checkout -b feature/your-feature-name
```

---

## 🔧 Making Changes

### Branch Naming Convention
- `feature/` - New features
- `bugfix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Adding tests

Examples:
- `feature/add-excel-export`
- `bugfix/fix-pdf-parsing`
- `docs/update-readme`

### Commit Message Guidelines
Use clear, descriptive commit messages:

```
<type>: <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Example:
```
feat: Add Excel export functionality

- Added openpyxl dependency
- Implemented Excel export in app.py
- Updated UI with Excel download button

Closes #123
```

---

## 📤 Submitting Changes

1. **Test your changes**
```bash
streamlit run app.py
# Test all extraction modes with sample files
```

2. **Commit your changes**
```bash
git add .
git commit -m "feat: your feature description"
```

3. **Push to your fork**
```bash
git push origin feature/your-feature-name
```

4. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template
   - Submit!

### Pull Request Checklist
- [ ] Code follows the project's coding standards
- [ ] Changes have been tested locally
- [ ] Documentation has been updated (if needed)
- [ ] Commit messages are clear and descriptive
- [ ] No unnecessary files are included
- [ ] .env file is not committed

---

## 📏 Coding Standards

### Python Style Guide
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Example:
```python
def extract_data(text: str, extraction_type: str) -> Dict[str, Any]:
    """
    Extract structured data from text using AI.
    
    Args:
        text: The document text to analyze
        extraction_type: Type of extraction (Resume, Invoice, Sentiment)
        
    Returns:
        Dictionary containing extracted data
        
    Raises:
        ValueError: If extraction type is invalid
    """
    # Implementation
```

### File Organization
- Keep related code together
- Use clear file and module names
- Avoid circular dependencies
- Keep configuration separate

### UI/UX Guidelines
- Maintain consistent styling
- Provide clear user feedback
- Handle errors gracefully
- Keep the interface intuitive

---

## 🧪 Testing

Before submitting:
1. Test all three extraction modes
2. Test with different file types (PDF and TXT)
3. Test error handling (invalid files, missing API key)
4. Test on different browsers (if UI changes)

---

## 📝 Documentation

When adding features:
- Update README.md if needed
- Add docstrings to new functions
- Update DEPLOYMENT.md for deployment changes
- Add examples for new functionality

---

## 🐛 Reporting Bugs

Use GitHub Issues with:
- Clear title
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version)

---

## 💡 Suggesting Features

Use GitHub Issues with:
- Clear description of the feature
- Use case / motivation
- Possible implementation approach
- Examples (if applicable)

---

## ❓ Questions?

- Open a GitHub Issue
- Check existing issues and PRs
- Review the documentation

---

## 🙏 Thank You!

Your contributions make DocuMind better for everyone. We appreciate your time and effort!

