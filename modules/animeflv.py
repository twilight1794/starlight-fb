from fbchat import models
from rules import *
from lxml.html.soupparser import fromstring
import requests

@command('animeflv')
def run(**kwargs):
    msgs = []
    cmd = kwargs['message_object'].text.partition(' ')
    if not cmd[2]:
        msgs.append('No has especificado ninguna palabra')
        return
    elif not cmd[2] == '+' or (cmd[2] == '+' and not kwargs['memory']['animeflv']):
        kwargs['memory']['animeflv'] = []
        busq = requests.get('https://animeflv.net/browse?q='+cmd[2].replace(' ', '+'))
        html = fromstring(busq.text)
        kwargs['memory']['animeflv'] = html.cssselect('article.Anime')
    ct = 5
    while kwargs['memory']['animeflv']:
        if ct>0:
            i=kwargs['memory']['animeflv'].pop(0)
            enlace = i[0].attrib['href']
            tipo = i[0].cssselect('.Type')[0].text
            texto = i.cssselect('.Title')[0].text
            msgs.append('*'+texto+'* ('+tipo+'):\nhttps://animeflv.net'+enlace)
            ct = ct-1
        else:
            break
    for i in msgs:
        kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
