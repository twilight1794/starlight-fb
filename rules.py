#!/usr/bin/python3
# Este archivo es parte de StarlightBot
# Este programa está bajo la Licencia Pública General de GNU
# Copyright (c) 2020 Giovanni Alfredo Garciliano Díaz.

# onMessage
def command(*args):
    if not len(args):
        raise TypeError('A command must be specified.')
    def dec(mod):
        if hasattr(mod, 'events'):
            mod.events.update({'command': [*args]})
        else:
            mod.events = {'command': [*args]}
        return mod
    return dec

def regex(*args):
    if not len(args):
        raise TypeError('A regex must be specified.')
    def dec(mod):
        if hasattr(mod, 'events'):
            mod.events.update({'regex': [*args]})
        else:
            mod.events = {'regex': [*args]}
        return mod
    return dec

def mentions(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'mentions': val})
        else:
            mod.events = {'mentions': val}
        return mod
    return dec

def file(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'file': val})
        else:
            mod.events = {'file': val}
        return mod
    return dec

# onColorChange
def color(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'color': val})
        else:
            mod.events = {'color': val}
        return mod
    return dec

# onEmojiChange
def emojiThread(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'emojiThread': val})
        else:
            mod.events = {'emojiThread': val}
        return mod
    return dec

# onTitleChange
def title(mod):
    if hasattr(mod, 'events'):
        mod.events.update({'title': [True]})
    else:
        mod.events = {'title': [True]}
    return mod

# onImageChange
def imageThread(mod):
    if hasattr(mod, 'events'):
        mod.events.update({'imageThread': [True]})
    else:
        mod.events = {'imageThread': [True]}
    return mod

# onNicknameChange
def nickname(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'nickname': val})
        else:
            mod.events = {'nickname': val}
        return mod
    return dec

# onAdminAdded
def addAdmin(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'addAdmin': val})
        else:
            mod.events = {'addAdmin': val}
        return mod
    return dec

# onAdminRemoved
def removeAdmin(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'removeAdmin': val})
        else:
            mod.events = {'removeAdmin': val}
        return mod
    return dec

# onMessageUnsent
def unsend(mod):
    if hasattr(mod, 'events'):
        mod.events.update({'unsend': [True]})
    else:
        mod.events = {'unsend': [True]}
    return mod

# onPeopleAdded
def adds(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'adds': val})
        else:
            mod.events = {'adds': val}
        return mod
    return dec

# onPersonRemoved
def removes(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'removes': val})
        else:
            mod.events = {'removes': val}
        return mod
    return dec

# onReactionAdded
def reacts(*args):
    def dec(mod):
        if len(args):
            val = [*args]
        else:
            val = [...]
        if hasattr(mod, 'events'):
            mod.events.update({'reacts': val})
        else:
            mod.events = {'reacts': val}
        return mod
    return dec

# onReactionRemoved
def unreacts(mod):
    if hasattr(mod, 'events'):
        mod.events.update({'unreacts': [True]})
    else:
        mod.events = {'unreacts': [True]}
    return mod
