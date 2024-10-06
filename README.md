# PDF/Document to Speech Converter

This project is a web-based application built with Flask that converts text from PDF, DOCX, and TXT files to speech using Google Text-to-Speech (gTTS). It also supports language detection and translation, allowing users to select their desired output language for the audio.

## Features

- **File Upload Support**: Upload PDF, DOCX, and TXT files.
- **Language Detection**: Automatically detects the language of the text.
- **Text Translation**: If the detected language is different from the selected output language, it translates the text.
- **Text-to-Speech (TTS)**: Converts the uploaded text to speech using gTTS.
- **Multiple Languages**: Supports multiple languages for text-to-speech conversion.
- **Downloadable MP3**: After the conversion, users can download the combined MP3 file.
- **Chunk-Based Processing**: Large texts are processed in chunks to ensure smooth conversion.
  
## Supported File Formats

- **PDF**
- **DOCX**
- **TXT**

## Supported Languages

The application supports the following languages for speech synthesis:

- **Afrikaans (af)**
- **Arabic (ar)**
- **Bengali (bn)**
- **Bosnian (bs)**
- **Catalan (ca)**
- **Czech (cs)**
- **Welsh (cy)**
- **Danish (da)**
- **German (de)**
- **Greek (el)**
- **English (en)**
- **Esperanto (eo)**
- **Spanish (es)**
- **Estonian (et)**
- **Finnish (fi)**
- **French (fr)**
- **Gujarati (gu)**
- **Hindi (hi)**
- **Croatian (hr)**
- **Hungarian (hu)**
- **Armenian (hy)**
- **Indonesian (id)**
- **Icelandic (is)**
- **Italian (it)**
- **Japanese (ja)**
- **Javanese (jw)**
- **Khmer (km)**
- **Kannada (kn)**
- **Korean (ko)**
- **Latin (la)**
- **Latvian (lv)**
- **Macedonian (mk)**
- **Malayalam (ml)**
- **Marathi (mr)**
- **Burmese (my)**
- **Nepali (ne)**
- **Dutch (nl)**
- **Norwegian (no)**
- **Polish (pl)**
- **Portuguese (pt)**
- **Romanian (ro)**
- **Russian (ru)**
- **Sinhala (si)**
- **Slovak (sk)**
- **Albanian (sq)**
- **Serbian (sr)**
- **Sundanese (su)**
- **Swedish (sv)**
- **Swahili (sw)**
- **Tamil (ta)**
- **Telugu (te)**
- **Thai (th)**
- **Filipino (tl)**
- **Turkish (tr)**
- **Ukrainian (uk)**
- **Urdu (ur)**
- **Vietnamese (vi)**
- **Chinese (zh-CN)**

## Technology Stack

- **Backend**: Flask, Python, gTTS, PyMuPDF (for PDF processing), python-docx (for DOCX processing)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Other Libraries**:
  - `pydub`: For audio manipulation and merging.
  - `concurrent.futures`: For multi-threaded text-to-speech processing.
  - `langdetect`: For detecting the language of the uploaded text.
  - `googletrans`: For translating text to the desired language.


## FFmpeg Installation

To enable audio manipulation in this project, FFmpeg is required. You can install FFmpeg using the following commands based on your operating system:

### Windows
1. Download FFmpeg from the official website: [FFmpeg Downloads](https://ffmpeg.org/download.html)
2. Add FFmpeg to your system's PATH environment variable.

### macOS
```bash
brew install ffmpeg
```
