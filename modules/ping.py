from fbchat import models
from rules import *

@command('ping')
def run(**kwargs):
    kwargs['fbobj'].send(models.Message(text='pong'), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
