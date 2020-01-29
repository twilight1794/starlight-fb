from fbchat import models
from rules import *
from urllib.parse import quote_plus

@command('wolfram')
def run(**kwargs):
    cmd = kwargs['message_object'].text.partition(' ')
    if cmd[2]:
        kwargs['fbobj'].sendRemoteFiles('http://api.wolframalpha.com/v1/simple?appid='+kwargs['config']['wolfram']['api_key']+'&input='+quote_plus(cmd[2]), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
    else:
        kwargs['fbobj'].send(models.Message(text=res), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
