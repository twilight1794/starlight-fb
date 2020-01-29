from fbchat import models
from rules import *

@command('bot')
def run(**kwargs):
    msg = [
        'Starlight v1.0',
        'Un bot escrito en Python, por @Rapunzel',
        'https://gitlab.com/twilight1794/starlight'
    ]
    for i in msg:
        kwargs['fbobj'].send(models.Message(text=i), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
