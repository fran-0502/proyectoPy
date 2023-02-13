
import pandas as pd

from textblob import TextBlob
from deep_translator import GoogleTranslator

import numpy as np
import pandas as pd
import re

# Gráficos
# ==============================================================================
import plotly.express as plt
import plotly.graph_objects as go

# Preprocesado y modelado
# ==============================================================================
from nltk.corpus import stopwords

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')


def analisis_de_sentimientos(texto):
    textoTraducido = traduccion(texto)
    analisis = TextBlob(textoTraducido)
    valor = analisis.sentiment[0]
    varlorR = round(valor, 2)
    if analisis.sentiment[0] >= 0.25 and analisis.sentiment[0] <= 1:
        return varlorR
    elif analisis.sentiment[0] > -0.25 and analisis.sentiment[0] < 0.25:
        return varlorR
    else:
        return varlorR


def traduccion(texto):
    traductor = GoogleTranslator(source='es', target='en')
    resultado = traductor.translate(texto)
    return resultado.replace("range", "gama")


def limpiar_tokenizar(texto):
    '''
    Esta función limpia y tokeniza el texto en palabras individuales.
    El orden en el que se va limpiando el texto no es arbitrario.
    El listado de signos de puntuación se ha obtenido de: print(string.punctuation)
    y re.escape(string.punctuation)
    '''

    # Se convierte todo el texto a minúsculas
    nuevo_texto = texto.lower()
    # Eliminación de páginas web (palabras que empiezan por "http")
    nuevo_texto = re.sub('http\S+', ' ', nuevo_texto)
    # Eliminación de signos de puntuación
    regex = '[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~]'
    nuevo_texto = re.sub(regex, ' ', nuevo_texto)
    # Eliminación de números
    nuevo_texto = re.sub("\d+", ' ', nuevo_texto)
    # Eliminación de espacios en blanco múltiples
    nuevo_texto = re.sub("\\s+", ' ', nuevo_texto)
    # Tokenización por palabras individuales
    nuevo_texto = nuevo_texto.split(sep=' ')
    # Eliminación de tokens con una longitud < 2
    nuevo_texto = [token for token in nuevo_texto if len(token) > 1]

    return (nuevo_texto)


# print("los sentimientos son:", analisis_de_sentimientos(texto))


texto = 'El gama es una cadena de supermercados genial'

df = pd.read_excel("ejemplo.xlsx")
df.columns = ['autor', 'fecha', 'id', 'comentario']
df['fecha'] = pd.to_datetime(df['fecha'])


df['texto_tokenizado'] = df['comentario'].apply(
    lambda x: limpiar_tokenizar(x))

df_tidy = df.explode(column='texto_tokenizado')
df_tidy = df_tidy.drop(columns='comentario')
df_tidy = df_tidy.rename(columns={'texto_tokenizado': 'token'})

stop_words = list(stopwords.words('spanish'))

df_tidy = df_tidy[~(df_tidy["token"].isin(stop_words))]
df_temp = df_tidy

contador = df_temp["token"].value_counts(ascending=False).to_frame().head(20)
contador.columns = ["cantidad"]
fig = plt.bar(contador, y="cantidad")
fig.show()


