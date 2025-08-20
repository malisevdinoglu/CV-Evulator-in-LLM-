# CV Evulator

AI-powered resume (CV) evaluator that scores uploaded resumes against user-defined criteria and returns a percentage-based match. Criteria can optionally be weighted to reflect importance, enabling flexible and consistent screening for HR and broader use cases.

---

## 🚀 Features
- Upload resumes (CVs) into the system
- Define evaluation criteria as input
- Optionally assign different weights to criteria
- Automatically calculate a percentage-based match score for each CV

## 🔮 Planned Features / Roadmap
- Export evaluation results as **PDF** reports
- Sort CVs by match score (highest → lowest)
- Integrations with external recruitment platforms
- Job-posting integrations for automated screening

---

## 🛠 Tech Stack
- **Language:** Python
- **Framework:** Flask
- **IDE:** PyCharm
- **Database:** None (current version uses uploaded files only)
- **AI Model:** LLaMA 3.1 (prompt-engineered via system prompt; **no fine-tuning**)

---

## ⚙️ Installation & Setup

> Requires Python 3.9+ (adjust if your environment differs)

1) **Clone the repository**
```bash
git clone https://github.com/yourusername/cv-evulator.git
cd cv-evulator
```

2) **(Optional) Create & activate virtual environment**
```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows (PowerShell)
python -m venv venv
venv\Scripts\Activate.ps1
```

3) **Install dependencies**
```bash
pip install -r requirements.txt
```

4) **Run the application**
```bash
python app.py
```

5) **Open in browser**
```
http://127.0.0.1:5000
```

---

## 🔧 Configuration
No additional configuration is required in the current version. The application runs locally after installing dependencies.

> If you later add a database or external APIs, introduce environment variables (e.g., via a `.env` file) and document them here.

---

## 🔍 Usage
1. **Upload CV** (PDF/DOCX)
2. **Enter criteria** and optionally **assign weights**
3. Click **“Evaluate”**
4. View the **percentage match score** for each CV

---

## 🤖 Model Details
- **Approach:** Prompt-engineering with a **system prompt** that specifies how to evaluate CVs and format answers (no model fine-tuning).
- **Model:** LLaMA 3.1 integrated locally on the developer’s machine.
- **Output format:** `Full Name – Match Percentage` (e.g., `Jane Doe – 82%`).
- **Scoring:** Percentage-based match derived from the criteria (with optional weights).
- **Notes:** Accuracy and consistency depend on prompt design, model version, and input quality.

> If you adopt a specific runtime (e.g., llama.cpp, vLLM, transformers), document it here with setup steps.

---

## 📸 Screenshots (Optional)
_Add screenshots or a short GIF demonstrating the upload → evaluate → results flow._

---

## 🤝 Contributing
Contributions are welcome! Please open an issue to discuss significant changes and submit a pull request with a clear description.

---

## 📅 License
Specify your license (e.g., MIT). Add a `LICENSE` file at the project root.

---

## 📫 Contact
- Author: Your Name
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

---

## ✨ Acknowledgements (Optional)
- LLaMA 3.1
- Flask community & Python ecosystem

