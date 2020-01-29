from fbchat import models
from rules import *
from urllib.parse import quote_plus
from html import unescape
import requests
import re

@command('google')
def run(**kwargs):
    msgs = []
    cmd = kwargs['message_object'].text.partition(' ')
    if not cmd[2]:
        msgs.append('No has especificado ninguna palabra')
        return
    elif not cmd[2] == '+' or (cmd[2] == '+' and not kwargs['memory']['google']):
        kwargs['memory']['google'] = []
        busq = requests.get('https://www.googleapis.com/customsearch/v1?key=AIzaSyBIlkNM208eD2SNwqu3zNSYwsUDT-YWfR8&cx=014588815263890643943:wtgjesbvlpm&prettyPrint=false&fields=searchInformation,items(link,title,htmlSnippet)&q='+quote_plus(cmd[2])).json()
        if busq['searchInformation']['totalResults'] == '0':
            msgs.append('No hay resultados de búsqueda')
        kwargs['memory']['google'] = busq['items']
    ct = 5
    while kwargs['memory']['google']:
        if ct>0:
            i=kwargs['memory']['google'].pop(0)
            enlace = i['link']
            titulo = i['title']
            texto = unescape(re.sub('</?[A-Za-z]+/?>', '', re.sub('</?b>', '*', re.sub('</?i>', '_', i['htmlSnippet']))))
            msgs.append('*'+titulo+'*:\n'+enlace+'\n'+texto)
            ct = ct-1
        else:
            break
    for i in msgs:
        kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
