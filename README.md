PDF Text Extractor and Translator
This Python script provides a seamless integration of two powerful functionalities: 
extracting text from PDF files and translating the extracted text into a specified language. 
Utilizing the PyPDF2 library, it first reads and extracts text from any given PDF file. 
The extracted text is then translated into the specified target language using the deep_translator library,
which employs GoogleTranslator for accurate and efficient translations. By default, the translation is set to Portuguese (pt), 
but this can be easily customized to any supported language by changing the target_lang parameter.

Features:
Text Extraction: Extracts all text from a PDF file, preserving the layout and spacing to maintain readability.
Language Translation: Translates the extracted text into the specified target language in chunks to comply with the Google Translator's character limit,
ensuring that large documents can be translated without issues.
How to Use:
Ensure PyPDF2 and deep_translator are installed in your environment.
Set the pdf_path variable to the path of your PDF file.
Call the extract_text(pdf_path) function to extract text from the PDF.
Use translate_text_by_parts(extracted_text, target_lang='your_language_code') to translate the text.
The translated text will be outputted or can be used as needed.
This script is ideal for quickly translating documents, manuals, books, and reports into different languages,
enhancing accessibility and understanding across language barriers.
