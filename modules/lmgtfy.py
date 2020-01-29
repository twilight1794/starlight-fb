from fbchat import models
from random import choice
from rules import *

@command('lmgtfy', 'gg')
def run(**kwargs):
    cmd = kwargs['message_object'].text.partition(' ')
    if cmd[2]:
        kwargs['fbobj'].send(models.Message(text='https://es.lmgtfy.com/?q='+cmd[2].replace(' ','+').replace('&', '%26').replace('%','%25')+'&s=g&iie=1'), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
