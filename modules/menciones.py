from fbchat import models
from rules import *
import re

@regex('.*@todos.*')
def run(**kwargs):
    names = {}
    objGrp = list(kwargs['fbobj'].fetchGroupInfo(kwargs['thread_id']).values())[0]
    for i in objGrp.participants:
        if i in objGrp.nicknames:
            names[i] = objGrp.nicknames[i]
        else:
            objPpl = list(kwargs['fbobj'].fetchThreadInfo(i).values())[0]
            names[i] = objPpl.first_name
    cad = ''
    tupls = []
    for k, v in names.items():
        cad = cad + '{} '
        tupls.append(tuple((k, '@'+v)))
    msg = models.Message.formatMentions(cad, *tupls)
    msg.reply_to_id = kwargs['message_object'].uid
    kwargs['fbobj'].send(msg, thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
