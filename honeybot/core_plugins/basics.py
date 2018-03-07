# -*- coding: utf-8 -*-
"""
@author: arj
"""
def data(incoming, attributes):
    
    words = incoming.split()
    sender, message, msg = '', '', []
    if '.'.join(attributes['server_url'].split('.')[1:]) not in words[0]:
        sender = incoming.split('!')[0][1:]
        message = incoming[1:].split(':')[1]
        msg = message.split()
        
    def address():
        address = ''
        if words[2] != attributes['name'] :
            address = words[2]
        elif words[2] == attributes['name'] :
            address = sender
        return address
    
    return {'words':words,
            'sender':sender,
            'msg_str':message,
            'msg_list':msg,
            'address':address()
            }


def command(x, info):
    return info['msg_list'][x].lower()

class Plugin:
    def __init__(self):
        pass
    
    def run(self, attributes, incoming, methods):
        try:
            info = data(incoming, attributes)
            def command(x):
                return info['msg_list'][x].lower()
            
            if command(0) in ['hello', 'hi', 'hey', 'hoi']:
                if command(1) == 'bot':
                    methods['send'](info['address'], command(0)+' '+info['sender'])
                    
            elif command(0) == 'join':
                methods['join'](command(1))
        except:
            pass
        print()
        
        
        
        
        
        
        
        