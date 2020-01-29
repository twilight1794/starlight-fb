from fbchat import models
from rules import *
from lxml.html.soupparser import fromstring
import requests

@command('mlibre')
def run(**kwargs):
    msgs = []
    cmd = kwargs['message_object'].text.partition(' ')
    if not cmd[2]:
        msgs.append('No has especificado ninguna palabra')
        return
    elif not cmd[2] == '+' or (cmd[2] == '+' and not kwargs['memory']['mlibre']):
        kwargs['memory']['mlibre'] = []
        busq = requests.get('https://listado.mercadolibre.com.mx/'+cmd[2].replace('-', ' '))
        html = fromstring(busq.text)
        kwargs['memory']['mlibre'] = html.cssselect('.item__info-link')
    ct = 5
    while kwargs['memory']['mlibre']:
        if ct>0:
            i=kwargs['memory']['mlibre'].pop(0)
            precio = i.cssselect('.price__fraction')[0].text
            enlace = i.attrib['href']
            egratis = ' (envío gratis)' if i.cssselect('.free-shipping') else ''
            full = ' ⚡' if i.cssselect('.item--has-fulfillment') else ''
            stars = '⭐'*len(i.cssselect('.star-icon-full'))
            half= '✨'*len(i.cssselect('.star-icon-half'))
            texto = i.cssselect('.main-title')[0].text
            msgs.append('*'+texto+'*:\n$'+precio+egratis+full+'\n'+stars+half+'\n'+enlace)
            ct = ct-1
        else:
            break
    for i in msgs:
        kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
