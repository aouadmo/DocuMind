# 🚀 Deployment Guide for DocuMind

This guide covers multiple deployment options for the DocuMind application.

## 📋 Table of Contents
- [Streamlit Cloud (Recommended)](#streamlit-cloud)
- [Docker Deployment](#docker-deployment)
- [Heroku Deployment](#heroku-deployment)
- [Local Development](#local-development)

---

## 🌐 Streamlit Cloud (Recommended)

Streamlit Cloud offers free hosting for Streamlit apps with easy GitHub integration.

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at [share.streamlit.io](https://share.streamlit.io))
- OpenAI API key

### Steps

1. **Push your code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Go to Streamlit Cloud**
- Visit [share.streamlit.io](https://share.streamlit.io)
- Click "New app"
- Connect your GitHub account if not already connected

3. **Configure the app**
- Repository: `aouadmo/DocuMind`
- Branch: `main`
- Main file path: `app.py`

4. **Add Secrets**
- Click "Advanced settings"
- In the "Secrets" section, add:
```toml
OPENAI_API_KEY = "your-api-key-here"
```

5. **Deploy**
- Click "Deploy!"
- Wait for the app to build and deploy (usually 2-3 minutes)
- You'll get a public URL like: `https://your-app-name.streamlit.app`

### Updating the App
Any push to the main branch will automatically trigger a redeployment.

---

## 🐳 Docker Deployment

### Create Dockerfile

Create a file named `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run

```bash
# Build the image
docker build -t documind .

# Run the container
docker run -p 8501:8501 -e OPENAI_API_KEY=your-api-key documind
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'
services:
  documind:
    build: .
    ports:
      - "8501:8501"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    env_file:
      - .env
```

Run with:
```bash
docker-compose up
```

---

## 🟣 Heroku Deployment

### Prerequisites
- Heroku account
- Heroku CLI installed

### Setup Files

1. **Create `setup.sh`**:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

2. **Create `Procfile`**:
```
web: sh setup.sh && streamlit run app.py
```

### Deploy

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set OPENAI_API_KEY=your-api-key

# Deploy
git push heroku main

# Open app
heroku open
```

---

## 💻 Local Development

### Quick Start

```bash
# Clone repository
git clone https://github.com/aouadmo/DocuMind.git
cd DocuMind

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run the app
streamlit run app.py
```

### Development Tips

- The app will auto-reload when you save changes
- Access at `http://localhost:8501`
- Use `streamlit run app.py --server.port=8502` to run on a different port

---

## 🔒 Security Best Practices

1. **Never commit API keys** - Always use environment variables
2. **Use secrets management** - For production, use proper secrets management
3. **Enable HTTPS** - Most platforms provide this by default
4. **Rate limiting** - Consider implementing rate limiting for production
5. **Input validation** - Already implemented in the app

---

## 📊 Monitoring & Logs

### Streamlit Cloud
- View logs in the Streamlit Cloud dashboard
- Monitor app health and usage

### Docker
```bash
docker logs <container-id>
```

### Heroku
```bash
heroku logs --tail
```

---

## 🆘 Troubleshooting

### Common Issues

**Issue**: "OPENAI_API_KEY not found"
- **Solution**: Make sure you've set the environment variable correctly

**Issue**: "Module not found"
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: "Port already in use"
- **Solution**: Use a different port with `--server.port=8502`

**Issue**: PDF extraction fails
- **Solution**: Ensure the PDF is not password-protected or corrupted

---

## 📞 Support

For deployment issues, please open an issue on GitHub or contact the maintainer.

