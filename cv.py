import os
import json
from flask import Flask, render_template, request, jsonify, session
from PyPDF2 import PdfReader
from werkzeug.utils import secure_filename
import ollama

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Yeni System Prompt Konfigürasyonu
SYSTEM_PROMPT = """
You are a strict CV evaluation assistant. Your task is to:
1. Analyze the CV text thoroughly
2. Check for each criterion with maximum precision
3. Calculate suitability percentage based on matched criteria
4. Return ONLY the following format without ANY additional text:

[Name Surname from CV] - [Percentage]%
MATCHED_CRITERIA: [Comma-separated list of matched criteria]

RULES:
- Use only exact information from the CV
- Name format: "Firstname Lastname" from CV header
- If no name found, use filename without extension
- Percentage must be precise (0-100%)
- List ONLY matched criteria names (no weights)
- No explanations, comments or extra text
- Be strict in evaluation - only exact matches count
- English language only

Example output:
John Doe - 85%
MATCHED_CRITERIA: Python, Java, Project Management
"""

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        print(f"PDF okuma hatası: {e}")
    return text.lower()

def analyze_with_ollama(cv_text, criteria):
    try:
        # Sadece kriter metinlerini hazırla (ağırlıklar backend'de kullanılacak)
        criteria_texts = [criterion['text'] for criterion in criteria]
        
        response = ollama.generate(
            model='llama3.1',
            prompt=f"CV Text: {cv_text[:10000]}\n\nCriteria: {', '.join(criteria_texts)}",
            system=SYSTEM_PROMPT,
            options={
                'temperature': 0.1,  # Daha kesin sonuçlar için
                'num_ctx': 4000,
                'top_k': 40,
                'top_p': 0.9,
                'repeat_penalty': 1.1
            }
        )
        
        # Çıktıyı temizle ve formatı kontrol et
        cleaned_response = response['response'].strip()
        return cleaned_response
        
    except Exception as e:
        print("OLLAMA Error:", str(e))
        return f"{secure_filename('error')} - 0%\nMATCHED_CRITERIA: None"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'files' not in request.files:
        return jsonify({"error": "No files selected"}), 400
    
    try:
        criteria_data = json.loads(request.form.get('criteria', '[]'))
        criteria = []
        for item in criteria_data:
            if isinstance(item, dict):
                criteria.append({
                    "text": item.get("text", "").strip(),
                    "weight": int(item.get("weight", 1))
                })
            else:
                criteria.append({
                    "text": item.strip(),
                    "weight": 1
                })
        criteria = [c for c in criteria if c["text"]]
    except Exception as e:
        return jsonify({"error": f"Invalid criteria format: {str(e)}"}), 400
    
    files = request.files.getlist('files')
    results = []
    
    for file in files:
        if not file.filename.lower().endswith('.pdf'):
            continue
            
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        cv_text = extract_text_from_pdf(filepath)
        if not cv_text.strip():
            results.append({
                "filename": filename,
                "error": "Empty or unreadable file"
            })
            continue
            
        ollama_response = analyze_with_ollama(cv_text, criteria)
        
        # Çıktıyı parse et
        try:
            name_part, percentage_part = ollama_response.split('\n')[0].split(' - ')
            matched_part = ollama_response.split('\n')[1].replace('MATCHED_CRITERIA:', '').strip()
        except:
            name_part = filename.replace('.pdf', '')
            percentage_part = "0%"
            matched_part = "None"
        
        results.append({
            "filename": filename,
            "analysis": f"{name_part} - {percentage_part}\nMATCHED_CRITERIA: {matched_part}",
            "matched_criteria": matched_part.split(', ') if matched_part != "None" else []
        })
        
        os.remove(filepath)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)