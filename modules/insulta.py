from fbchat import models
from random import choice
from rules import *
import re

@command('insulta')
def run(**kwargs):
    insultos = [
        'Yo analizo a {}, pero no le encuentro cerebro!',
        'Ya callate {}, joder'
    ]
    cmd = kwargs['message_object'].text.partition(' ')
    if not re.match('.*(ariel|rapunzel|starlight|gio[bv]ann?i|giobirul|yo[bv]ann?i|alfredo|[ck]arolina|[kc]aro).*', cmd[2].lower()):
        kwargs['fbobj'].send(models.Message(text=choice(insultos).format(cmd[2])), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
    else:
        kwargs['fbobj'].send(models.Message(text='No voy a insultar a mi ama'), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
