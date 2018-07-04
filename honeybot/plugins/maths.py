# -*- coding: utf-8 -*-
"""

"""
import math 

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
                    if msgs[0] == '.sin':
                        sine = math.sin(int(msgs[1]))
                        methods['send'](info['address'], '{}'.format(sine))
                    elif msgs[0] == '.cos':
                        cosine = math.cos(int(msgs[1]))
                        methods['send'](info['address'], '{}'.format(cosine))
                    elif msgs[0] == '.tan':
                        tangent = math.tan(int(msgs[1]))
                        methods['send'](info['address'], '{}'.format(tangent))
        except Exception as e:
            print('woops plug',e)

