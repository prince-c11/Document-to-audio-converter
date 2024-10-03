from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify
import os
import fitz  # PyMuPDF
from gtts import gTTS
from concurrent.futures import ThreadPoolExecutor
from pydub import AudioSegment
from langdetect import detect
from googletrans import Translator
from werkzeug.utils import secure_filename
from docx import Document

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['AUDIO_FOLDER'] = './audio'

# Allowed extensions
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx'}

# Language codes mapping
LANGUAGES = {
    'af': 'Afrikaans',
    'ar': 'Arabic',
    'bn': 'Bengali',
    'bs': 'Bosnian',
    'ca': 'Catalan',
    'cs': 'Czech',
    'cy': 'Welsh',
    'da': 'Danish',
    'de': 'German',
    'el': 'Greek',
    'en': 'English',
    'eo': 'Esperanto',
    'es': 'Spanish',
    'et': 'Estonian',
    'fi': 'Finnish',
    'fr': 'French',
    'gu': 'Gujarati',
    'hi': 'Hindi',
    'hr': 'Croatian',
    'hu': 'Hungarian',
    'hy': 'Armenian',
    'id': 'Indonesian',
    'is': 'Icelandic',
    'it': 'Italian',
    'ja': 'Japanese',
    'jw': 'Javanese',
    'km': 'Khmer',
    'kn': 'Kannada',
    'ko': 'Korean',
    'la': 'Latin',
    'lv': 'Latvian',
    'mk': 'Macedonian',
    'ml': 'Malayalam',
    'mr': 'Marathi',
    'my': 'Myanmar (Burmese)',
    'ne': 'Nepali',
    'nl': 'Dutch',
    'no': 'Norwegian',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ro': 'Romanian',
    'ru': 'Russian',
    'si': 'Sinhala',
    'sk': 'Slovak',
    'sq': 'Albanian',
    'sr': 'Serbian',
    'su': 'Sundanese',
    'sv': 'Swedish',
    'sw': 'Swahili',
    'ta': 'Tamil',
    'te': 'Telugu',
    'th': 'Thai',
    'tl': 'Filipino',
    'tr': 'Turkish',
    'uk': 'Ukrainian',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'zh-CN': 'Chinese'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def synthesize_speech(text, output_file, lang='en'):
    print(f"Synthesizing speech in {LANGUAGES.get(lang, 'Unknown')}...")
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    print(f"Speech synthesis completed in {LANGUAGES.get(lang, 'Unknown')}")
    return output_file

def combine_audio_files(output_files, combined_file):
    combined_audio = None
    for file in output_files:
        segment = AudioSegment.from_mp3(file)
        if combined_audio is None:
            combined_audio = segment
        else:
            combined_audio += segment
    combined_audio.export(combined_file, format="mp3")
    return combined_file

def convert_text_to_speech(text, output_folder, combined_file, lang='en', chunk_size=500):
    print(f"Converting text to speech in {LANGUAGES.get(lang, 'Unknown')}...")
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    output_files = [os.path.join(output_folder, f"chunk_{i}.mp3") for i in range(len(chunks))]
    translator = Translator()
    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = []
        for chunk, output_file in zip(chunks, output_files):
            detected_lang = detect(chunk)
            if detected_lang != lang:
                try:
                    translated_chunk = translator.translate(chunk, src=detected_lang, dest=lang).text
                except Exception as e:
                    print(f"Error translating chunk: {e}")
                    translated_chunk = chunk
            else:
                translated_chunk = chunk
            futures.append(executor.submit(synthesize_speech, translated_chunk, output_file, lang))
        for future in futures:
            print(f"Processed: {future.result()}")
    combine_audio_files(output_files, combined_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    lang = request.form.get('language', 'en')
    print(f"Selected language: {lang}")
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        if file_path.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            text = extract_text_from_docx(file_path)
        else:  # Assume it is a text file
            text = file.read().decode('utf-8')
        output_folder = app.config['AUDIO_FOLDER']
        os.makedirs(output_folder, exist_ok=True)
        combined_file = os.path.join(output_folder, "combined_output.mp3")
        convert_text_to_speech(text, output_folder, combined_file, lang)
        return redirect(url_for('result'))

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/download')
def download():
    audio_file = os.path.join(app.config['AUDIO_FOLDER'], 'combined_output.mp3')
    return send_file(audio_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
