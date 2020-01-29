from fbchat import models
from rules import *

@command('ayuda')
def run(**kwargs):
    cmds = {
        'animeflv': ['Devuelve los primeros 5 resultados del sitio web AnimeFLV.', 'Uso:\n-animeflv parámetros'],
        'ayuda': ['Muestra la ayuda de un comando.', 'Uso:\n-ayuda comando'],
        'bot': ['Informa sobre el bot.', 'Uso:\n-bot'],
        'calc': ['Realiza operaciones matemáticas.', 'Ejemplo:\n-calc 32*32', '1024'],
        'dado': ['Lanza un dado y te dice el número que cayó.', 'Uso:\n-dado'],
        'google':['Devuelve los primeros 2 resultados de búsqueda.','Ejemplo:\n-google tara strong'],
        'insulta': ['Pues eso, insulta.', 'Uso:\n-insulta usuario.'],
        'lmgtfy': ['Para los flojos, un enlace a Google.', 'Alias:\n-gg', 'Uso:\n-lmgtfy cómo hacer un avioncito de papel'],
        'mlibre': ['Devuelve los primeros 5 resultados del sitio web MercadoLibre.', 'Uso:\n-mlibre palabras a buscar'],
        'moneda': ['Lanza una moneda y te dice si cayó sol o águila.', 'Uso:\n-moneda'],
        'nhentai': ['Devuelve los primeros 5 resultados del sitio web nhentai.net.', 'Uso:\n-nhentai palabras a buscar'],
        'ping': ['Si el bot está disponible, devuelve "pong".', 'Uso:\n-ping'],
        'tiempo': ['Muestra el estado del tiempo, y otros datos. Por ahora, sólo en Villahermosa.', 'Uso:\n-tiempo'],
        'wolfram': ['Consultas a Wolfram|Alpha. Devuelve una imagen con el resultado. Útil para resolver ecuaciones, integrales, derivadas y graficar.', 'Ejemplo:\n-wolfram x^2+x^3=12'],
        'wp': ['Muestra un resumen de Wikipedia. Si no encuentra el artículo, muestra 5 posibles coincidencias para elegir a mostrar.', 'Ejemplo:\n-wp Keanu Reeves'],
    }
    cmd = kwargs['message_object'].text.partition(' ')
    if cmd[2]:
        if cmd[2] in cmds:
            for i in cmds[cmd[2]]:
                kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
        else:
            kwargs['fbobj'].send(models.Message(text='El comando no existe'), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
    else:
        msgs = []
        msgs.append('Comandos disponibles:')
        msgs.append(' '.join(cmds.keys()))
        msgs.append('Para saber cómo usar un comando, usa el comando ayuda seguido del comando')
        for i in msgs:
            kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
