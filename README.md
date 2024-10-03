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

## Setup Instructions

1. Clone this repository:
    ```bash
    git clone https://github.com/your_username/your_repository.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your_repository
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create the necessary directories:
    ```bash
    mkdir uploads
    mkdir audio
    ```

5. Run the application:
    ```bash
    flask run
    ```

6. Access the app at `http://127.0.0.1:5000/`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to fork this repository, open issues, and submit pull requests!

## Author

Developed by [Your Name]. If you have any questions or feedback, feel free to contact me.

