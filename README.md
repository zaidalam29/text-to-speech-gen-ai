
# 🎙️ Dynamic Text-to-Speech AI Web App

**Created by:** Zaid Alam – Full Stack Engineer  
**Technology Stack:** Flask, OpenAI GPT-4o-mini, TTS-1, Bootstrap 5  

---

## 🔥 Overview

This web application allows users to convert **any text** into **speech** dynamically using AI. Users can:

- Input text of any type (general, poem, news, joke)  
- Select **content type** manually or let AI auto-detect  
- Choose **language** (English, Hindi, Urdu, Arabic, French)  
- Receive **processed text** rewritten by AI  
- Listen to **audio output** and download it as MP3  

This project demonstrates **Generative AI** for real-world applications: text transformation + speech generation.

---

## 🧠 LLM & AI Details

- **Language Model (LLM):** [OpenAI GPT-4o-mini](https://platform.openai.com/docs/models/gpt-4o-mini)  
  - Used for: Content classification and text rewriting  
  - Capable of: Poetic, formal news, joke, or general style text generation  
  - Supports multi-lingual output (English, Hindi, Urdu, Arabic, French)

- **Text-to-Speech Model:** [OpenAI TTS-1](https://platform.openai.com/docs/guides/text-to-speech)  
  - Converts processed text to audio  
  - Voice mapping based on content type:
    - General → Alloy  
    - Poem → Nova  
    - News → Onyx  
    - Joke → Shimmer  

- **Generative AI Perspective:**  
  - **Input → AI LLM → Processed Text → TTS → Audio**  
  - AI ensures contextually correct, style-aware, and language-specific output.  

---

## ⚙️ Features

1. **Auto Content Type Detection:** Let AI classify your text into general, poem, news, or joke  
2. **Manual Selection:** Optionally choose the type yourself  
3. **Multi-language Support:** Convert text to speech in multiple languages  
4. **Side-by-side UI:** Processed text and audio output appear together  
5. **Download Audio:** Save generated MP3 locally  
6. **Responsive Design:** Works on desktop and mobile  

---

## 🛠️ Installation & Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd flask_tts_app
```

2. **Create a Python virtual environment** (recommended)
```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate   # Linux / Mac
```

3. **Install dependencies**
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
# .env file in project root
OPENAI_API_KEY=your_openai_api_key_here
```

5. **Run the Flask app**
```bash
python app.py
```

6. **Open the app in browser**
```
http://127.0.0.1:5000
```

---

## 🖥️ Usage

1. Enter your text in the input box  
2. Select content type or choose "Auto Detect"  
3. Choose language  
4. Click **Generate Voice**  
5. View **processed text** and play audio  
6. Optionally click **Download MP3** to save audio locally  

---

## 📂 Folder Structure
```
flask_tts_app/
│
├── app.py             # Flask backend logic
├── templates/
│   └── index.html     # Frontend HTML + JS
├── static/
│   └── audio/         # Generated audio files
├── .env               # OpenAI API key
└── requirements.txt   # Dependencies
```

---

## 💡 Future Improvements

- Add **multiple voice accents per language**  
- Real-time **audio waveform visualization**  
- Support **longer texts with streaming TTS**  
- Deploy on **cloud / Docker** for scalable access  

---

## 📌 Credits

**Developed by:** Zaid Alam – Full Stack Engineer  
- Full-stack development with Flask, Python, Bootstrap  
- Generative AI integration (OpenAI GPT-4o-mini + TTS-1)  

---

## 📖 References

- [OpenAI GPT-4o-mini Documentation](https://platform.openai.com/docs/models/gpt-4o-mini)  
- [OpenAI Text-to-Speech Documentation](https://platform.openai.com/docs/guides/text-to-speech)  
- [Bootstrap 5 Grid System](https://getbootstrap.com/docs/5.3/layout/grid/)
