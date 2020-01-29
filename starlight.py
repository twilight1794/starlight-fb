#!/usr/bin/python3
# Este archivo es parte de StarlightBot
# Este programa está bajo la Licencia Pública General de GNU
# Copyright (c) 2020 Giovanni Alfredo Garciliano Díaz.

from fbchat import Client
import fbchat.models as models
import importlib
import json
import glob
import re
from time import sleep

modules = {}
memory = {}
events = {'command': {}, 'regex': {}, 'mentions': {}, 'file': {}, 'color': {}, 'emojiThread': {}, 'title': {}, 'imageThread': {}, 'nickname': {}, 'addAdmin': {}, 'removeAdmin': {}, 'unsend': {}, 'adds': {}, 'removes': {}, 'reacts': {}, 'unreacts': {}}
cookie = None

def listener(event, modules, **kwargs):
    if not kwargs['author_id'] == client.uid:
        for i in modules:
            try:
                i(fbobj=client, config=config, memory=memory, event=event, **kwargs)
            except ZeroDivisionError as e:
                client.send(models.Message(text='Error al ejecutar el comando :c'), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])
                client.send(models.Message(text=str(e)), thread_id=kwargs['thread_id'], thread_type=kwargs['thread_type'])

class Bot(Client):
    def onMessage(self, **kwargs):
        # Command match
        for k, v in events['command'].items():
            command = kwargs['message_object'].text.partition(' ')[0][1:]
            if k == command:
                listener('command', v, **kwargs)
                break
        # Regex match:
        for k, v in events['regex'].items():
            if re.match(k, kwargs['message_object'].text):
                listener('regex', v, **kwargs)
        # Mention match:
        for k, v in events['mentions'].items():
            if kwargs['message_object'].mentions and k in kwargs['message_object'].mentions:
                listener('mentions', v, **kwargs)
                break

    def onColorChange(self, **kwargs):
        for k, v in events['color'].items():
            if k == kwargs['new_color'].name or k == ...:
                listener('color', v, **kwargs)

    def onEmojiChange(self, **kwargs):
        for k, v in events['emojiThread'].items():
            if k == kwargs['new_emoji'].name or k == ...:
                listener('emojiThread', v, **kwargs)

    def onTitleChange(self, **kwargs):
        if 'title' in events:
            if True in events['title']:
                listener('title', events['title'][True], **kwargs)

    def onImageChange(self, **kwargs):
        if 'imageThread' in events:
            if True in events['title']:
                listener('imageThread', events['title'][True], **kwargs)

    def onNicknameChange(self, **kwargs):
        for k, v in events['nickname'].items():
            if k == kwargs['changed_for'] or k == ...:
                listener('nickname', v, **kwargs)

    def onAdminChange(self, **kwargs):
        for k, v in events['addAdmin'].items():
            if k == kwargs['added_id'] or k == ...:
                listener('addAdmin', v, **kwargs)

    def onAdminRemove(self, **kwargs):
        for k, v in events['removeAdmin'].items():
            if k == kwargs['removed_id'] or k == ...:
                listener('removeAdmin', v, **kwargs)

    def onMessageUnsent(self, **kwargs):
        if 'unsend' in events:
            if True in events['title']:
                listener('unsend', events['unsend'][True], **kwargs)

    def onPeopleAdded(self, **kwargs):
        for k, v in events['adds'].items():
            for i in kwargs['added_ids']:
                if k == i:
                    listener('adds', v, **kwargs)
            if k == ...:
                listener('adds', v, **kwargs)

    def onPersonRemoved(self, **kwargs):
        for k, v in events['removes'].items():
            if k == kwargs['removed_id'] or k == ...:
                listener('adds', v, **kwargs)

    def onReactionAdded(self, **kwargs):
        for k, v in events['unreacts'].items():
            if k == kwargs['reaction'].name or k == ...:
                listener('unreact', v, **kwargs)

    def onReactionRemoved(self, **kwargs):
        if 'unreact' in events:
            if True in events['title']:
                listener('unreact', events['unreact'][True], **kwargs)

# Cargar configuración
try:
    with open('config.json') as f:
        config = json.load(f)
except json.decoder.JSONDecodeError:
    print('Config is malformed!')
    exit(1)
except FileNotFoundError:
    print('Config is required!')
    exit(1)
else:
    print('Config loaded!')
# Abrir cookie, si hay
try:
    with open('fbcookie', 'r') as f:
        cookie = json.loads(f.read())
except:
    print('Cookie not found, it will use credentials.')
else:
    print('Cookie loaded!')
# Iniciar sesión
try:
    client = Bot(config['starlight']['user'], config['starlight']['password'], session_cookies=cookie)
except:
    print('Invalid login!')
    exit(1)
else:
    try:
        if not cookie:
            with open('fbcookie', 'w') as f:
                cookie = client.getSession()
                f.write(json.dumps(cookie))
        print('Cookies saved on file "fbcookie"!')
    except:
        print('Cannot store the session cookie!')
# Cargar módulos
for i in glob.glob('modules/*.py'):
    try:
        mod = i.split('/')[-1][:-3]
        modules[mod] = importlib.import_module('modules.'+mod).run
        for event, list in modules[mod].events.items():
            for param in list:
                if param in events[event]:
                    events[event][param].append(modules[mod])
                else:
                    events[event][param] = [modules[mod]]
        print('Module', mod, 'loaded!')
    except:
        print('Mod', mod, 'can\'t be loaded')

# Escuchar comandos!
client.listen()
