from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os, io, tempfile, re

# Load environment
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
client = OpenAI()

# Utility function
def sanitize_filename(text, max_length=20):
    sanitized = re.sub(r'[^\w\s-]', '', text.lower())
    sanitized = re.sub(r'[-\s]+', '_', sanitized)
    return sanitized[:max_length]

def classify_content(input_text: str):
    """Classify the input text"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Classify the content as one of: 'general', 'poem', 'news', 'joke'."},
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message.content.strip().lower()

def process_text(input_text: str, content_type: str, language: str):
    """Process text based on type and language"""
    system_prompts = {
        "general": f"Rewrite the text in {language} language, keeping the meaning same.",
        "poem": f"Rewrite the following text as a short, beautiful poem in {language}:",
        "news": f"Rewrite the following text in a formal news anchor style in {language}:",
        "joke": f"Turn the following text into a short, funny joke in {language}:"
    }
    prompt = system_prompts.get(content_type, system_prompts["general"])

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message.content.strip()


def text_to_speech(processed_text: str, content_type: str):
    """Convert text to speech and return file path"""
    voice_map = {
        "general": "alloy",
        "poem": "nova",
        "news": "onyx",
        "joke": "shimmer"
    }
    voice = voice_map.get(content_type, "alloy")

    audio_data = io.BytesIO()
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice=voice,
        input=processed_text
    ) as response:
        for chunk in response.iter_bytes():
            audio_data.write(chunk)

    # Save audio file in static/audio
    os.makedirs("static/audio", exist_ok=True)
    file_name = f"{sanitize_filename(content_type)}_{sanitize_filename(processed_text)}.mp3"
    file_path = os.path.join("static/audio", file_name)
    with open(file_path, "wb") as f:
        f.write(audio_data.getvalue())

    return file_path

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    try:
        input_text = request.form.get("input_text")
        content_type = request.form.get("content_type")
        language = request.form.get("language")

        if content_type == "auto":
            content_type = classify_content(input_text)

        processed_text = process_text(input_text, content_type, language)
        audio_path = text_to_speech(processed_text, content_type)

        return jsonify({
            "language": language,
            "content_type": content_type,
            "processed_text": processed_text,
            "audio_url": "/" + audio_path
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
