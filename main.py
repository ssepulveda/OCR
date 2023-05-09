from pdf2image import convert_from_path
from os import listdir
import pandas as pd

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

RUTA = 'pruebas'
articulosIndefinidos = ['la', 'las', 'ellas', 'el', 'los', 'ellos', 'les']
preposiciones = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde',
                 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante',
                 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras',
                 'versus', 'via']
palabrasExcluidas = articulosIndefinidos + preposiciones

# Crear dataframe
df = pd.DataFrame(columns=['palabra', 'pdf'])
pd.set_option("display.max_rows", None)

# listar PDFs de la carpeta prueba
pdfs = listdir(RUTA)

# Cargar cada PDF y obtener texto
for pdf in pdfs:
    paginas = convert_from_path(RUTA + '/' + pdf)
    for index, pagina in enumerate(paginas):
        print(f"Revisando pagina {index + 1} de {pdf}")
        # Convierte imagenes a texto
        texto = pytesseract.image_to_string(pagina)
        # Obtener cada palabra del texto, quitando los saltos de linea,
        # puntos, y todo en minusculas
        texto = texto.lower().replace('\n', ' ').replace('.', ' ').split(' ')
        for palabra in texto:
            # descartar palabras con numeros y simbolos
            if palabra not in palabrasExcluidas:
                if len(palabra) > 2 and palabra.isalpha():
                    df = df.append({'palabra': palabra, 'pdf': pdf},
                                   ignore_index=True)

conteo = df['palabra'].value_counts()
# Exportar dataframe
df.to_csv('palabras.csv')
conteo.to_csv('conteo.csv', index=True, header=True)
