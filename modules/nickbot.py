from fbchat import models
from rules import *
from datetime import datetime

@regex('.*')
@nickname()
@color()
@emojiThread()
@title
@imageThread
def run(**kwargs):
    if kwargs['event']=='nickname':
        print('EA')
        if kwargs['changed_for'] in kwargs['config']['nickbot']['nicks']:
            kwargs['fbobj'].changeNickname(kwargs['config']['nickbot']['nicks'][kwargs['changed_for']], kwargs['changed_for'], thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
    d = datetime.now().weekday()
    if str(d) in kwargs['config']['nickbot']['days']:
        dt = kwargs['config']['nickbot']['days'][str(d)]
        kwargs['fbobj'].changeThreadEmoji(dt['emoji'], thread_id=kwargs['thread_id'])
        kwargs['fbobj'].changeThreadTitle(dt['title'], thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
        print(str(type(getattr(models.ThreadColor, dt['color']))))
        kwargs['fbobj'].changeThreadColor(getattr(models.ThreadColor, dt['color']), thread_id=kwargs['thread_id'])
