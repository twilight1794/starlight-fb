from fbchat import models
from rules import *
from random import randint

@command('moneda')
def run(**kwargs):
    lado = 'sol' if randint(0,1) else 'águila'
    kwargs['fbobj'].send(models.Message(text='Cayó '+lado), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
