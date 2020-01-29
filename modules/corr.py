from fbchat import models
from rules import *
import re

@regex('^s/.*/.*$')
def run(**kwargs):
    cad = kwargs['message_object'].replied_to.text
    subst = re.match(r'^s/(.*)/(.*)$', kwargs['message_object'].text)
    cad2 = cad.replace(subst.group(1),subst.group(2))
    l = kwargs['fbobj'].fetchGroupInfo(kwargs['thread_id'])
    if kwargs['message_object'].author in list(l.values())[0].nicknames:
        kwargs['fbobj'].send(models.Message(text=list(l.values())[0].nicknames[kwargs['message_object'].author]+' quiso decir:\n'+cad2, reply_to_id=kwargs['message_object'].replied_to.uid), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
    else:
        kwargs['fbobj'].send(models.Message(text='*'+cad2, reply_to_id=kwargs['message_object'].replied_to.uid), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
