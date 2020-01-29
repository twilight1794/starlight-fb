from fbchat import models
from rules import *
from random import randint

@command('dado')
def run(**kwargs):
    num = str(randint(1,6))
    kwargs['fbobj'].send(models.Message(text=num), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
