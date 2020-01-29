from fbchat import models
from rules import *
from urllib.parse import quote_plus
import requests

@regex(r'^\d$')
@command('wp')
def run(**kwargs):
    msgs = []
    first = True
    if not 'wp' in kwargs['memory']:
        cmd = kwargs['message_object'].text.partition(' ')
        if cmd[2]:
            art = requests.get('https://es.wikipedia.org/w/api.php?action=query&prop=extracts&titles='+quote_plus(cmd[2])+'&exsectionformat=plain&exintro=y&explaintext=y&format=json').json()
            if not 'missing' in list(art['query']['pages'].values())[0] and list(art['query']['pages'].values())[0]['extract']:
                title = list(art['query']['pages'].values())[0]['title']
                cont = list(art['query']['pages'].values())[0]['extract']
                msgs.append('*'+title+'*')
                msgs.append(cont)
            else:
                busq = requests.get('https://es.wikipedia.org/w/api.php?action=query&list=search&srsearch='+quote_plus(cmd[2])+'&format=json').json()
                if busq['query']['searchinfo']['totalhits']:
                    kwargs['memory']['wp'] = {}
                    msgs.append('Coincidencias para «*'+cmd[2]+'*»\nEscoge un número')
                    cnt = 5
                    for i in busq['query']['search']:
                        if cnt == 0:
                            break
                        msgs.append(str(5-cnt)+': '+i['title'])
                        kwargs['memory']['wp'][str(5-cnt)]=i['title']
                        cnt = cnt-1
                else:
                    msgs.append('No se ha encontrado el artículo')
        else:
            msgs.append('Qué se supone que debo buscar?')
    else:
        if kwargs['message_object'].text in kwargs['memory']['wp']:
            art = requests.get('https://es.wikipedia.org/w/api.php?action=query&prop=extracts&titles='+quote_plus(kwargs['memory']['wp'][kwargs['message_object'].text])+'&exsectionformat=plain&exintro=y&explaintext=y&format=json').json()
            del kwargs['memory']['wp']
            title = list(art['query']['pages'].values())[0]['title']
            cont = list(art['query']['pages'].values())[0]['extract']
            msgs.append('*'+title+'*')
            msgs.append(cont)

    for i in msgs:
        if first:
            kwargs['fbobj'].send(models.Message(text=i, reply_to_id=kwargs['message_object'].uid), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
            first = False
        else:
            kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
