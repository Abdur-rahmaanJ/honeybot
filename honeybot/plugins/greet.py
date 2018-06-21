# -*- coding: utf-8 -*-
"""

"""

class Plugin:
    def __init__(self):
        pass
    
    def run(self, incoming, methods):
        print('greet')
        msg = ''
        if incoming[-1][0] == ':':
            msg = incoming[-1][1:]
            if msg == 'hi':
                if '#' in incoming[-2]:
                    methods['send'](incoming[-2], 'hoho')
                else:
                    methods['send'](incoming[0].split('!~')[0][1:], 'hoho')
        pass
