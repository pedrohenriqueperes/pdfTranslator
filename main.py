import PyPDF2
from deep_translator import GoogleTranslator

def extrair_texto(pdf_path):
    texto = ""
    with open(pdf_path, "rb") as file:
        leitor = PyPDF2.PdfReader(file)
        num_paginas = len(leitor.pages)
        for pagina in range(num_paginas):
            texto += leitor.pages[pagina].extract_text() + "\n\n"
    return texto

def traduzir_texto_por_partes(texto, lang_destino='pt'):
    limite_caracteres = 4000
    tradutor = GoogleTranslator(source='auto', target=lang_destino)
    partes_texto = [texto[i:i+limite_caracteres] for i in range(0, len(texto), limite_caracteres)]
    texto_traduzido = ""

    for parte in partes_texto:
        parte_limpa = parte.strip()
        if len(parte_limpa) > 0 and len(parte_limpa) <= limite_caracteres:
            try:
                parte_traduzida = tradutor.translate(parte_limpa)
                texto_traduzido += parte_traduzida + "\n\n"
            except Exception as e:
                print(f"Erro ao traduzir parte do texto: {e}")
                texto_traduzido += parte_limpa + "\n\n"  # Adiciona o texto original em caso de erro

    return texto_traduzido

# Exemplo de uso
caminho_pdf = ""
texto_extraido = extrair_texto(caminho_pdf)
texto_traduzido = traduzir_texto_por_partes(texto_extraido)  # Traduzir para Português
print(texto_traduzido)
