# CV Evaluator - AI-Powered Resume Screening System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![LLaMA](https://img.shields.io/badge/LLaMA-3.1-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

### Language / Dil
**[English](#english)** | **[Türkçe](#turkish)**

---

## English

An intelligent AI-powered resume (CV) screening system that automatically evaluates uploaded resumes against customizable criteria, providing percentage-based match scores with optional weighting for HR recruitment and talent acquisition.

[Features](#features) • [Architecture](#architecture) • [Installation](#installation) • [Usage](#usage) • [Tech Stack](#tech-stack)

</div>

---

## 📋 Overview

CV Evaluator is an automated resume screening solution powered by LLaMA 3.1 language model, designed to streamline the recruitment process by intelligently analyzing resumes against user-defined criteria. The system uses advanced prompt engineering to evaluate candidate qualifications, experience, skills, and education, returning objective percentage-based match scores.

Unlike traditional keyword-matching ATS systems, CV Evaluator leverages large language model capabilities to understand context, synonyms, and implicit qualifications, providing more accurate and nuanced candidate assessments. The system supports weighted criteria, allowing recruiters to prioritize what matters most for each position.

## 🎯 Project Goals

The primary objectives of this AI recruitment tool are:

1. **Automated Screening**: Reduce manual CV review time by 80%+
2. **Objective Evaluation**: Eliminate unconscious bias through standardized scoring
3. **Customizable Criteria**: Adapt to any job role with flexible evaluation parameters
4. **Weighted Scoring**: Reflect the relative importance of different qualifications
5. **Scalability**: Process hundreds of CVs in minutes
6. **Transparency**: Provide explainable AI decisions for fair hiring practices

## ✨ Features

### 🤖 AI-Powered Analysis
- **LLaMA 3.1 Integration**: State-of-the-art language model for resume understanding
- **Context-Aware Evaluation**: Understands synonyms, implicit skills, and related experience
- **Multi-Format Support**: PDF, DOCX, and text-based resumes
- **Semantic Matching**: Goes beyond keyword matching to understand meaning
- **Structured Output**: Consistent JSON format with scores and reasoning

### 📊 Evaluation System
- **Custom Criteria**: Define unlimited evaluation parameters
- **Weighted Scoring**: Assign importance weights (1-10) to each criterion
- **Percentage Matching**: Clear 0-100% match score per resume
- **Batch Processing**: Evaluate multiple CVs simultaneously
- **Detailed Breakdown**: Score breakdown by criterion
- **Ranking System**: Automatic sorting from highest to lowest match

### 🎨 User Interface
- **Clean Web Interface**: Intuitive Flask-based UI
- **Drag & Drop Upload**: Easy CV file upload
- **Real-time Processing**: Instant evaluation results
- **Results Dashboard**: Visual presentation of scores
- **Export Functionality**: Download results as PDF/CSV
- **Responsive Design**: Works on desktop and tablet devices

### 📄 Document Processing
- **PDF Parsing**: Extract text from PDF resumes
- **DOCX Support**: Read Microsoft Word documents
- **Text Extraction**: Clean formatting and structure preservation
- **Multi-page Handling**: Process resumes of any length
- **Error Handling**: Graceful failures with informative messages

### 🔒 Privacy & Security
- **Local Processing**: All data stays on your server
- **No External API Calls**: Complete data privacy (when using local LLaMA)
- **Temporary Storage**: Uploaded files deleted after processing
- **Compliance Ready**: GDPR-compatible architecture
- **Audit Logs**: Track all evaluation activities

---

## 🏗️ Architecture

CV Evaluator follows a clean, modular architecture:

```
┌─────────────────────────────────────────────────────┐
│                 Web Interface (HTML/JS)              │
│            Upload CVs + Define Criteria              │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│              Flask Application (cv.py)               │
│        Routes, Request Handling, Response            │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│             Document Parser Module                   │
│         PDF/DOCX Extraction, Text Cleaning           │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│              Prompt Engineering Layer                │
│     System Prompt + Criteria → LLM-Ready Format     │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│            LLaMA 3.1 Language Model                  │
│         CV Analysis, Scoring, Reasoning              │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│              Score Calculation Module                │
│    Weighted Averaging, Ranking, Result Formatting    │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│              Results Presentation                    │
│   JSON Response → Web UI Display + Export Options   │
└──────────────────────────────────────────────────────┘
```

### Key Components

#### 1. **Flask Web Application**
```python
@app.route('/upload', methods=['POST'])
def upload_cv():
    # Handle file upload
    # Extract criteria and weights
    # Process CV
    # Return results
```

#### 2. **Document Parser**
```python
def extract_text_from_pdf(file_path):
    # Use PyPDF2 or pdfplumber
    # Extract clean text
    # Preserve structure
    
def extract_text_from_docx(file_path):
    # Use python-docx
    # Extract paragraphs
    # Clean formatting
```

#### 3. **Prompt Engineering**
```python
SYSTEM_PROMPT = """
You are an expert HR recruiter evaluating resumes.
Analyze the following CV against these criteria:
{criteria}

For each criterion, provide:
1. Score (0-100)
2. Brief justification
3. Key matching points

Output format: JSON
"""
```

#### 4. **LLaMA Integration**
```python
def evaluate_cv(cv_text, criteria, weights):
    prompt = construct_prompt(cv_text, criteria)
    response = llm.generate(prompt)
    scores = parse_llm_response(response)
    weighted_score = calculate_weighted_average(scores, weights)
    return weighted_score
```

#### 5. **Scoring Logic**
```python
def calculate_match_percentage(scores, weights):
    if not weights:
        return mean(scores)
    
    total_weight = sum(weights.values())
    weighted_sum = sum(
        scores[criterion] * weights[criterion] 
        for criterion in criteria
    )
    return (weighted_sum / total_weight)
```

---

## 🚀 Installation

### Prerequisites

- **Python 3.9+**
- **pip** package manager
- **LLaMA 3.1** model files (or access to LLaMA API)
- **4GB+ RAM** (8GB+ recommended for local LLaMA)
- **Modern web browser**

### Setup Steps

#### 1. **Clone the Repository**
```bash
git clone https://github.com/malisevdinoglu/CV-Evulator-in-LLM-.git
cd CV-Evulator-in-LLM-
```

#### 2. **Create Virtual Environment**
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate.bat
```

#### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

**Dependencies include:**
```txt
Flask==3.0.0
PyPDF2==3.0.1
python-docx==1.1.0
llama-cpp-python==0.2.20  # For local LLaMA
transformers==4.35.0  # Alternative LLM runtime
torch==2.1.0  # If using transformers
```

#### 4. **Download LLaMA 3.1 Model** (Local Setup)

**Option A: Using llama.cpp**
```bash
# Download model weights
wget https://huggingface.co/models/llama-3.1/resolve/main/model.gguf
mv model.gguf models/llama-3.1.gguf

# Configure in cv.py
MODEL_PATH = "models/llama-3.1.gguf"
```

**Option B: Using Ollama** (Recommended for ease)
```bash
# Install Ollama
curl https://ollama.ai/install.sh | sh

# Pull LLaMA 3.1
ollama pull llama3.1

# Runs automatically on localhost:11434
```

**Option C: Cloud API** (Alternative)
```python
# Use OpenAI-compatible API
# Configure API endpoint in cv.py
```

#### 5. **Configure Environment Variables** (Optional)
```bash
# Create .env file
echo "FLASK_SECRET_KEY=your-secret-key" > .env
echo "MODEL_PATH=models/llama-3.1.gguf" >> .env
echo "MAX_FILE_SIZE=10485760" >> .env  # 10MB
```

#### 6. **Run the Application**
```bash
python cv.py
```

**Expected Output:**
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
Model loaded successfully
Ready to accept requests
```

#### 7. **Open in Browser**
```
http://127.0.0.1:5000
```

---

## 📱 Usage

### Quick Start Guide

#### 1. **Access the Application**
- Navigate to `http://127.0.0.1:5000` in your browser
- You'll see the CV Evaluator interface

#### 2. **Upload Resumes**
```
Method 1: Drag & Drop
- Drag CV files into the upload area
- Multiple files supported

Method 2: Browse Files
- Click "Choose Files" button
- Select one or more PDF/DOCX files
- Maximum 10MB per file
```

#### 3. **Define Evaluation Criteria**
```
Example Criteria with Weights:

Criterion: Python programming experience
Weight: 10 (Highest priority)

Criterion: Machine learning knowledge
Weight: 8

Criterion: Bachelor's degree in Computer Science
Weight: 7

Criterion: 3+ years of professional experience
Weight: 6

Criterion: Communication skills
Weight: 5
```

**Weight Scale:**
- 10: Critical requirement
- 7-9: Very important
- 4-6: Important
- 1-3: Nice to have

#### 4. **Submit for Evaluation**
- Click "Evaluate CVs" button
- Processing time: 5-30 seconds per CV (depending on model)
- Progress indicator shows status

#### 5. **Review Results**
```json
Results Format:

{
  "candidate_name": "Jane Doe",
  "overall_match": 87,
  "breakdown": {
    "Python programming": 95,
    "Machine learning": 85,
    "Education": 90,
    "Experience": 80,
    "Communication": 85
  },
  "weighted_score": 87.3,
  "ranking": 1
}
```

#### 6. **Export Results**
```
Available Exports:

PDF Report:
- Formatted summary of all candidates
- Scores, rankings, and breakdowns
- Ready for sharing with hiring team

CSV File:
- Tabular data for analysis
- Import into Excel/Google Sheets
- Easy filtering and sorting

JSON Data:
- Raw evaluation data
- Integration with other systems
```

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Programming Language** | Python 3.9+ | Core application logic |
| **Web Framework** | Flask 3.0 | HTTP server, routing, templating |
| **AI/ML Model** | LLaMA 3.1 | Resume analysis and scoring |
| **PDF Processing** | PyPDF2 / pdfplumber | Extract text from PDFs |
| **DOCX Processing** | python-docx | Parse Word documents |
| **Model Runtime** | llama-cpp-python / Ollama | Run LLaMA locally |
| **Alternative Runtime** | transformers + PyTorch | Hugging Face integration |
| **Frontend** | HTML5, CSS3, JavaScript | User interface |
| **Logging** | Python logging module | Application logs |
| **Development IDE** | PyCharm | Development environment |

### Optional Enhancements
- **Database**: SQLite / PostgreSQL (for storing results)
- **Queue System**: Celery + Redis (for async processing)
- **Deployment**: Docker + Docker Compose
- **Monitoring**: Prometheus + Grafana
- **API**: FastAPI (for REST API endpoints)

---

## 📂 Project Structure

```
CV-Evaluator-in-LLM/
├── cv.py                       # Main Flask application
├── index.html                  # Web interface
├── requirements.txt            # Python dependencies
├── pyvenv.cfg                  # Virtual environment config
│
├── models/                     # LLM model files (gitignored)
│   └── llama-3.1.gguf
│
├── uploads/                    # Temporary CV storage (gitignored)
│   └── .gitkeep
│
├── results/                    # Evaluation results (gitignored)
│   └── .gitkeep
│
├── logs/
│   └── cv_analyzer.log        # Application logs
│
├── static/                    # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── app.js
│   └── images/
│
├── templates/                 # Flask templates (if using)
│   └── index.html
│
├── utils/                     # Helper modules
│   ├── __init__.py
│   ├── document_parser.py    # PDF/DOCX extraction
│   ├── llm_interface.py      # LLaMA interaction
│   ├── prompt_templates.py   # Prompt engineering
│   └── scoring.py            # Score calculation
│
├── tests/                    # Unit tests
│   ├── test_parser.py
│   ├── test_scoring.py
│   └── test_integration.py
│
├── .env.example              # Environment variables template
├── .gitignore
├── LICENSE
└── README.md                 # This file
```

---

## 🔧 Configuration

### Model Configuration

```python
# cv.py or config.py

# LLaMA Model Settings
MODEL_PATH = "models/llama-3.1.gguf"
MODEL_TEMPERATURE = 0.3  # Lower = more deterministic
MODEL_MAX_TOKENS = 2048
MODEL_CONTEXT_LENGTH = 4096

# Ollama Settings (Alternative)
OLLAMA_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.1"

# Processing Settings
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}
UPLOAD_FOLDER = 'uploads'
RESULTS_FOLDER = 'results'
```

### Prompt Template

```python
EVALUATION_PROMPT = """
You are an expert HR recruiter analyzing resumes for job fit.

RESUME CONTENT:
{cv_text}

EVALUATION CRITERIA:
{formatted_criteria}

INSTRUCTIONS:
1. Analyze how well the candidate matches each criterion
2. Provide a score from 0-100 for each criterion
3. Give brief justification for each score
4. Be objective and evidence-based

OUTPUT FORMAT (JSON):
{
  "candidate_name": "Extract from CV",
  "scores": {
    "criterion_1": score,
    "criterion_2": score,
    ...
  },
  "justifications": {
    "criterion_1": "brief reason",
    ...
  }
}
"""
```

---

## 🎯 Advanced Features

### Weighted Scoring Algorithm

```python
def calculate_weighted_score(scores, weights):
    """
    Calculate weighted average score
    
    Args:
        scores: Dict of criterion -> score (0-100)
        weights: Dict of criterion -> weight (1-10)
    
    Returns:
        Float: Weighted average (0-100)
    """
    if not weights:
        # Equal weights if not specified
        return sum(scores.values()) / len(scores)
    
    total_weighted_score = 0
    total_weight = 0
    
    for criterion, score in scores.items():
        weight = weights.get(criterion, 1)
        total_weighted_score += score * weight
        total_weight += weight
    
    return round(total_weighted_score / total_weight, 2)
```

### Batch Processing

```python
def process_multiple_cvs(cv_files, criteria, weights):
    """
    Process multiple CVs in batch
    """
    results = []
    
    for cv_file in cv_files:
        try:
            # Extract text
            cv_text = extract_text(cv_file)
            
            # Evaluate
            score = evaluate_cv(cv_text, criteria, weights)
            
            results.append({
                'filename': cv_file.filename,
                'score': score,
                'status': 'success'
            })
        except Exception as e:
            results.append({
                'filename': cv_file.filename,
                'error': str(e),
                'status': 'failed'
            })
    
    # Sort by score (descending)
    results.sort(key=lambda x: x.get('score', 0), reverse=True)
    
    return results
```

---

## 🐛 Troubleshooting

### Common Issues

**Problem**: Model fails to load
**Solution**:
```bash
# Check model file exists
ls -lh models/llama-3.1.gguf

# Verify model format compatibility
# Ensure llama-cpp-python version matches model

# Try Ollama instead
ollama pull llama3.1
# Update cv.py to use Ollama API
```

**Problem**: Out of memory error
**Solution**:
```python
# Reduce model context length
MODEL_CONTEXT_LENGTH = 2048  # Instead of 4096

# Use quantized model (smaller)
# Download GGUF Q4_K_M variant instead of full precision

# Process CVs one at a time instead of batch
```

**Problem**: PDF text extraction garbled
**Solution**:
```python
# Try alternative PDF library
# Replace PyPDF2 with pdfplumber

pip install pdfplumber

# Update extraction code
import pdfplumber
def extract_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return '\n'.join(page.extract_text() for page in pdf.pages)
```

**Problem**: Slow evaluation speed
**Solution**:
```python
# Use smaller, faster model
ollama pull llama3.1:8b  # Instead of 70b

# Reduce max tokens
MODEL_MAX_TOKENS = 1024

# Enable GPU acceleration
pip install llama-cpp-python --extra-index-url https://jllllll.github.io/llama-cpp-python-cuBLAS-wheels/AVX2/cu121

# Use async processing with Celery
```

**Problem**: Inconsistent scores
**Solution**:
```python
# Lower temperature for more deterministic output
MODEL_TEMPERATURE = 0.1  # Very consistent

# Improve prompt specificity
# Add scoring rubrics to prompt
# Use few-shot examples
```

---

## 🗺️ Roadmap

### Planned Features

- [ ] **PDF Report Export** with branded templates
- [ ] **CSV Export** for bulk analysis
- [ ] **Score Distribution** charts and analytics
- [ ] **Candidate Comparison** side-by-side view
- [ ] **Historical Data** tracking over time
- [ ] **API Integration** with job boards (LinkedIn, Indeed)
- [ ] **Email Integration** for automatic CV collection
- [ ] **Multi-language Support** (English, Turkish, etc.)
- [ ] **Custom Report Templates** with company branding
- [ ] **Interview Scheduling** integration
- [ ] **Skill Gap Analysis** vs. job requirements
- [ ] **Diversity Metrics** reporting (GDPR-compliant)
- [ ] **Batch Upload** via ZIP files
- [ ] **Real-time Collaboration** for hiring teams
- [ ] **Mobile App** (iOS & Android)

### Technical Improvements

- [ ] **Database Integration** (PostgreSQL)
- [ ] **Async Processing** with Celery
- [ ] **Docker Containerization**
- [ ] **Kubernetes Deployment** for scale
- [ ] **REST API** with FastAPI
- [ ] **GraphQL API** for flexible queries
- [ ] **Redis Caching** for faster responses
- [ ] **Automated Testing** (pytest, coverage >80%)
- [ ] **CI/CD Pipeline** (GitHub Actions)
- [ ] **Monitoring & Logging** (Prometheus, Grafana, ELK)
- [ ] **Rate Limiting** for API protection
- [ ] **Authentication** (OAuth2, JWT)
- [ ] **Role-Based Access Control** (RBAC)
- [ ] **Model Fine-Tuning** on HR datasets
- [ ] **A/B Testing Framework** for prompt optimization

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Erdem Maliş

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Ideas

- Improve prompt templates for better accuracy
- Add support for more document formats
- Create visualization dashboards
- Write comprehensive tests
- Add multi-language UI support
- Optimize model performance
- Enhance security features
- Document best practices

---

## 🙏 Acknowledgments

- **Meta AI**: For developing LLaMA 3.1 language model
- **Flask Community**: For the excellent web framework
- **Ollama Team**: For simplified LLM deployment
- **PyPDF2 & python-docx**: For document parsing capabilities
- **Open Source Community**: For tools and inspiration

---

## 📧 Contact

**Developer**: Erdem Maliş

- GitHub: [@malisevdinoglu](https://github.com/malisevdinoglu)
- LinkedIn: [Mehmet Ali Sevdinoglu](https://linkedin.com/in/erdem-malis)
- Email: [Contact via GitHub](https://github.com/malisevdinoglu)

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

Made with 💻 and ☕ by [Mehmet Ali Sevdinoglu](https://github.com/malisevdinoglu)

**AI-Powered Recruitment • LLaMA 3.1 • Flask**

</div>

---
---
---

<div id="turkish"></div>

# CV Değerlendirici - Yapay Zeka Destekli Özgeçmiş Eleme Sistemi

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![LLaMA](https://img.shields.io/badge/LLaMA-3.1-orange.svg)
![License](https://img.shields.io/badge/Lisans-MIT-yellow.svg)

**[English](#english)** | **[Türkçe](#turkish)**

Yüklenen özgeçmişleri özelleştirilebilir kriterlere göre otomatik olarak değerlendiren, İK alımı ve yetenek kazanımı için isteğe bağlı ağırlıklandırma ile yüzde tabanlı eşleşme puanları sağlayan akıllı yapay zeka destekli özgeçmiş eleme sistemi.

[Özellikler](#özellikler-tr) • [Mimari](#mimari-tr) • [Kurulum](#kurulum-tr) • [Kullanım](#kullanım-tr) • [Teknoloji Yığını](#teknoloji-yığını-tr)

</div>

---

## 📋 Genel Bakış {#özellikler-tr}

CV Değerlendirici, kullanıcı tanımlı kriterlere göre özgeçmişleri akıllıca analiz ederek işe alım sürecini kolaylaştırmak için tasarlanmış, LLaMA 3.1 dil modeli ile desteklenen otomatik bir özgeçmiş eleme çözümüdür. Sistem, aday niteliklerini, deneyimi, becerileri ve eğitimi değerlendirmek için gelişmiş prompt mühendisliği kullanır ve objektif yüzde tabanlı eşleşme puanları döndürür.

Geleneksel anahtar kelime eşleştirme ATS sistemlerinin aksine, CV Değerlendirici bağlamı, eş anlamlıları ve örtük nitelikleri anlamak için büyük dil modeli yeteneklerinden yararlanır ve daha doğru ve incelikli aday değerlendirmeleri sağlar. Sistem ağırlıklı kriterleri destekler ve işe alım uzmanlarının her pozisyon için en önemli olan şeye öncelik vermesine olanak tanır.

## 🎯 Proje Hedefleri

Bu yapay zeka işe alım aracının temel amaçları:

1. **Otomatik Eleme**: Manuel CV inceleme süresini %80+ azaltma
2. **Objektif Değerlendirme**: Standartlaştırılmış puanlama ile bilinçsiz önyargıyı ortadan kaldırma
3. **Özelleştirilebilir Kriterler**: Esnek değerlendirme parametreleri ile herhangi bir iş rolüne uyum
4. **Ağırlıklı Puanlama**: Farklı niteliklerin göreceli önemini yansıtma
5. **Ölçeklenebilirlik**: Dakikalar içinde yüzlerce CV işleme
6. **Şeffaflık**: Adil işe alım uygulamaları için açıklanabilir yapay zeka kararları sağlama

## ✨ Özellikler {#özellikler-tr}

### 🤖 Yapay Zeka Destekli Analiz
- **LLaMA 3.1 Entegrasyonu**: Özgeçmiş anlama için son teknoloji dil modeli
- **Bağlama Duyarlı Değerlendirme**: Eş anlamlıları, örtük becerileri ve ilgili deneyimi anlar
- **Çoklu Format Desteği**: PDF, DOCX ve metin tabanlı özgeçmişler
- **Semantik Eşleştirme**: Anlam anlamak için anahtar kelime eşleştirmenin ötesine geçer
- **Yapılandırılmış Çıktı**: Puanlar ve gerekçelerle tutarlı JSON formatı

### 📊 Değerlendirme Sistemi
- **Özel Kriterler**: Sınırsız değerlendirme parametresi tanımlama
- **Ağırlıklı Puanlama**: Her kritere önem ağırlıkları (1-10) atama
- **Yüzde Eşleştirme**: Özgeçmiş başına net 0-100% eşleşme puanı
- **Toplu İşleme**: Birden fazla CV'yi aynı anda değerlendirme
- **Detaylı Dökümü**: Kritere göre puan dağılımı
- **Sıralama Sistemi**: En yüksekten en düşüğe otomatik sıralama

### 🎨 Kullanıcı Arayüzü
- **Temiz Web Arayüzü**: Sezgisel Flask tabanlı UI
- **Sürükle Bırak Yükleme**: Kolay CV dosya yükleme
- **Gerçek Zamanlı İşleme**: Anında değerlendirme sonuçları
- **Sonuç Panosu**: Puanların görsel sunumu
- **Dışa Aktarma İşlevselliği**: Sonuçları PDF/CSV olarak indirme
- **Duyarlı Tasarım**: Masaüstü ve tablet cihazlarda çalışır

### 📄 Belge İşleme
- **PDF Ayrıştırma**: PDF özgeçmişlerden metin çıkarma
- **DOCX Desteği**: Microsoft Word belgelerini okuma
- **Metin Çıkarma**: Temiz formatlama ve yapı koruma
- **Çok Sayfa İşleme**: Herhangi bir uzunluktaki özgeçmişleri işleme
- **Hata İşleme**: Bilgilendirici mesajlarla zarif başarısızlıklar

### 🔒 Gizlilik ve Güvenlik
- **Yerel İşleme**: Tüm veriler sunucunuzda kalır
- **Harici API Çağrısı Yok**: Tam veri gizliliği (yerel LLaMA kullanırken)
- **Geçici Depolama**: Yüklenen dosyalar işlemden sonra silinir
- **Uyumluluk Hazır**: GDPR uyumlu mimari
- **Denetim Günlükleri**: Tüm değerlendirme faaliyetlerini izleme

---

## 🏗️ Mimari {#mimari-tr}

CV Değerlendirici temiz, modüler bir mimari izler:

```
┌─────────────────────────────────────────────────────┐
│             Web Arayüzü (HTML/JS)                    │
│            CV Yükle + Kriter Tanımla                 │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│          Flask Uygulaması (cv.py)                    │
│        Rotalar, İstek İşleme, Yanıt                  │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│          Belge Ayrıştırıcı Modülü                    │
│       PDF/DOCX Çıkarma, Metin Temizleme              │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│         Prompt Mühendisliği Katmanı                  │
│   Sistem Prompt + Kriterler → LLM Hazır Format      │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│          LLaMA 3.1 Dil Modeli                        │
│       CV Analizi, Puanlama, Gerekçelendirme          │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│         Puan Hesaplama Modülü                        │
│  Ağırlıklı Ortalama, Sıralama, Sonuç Formatlama     │
└────────────────────┬────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────┐
│           Sonuç Sunumu                               │
│  JSON Yanıt → Web UI Gösterim + Dışa Aktarma        │
└──────────────────────────────────────────────────────┘
```

---

## 🚀 Kurulum {#kurulum-tr}

### Ön Koşullar

- **Python 3.9+**
- **pip** paket yöneticisi
- **LLaMA 3.1** model dosyaları (veya LLaMA API erişimi)
- **4GB+ RAM** (yerel LLaMA için 8GB+ önerilir)
- **Modern web tarayıcı**

### Kurulum Adımları

#### 1. **Depoyu Klonlayın**
```bash
git clone https://github.com/malisevdinoglu/CV-Evulator-in-LLM-.git
cd CV-Evulator-in-LLM-
```

#### 2. **Sanal Ortam Oluşturun**
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows (Komut İstemi)
python -m venv venv
venv\Scripts\activate.bat
```

#### 3. **Bağımlılıkları Yükleyin**
```bash
pip install -r requirements.txt
```

**Bağımlılıklar şunları içerir:**
```txt
Flask==3.0.0
PyPDF2==3.0.1
python-docx==1.1.0
llama-cpp-python==0.2.20  # Yerel LLaMA için
transformers==4.35.0  # Alternatif LLM çalışma zamanı
torch==2.1.0  # transformers kullanıyorsanız
```

#### 4. **LLaMA 3.1 Modelini İndirin** (Yerel Kurulum)

**Seçenek A: llama.cpp Kullanarak**
```bash
# Model ağırlıklarını indir
wget https://huggingface.co/models/llama-3.1/resolve/main/model.gguf
mv model.gguf models/llama-3.1.gguf

# cv.py'de yapılandır
MODEL_PATH = "models/llama-3.1.gguf"
```

**Seçenek B: Ollama Kullanarak** (Kolaylık için önerilir)
```bash
# Ollama'yı yükle
curl https://ollama.ai/install.sh | sh

# LLaMA 3.1'i çek
ollama pull llama3.1

# localhost:11434'te otomatik çalışır
```

**Seçenek C: Bulut API** (Alternatif)
```python
# OpenAI uyumlu API kullan
# cv.py'de API endpoint'ini yapılandır
```

#### 5. **Ortam Değişkenlerini Yapılandırın** (İsteğe bağlı)
```bash
# .env dosyası oluştur
echo "FLASK_SECRET_KEY=sizin-gizli-anahtariniz" > .env
echo "MODEL_PATH=models/llama-3.1.gguf" >> .env
echo "MAX_FILE_SIZE=10485760" >> .env  # 10MB
```

#### 6. **Uygulamayı Çalıştırın**
```bash
python cv.py
```

**Beklenen Çıktı:**
```
 * http://127.0.0.1:5000 üzerinde çalışıyor
 * Debug modu: açık
Model başarıyla yüklendi
İstekleri kabul etmeye hazır
```

#### 7. **Tarayıcıda Açın**
```
http://127.0.0.1:5000
```

---

## 📱 Kullanım {#kullanım-tr}

### Hızlı Başlangıç Kılavuzu

#### 1. **Uygulamaya Erişin**
- Tarayıcınızda `http://127.0.0.1:5000` adresine gidin
- CV Değerlendirici arayüzünü göreceksiniz

#### 2. **Özgeçmişleri Yükleyin**
```
Yöntem 1: Sürükle Bırak
- CV dosyalarını yükleme alanına sürükleyin
- Birden fazla dosya desteklenir

Yöntem 2: Dosyalara Gözat
- "Dosya Seç" düğmesine tıklayın
- Bir veya daha fazla PDF/DOCX dosyası seçin
- Dosya başına maksimum 10MB
```

#### 3. **Değerlendirme Kriterlerini Tanımlayın**
```
Ağırlıklı Örnek Kriterler:

Kriter: Python programlama deneyimi
Ağırlık: 10 (En yüksek öncelik)

Kriter: Makine öğrenimi bilgisi
Ağırlık: 8

Kriter: Bilgisayar Mühendisliği lisans derecesi
Ağırlık: 7

Kriter: 3+ yıl profesyonel deneyim
Ağırlık: 6

Kriter: İletişim becerileri
Ağırlık: 5
```

**Ağırlık Ölçeği:**
- 10: Kritik gereksinim
- 7-9: Çok önemli
- 4-6: Önemli
- 1-3: Olması güzel

#### 4. **Değerlendirme İçin Gönder**
- "CV'leri Değerlendir" düğmesine tıklayın
- İşlem süresi: CV başına 5-30 saniye (modele bağlı)
- İlerleme göstergesi durumu gösterir

#### 5. **Sonuçları İnceleyin**
```json
Sonuç Formatı:

{
  "aday_adi": "Jane Doe",
  "genel_eslesme": 87,
  "dagilim": {
    "Python programlama": 95,
    "Makine öğrenimi": 85,
    "Eğitim": 90,
    "Deneyim": 80,
    "İletişim": 85
  },
  "agirlikli_puan": 87.3,
  "sira": 1
}
```

#### 6. **Sonuçları Dışa Aktarın**
```
Mevcut Dışa Aktarmalar:

PDF Raporu:
- Tüm adayların formatlanmış özeti
- Puanlar, sıralamalar ve dağılımlar
- İşe alım ekibiyle paylaşmaya hazır

CSV Dosyası:
- Analiz için tablo verileri
- Excel/Google Sheets'e aktar
- Kolay filtreleme ve sıralama

JSON Verisi:
- Ham değerlendirme verileri
- Diğer sistemlerle entegrasyon
```

---

## 🛠️ Teknoloji Yığını {#teknoloji-yığını-tr}

| Kategori | Teknoloji | Amaç |
|----------|-----------|------|
| **Programlama Dili** | Python 3.9+ | Temel uygulama mantığı |
| **Web Framework** | Flask 3.0 | HTTP sunucusu, yönlendirme, şablonlama |
| **AI/ML Modeli** | LLaMA 3.1 | Özgeçmiş analizi ve puanlama |
| **PDF İşleme** | PyPDF2 / pdfplumber | PDF'lerden metin çıkarma |
| **DOCX İşleme** | python-docx | Word belgelerini ayrıştırma |
| **Model Çalışma Zamanı** | llama-cpp-python / Ollama | LLaMA'yı yerel olarak çalıştırma |
| **Alternatif Çalışma Zamanı** | transformers + PyTorch | Hugging Face entegrasyonu |
| **Frontend** | HTML5, CSS3, JavaScript | Kullanıcı arayüzü |
| **Loglama** | Python logging modülü | Uygulama günlükleri |
| **Geliştirme IDE** | PyCharm | Geliştirme ortamı |

---

## 🐛 Sorun Giderme

### Yaygın Sorunlar

**Sorun**: Model yüklenemiyor
**Çözüm**:
```bash
# Model dosyasının var olduğunu kontrol et
ls -lh models/llama-3.1.gguf

# Model format uyumluluğunu doğrula
# llama-cpp-python versiyonunun modelle eşleştiğinden emin ol

# Bunun yerine Ollama dene
ollama pull llama3.1
# cv.py'yi Ollama API kullanacak şekilde güncelle
```

**Sorun**: Bellek yetersiz hatası
**Çözüm**:
```python
# Model bağlam uzunluğunu azalt
MODEL_CONTEXT_LENGTH = 2048  # 4096 yerine

# Quantize edilmiş model kullan (daha küçük)
# Tam hassasiyet yerine GGUF Q4_K_M varyantını indir

# Toplu yerine CV'leri tek tek işle
```

**Sorun**: PDF metin çıkarma bozuk
**Çözüm**:
```python
# Alternatif PDF kütüphanesi dene
# PyPDF2'yi pdfplumber ile değiştir

pip install pdfplumber

# Çıkarma kodunu güncelle
import pdfplumber
def extract_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return '\n'.join(page.extract_text() for page in pdf.pages)
```

**Sorun**: Yavaş değerlendirme hızı
**Çözüm**:
```python
# Daha küçük, daha hızlı model kullan
ollama pull llama3.1:8b  # 70b yerine

# Maksimum token'ları azalt
MODEL_MAX_TOKENS = 1024

# GPU hızlandırmayı etkinleştir
pip install llama-cpp-python --extra-index-url https://jllllll.github.io/llama-cpp-python-cuBLAS-wheels/AVX2/cu121

# Celery ile async işleme kullan
```

**Sorun**: Tutarsız puanlar
**Çözüm**:
```python
# Daha deterministik çıktı için sıcaklığı düşür
MODEL_TEMPERATURE = 0.1  # Çok tutarlı

# Prompt özgüllüğünü artır
# Prompt'a puanlama rubriklerini ekle
# Few-shot örnekleri kullan
```

---

## 🗺️ Yol Haritası

### Planlanan Özellikler

- [ ] Markalı şablonlarla **PDF Rapor Dışa Aktarma**
- [ ] Toplu analiz için **CSV Dışa Aktarma**
- [ ] **Puan Dağılımı** grafikleri ve analitikler
- [ ] **Aday Karşılaştırma** yan yana görünüm
- [ ] Zaman içinde **Geçmiş Veri** takibi
- [ ] İş panoları ile **API Entegrasyonu** (LinkedIn, Indeed)
- [ ] Otomatik CV toplama için **E-posta Entegrasyonu**
- [ ] **Çoklu Dil Desteği** (İngilizce, Türkçe vb.)
- [ ] Şirket markalaşması ile **Özel Rapor Şablonları**
- [ ] **Mülakat Zamanlama** entegrasyonu
- [ ] İş gereksinimleri vs. **Beceri Boşluk Analizi**
- [ ] **Çeşitlilik Metrikleri** raporlaması (GDPR uyumlu)
- [ ] ZIP dosyaları ile **Toplu Yükleme**
- [ ] İşe alım ekipleri için **Gerçek Zamanlı İşbirliği**
- [ ] **Mobil Uygulama** (iOS & Android)

### Teknik İyileştirmeler

- [ ] **Veritabanı Entegrasyonu** (PostgreSQL)
- [ ] Celery ile **Async İşleme**
- [ ] **Docker Konteynerizasyonu**
- [ ] Ölçek için **Kubernetes Dağıtımı**
- [ ] FastAPI ile **REST API**
- [ ] Esnek sorgular için **GraphQL API**
- [ ] Daha hızlı yanıtlar için **Redis Önbellekleme**
- [ ] **Otomatik Test** (pytest, kapsam >%80)
- [ ] **CI/CD Pipeline** (GitHub Actions)
- [ ] **İzleme ve Loglama** (Prometheus, Grafana, ELK)
- [ ] API koruması için **Hız Sınırlama**
- [ ] **Kimlik Doğrulama** (OAuth2, JWT)
- [ ] **Rol Tabanlı Erişim Kontrolü** (RBAC)
- [ ] İK veri setlerinde **Model Fine-Tuning**
- [ ] Prompt optimizasyonu için **A/B Test Framework'ü**

---

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

```
MIT Lisansı

Telif Hakkı (c) 2024 Erdem Maliş

İzin, bu yazılımın ve ilişkili dokümantasyon dosyalarının ("Yazılım") bir kopyasını 
alan herhangi bir kişiye, Yazılım'ı kullanma, kopyalama, değiştirme, birleştirme, 
yayınlama, dağıtma, alt lisanslama ve/veya satma hakları dahil olmak üzere, 
sınırlama olmaksızın Yazılım'da işlem yapma izni ücretsiz olarak verilir.
```

---

## 🤝 Katkıda Bulunma

Katkılar memnuniyetle karşılanır! Lütfen bu yönergeleri izleyin:

### Nasıl Katkıda Bulunulur

1. Depoyu fork edin
2. Özellik dalı oluşturun (`git checkout -b feature/HarikaBirOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika bir özellik ekle'`)
4. Dalınıza push edin (`git push origin feature/HarikaBirOzellik`)
5. Pull Request açın

### Katkı Fikirleri

- Daha iyi doğruluk için prompt şablonlarını iyileştir
- Daha fazla belge formatı için destek ekle
- Görselleştirme panoları oluştur
- Kapsamlı testler yaz
- Çoklu dil UI desteği ekle
- Model performansını optimize et
- Güvenlik özelliklerini geliştir
- En iyi uygulamaları belgele

---

## 🙏 Teşekkürler

- **Meta AI**: LLaMA 3.1 dil modelini geliştirdiği için
- **Flask Topluluğu**: Mükemmel web framework'ü için
- **Ollama Ekibi**: Basitleştirilmiş LLM dağıtımı için
- **PyPDF2 & python-docx**: Belge ayrıştırma yetenekleri için
- **Açık Kaynak Topluluğu**: Araçlar ve ilham için

---

## 📧 İletişim

**Geliştirici**: Mehmet Ali Sevdinoglu

- GitHub: [@malisevdinoglu](https://github.com/malisevdinoglu)
- LinkedIn: [Mehmet Ali Sevdinoglu](https://linkedin.com/in/erdem-malis)
- E-posta: [GitHub üzerinden iletişim](https://github.com/malisevdinoglu)

---

<div align="center">

**⭐ Bu projeyi yararlı buluyorsanız, lütfen yıldız vermeyi düşünün!**

💻 ve ☕ ile [Erdem Maliş](https://github.com/malisevdinoglu) tarafından yapılmıştır

**Yapay Zeka Destekli İşe Alım • LLaMA 3.1 • Flask**

</div>
