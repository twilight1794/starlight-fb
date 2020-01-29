from fbchat import models
from rules import *
from lxml.html.soupparser import fromstring
import requests

@command('nhentai')
def run(**kwargs):
    msgs = []
    cmd = kwargs['message_object'].text.partition(' ')
    if not cmd[2]:
        msgs.append('No has especificado ninguna palabra')
        return
    elif not cmd[2] == '+' or (cmd[2] == '+' and not kwargs['memory']['nhentai']):
        kwargs['memory']['nhentai'] = []
        busq = requests.get('https://nhentai.net/search/?q='+cmd[2])
        html = fromstring(busq.text)
        kwargs['memory']['nhentai'] = html.cssselect('.gallery')
    ct = 5
    while kwargs['memory']['nhentai']:
        if ct>0:
            i=kwargs['memory']['nhentai'].pop(0)
            enlace = i[0].attrib['href']
            texto = i.cssselect('.caption')[0].text
            msgs.append('*'+texto+'*:\nhttps://nhentai.net'+enlace)
            ct = ct-1
        else:
            break
    for i in msgs:
        kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
