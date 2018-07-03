# -*- coding: utf-8 -*-
"""

"""
import random

class Plugin:
    def __init__(self):
        pass
    
    def gen_uname(self):
        p1 = ['flower', 'tree', 'land', 'moon']
        p2 = ['star', 'hope', 'ant', 'spyder']
        return '{}{}'.format(random.choice(p1), random.choice(p2))
        
    def run(self, incoming, methods, info):
        try:
            #if '!~' in info['prefix']:
                #print(info)
            msgs = info['args'][1:]
            if info['command'] == 'PRIVMSG' and msgs[0] == '.uname':
                methods['send'](info['address'], self.gen_uname())
        except Exception as e:
            print('woops plug',e)
