from fbchat import models
from rules import *

@command('calc')
def run(**kwargs):
    cmd = kwargs['message_object'].text.partition(' ')
    try:
        res = eval(cmd[2].replace('exit','').replace('^','**'))
    except ZeroDivisionError:
        res = 'No puedes dividir entre cero'
    except:
        res = 'Syntax Error'
    kwargs['fbobj'].send(models.Message(text=res), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
