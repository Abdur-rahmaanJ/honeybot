# -*- coding: utf-8 -*-
"""

"""

class Plugin:
    def __init__(self):
        pass
    
    def run(self, incoming, methods, info):
        try:
            # if '!~' in info['prefix']:
                # print(info)
            if info['command'] == 'PRIVMSG' and info['args'][1] == 'hi':
                methods['send'](info['address'], 'hooo')
        except Exception as e:
            print('woops plug',e)