import PyPDF2
from deep_translator import GoogleTranslator


def extract_text(pdf_path):
    """
    Extracts text from a PDF file.

    :param pdf_path: Path to the PDF file.
    :return: Extracted text from the PDF.
    """
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page in range(num_pages):
            text += reader.pages[page].extract_text() + "\n\n"
    return text


def translate_text_by_parts(text, target_lang='pt'):
    """
    Translates the extracted text into the specified language by parts due to translation service limits.

    :param text: Text to be translated.
    :param target_lang: Target language for translation (default: 'pt' for Portuguese).
    :return: Translated text.
    """
    char_limit = 4000
    translator = GoogleTranslator(source='auto', target=target_lang)
    text_parts = [text[i:i + char_limit] for i in range(0, len(text), char_limit)]
    translated_text = ""

    for part in text_parts:
        clean_part = part.strip()
        if len(clean_part) > 0 and len(clean_part) <= char_limit:
            try:
                translated_part = translator.translate(clean_part)
                translated_text += translated_part + "\n\n"
            except Exception as e:
                print(f"Error translating text part: {e}")
                translated_text += clean_part + "\n\n"  # Adds the original text in case of an error

    return translated_text


# Usage example
pdf_path = ""
extracted_text = extract_text(pdf_path)
translated_text = translate_text_by_parts(extracted_text)  # Translates to Portuguese
print(translated_text)
