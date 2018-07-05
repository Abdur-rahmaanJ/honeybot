# -*- coding: utf-8 -*-
"""

"""
from string import ascii_letters

class Plugin:
    def __init__(self):
        pass
        
    def run(self, incoming, methods, info):
        try:
            #if '!~' in info['prefix']:
                #print(info)
            msgs = info['args'][1:][0].split()
            # print(msgs)
            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    if msgs[0] == '.calc':
                        expr = msgs[1]
                        for c in ascii_letters:
                            expr = '' + expr.replace(c, '')
                        methods['send'](info['address'], '{}'.format(
                                eval(expr)))
        except Exception as e:
            print('woops plugin', __file__, e)
            methods['send'](info['address'], 'error in calc command')