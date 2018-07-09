# -*- coding: utf-8 -*-
"""

"""
import random

class Plugin:
    def __init__(self):
        self.topics = {
                'bot':{
                       'words':['bot', 'robot', 'artificial intelligence', 'ai'],
                       'occurs':1,
                       'replies':['you are thinking about me and my cousins', 
                       'bots are we?']
                        },
                'nature':{
                       'words':['earth', 'flower', 'lake', 'sea', 'world', 
                                'forest', 'grass'],
                       'occurs':2,
                       'replies':['we must remind ourselves to protect our lovely '+
                                'planet', 
                                'plant a tree when you can']
                        },
                }


    def run(self, incoming, methods, info):
        try:
            msgs = info['args'][1:][0].split()
            
            if info['command'] == 'PRIVMSG':
                if len(msgs) > 1:
                    msgs = set(msgs)
                    
                    for topic in self.topics:
                        meet = set(self.topics[topic]['words']).intersection(msgs)
                        
                        if len(meet) == self.topics[topic]['occurs']:
                            methods['send'](info['address'], 
                                   random.choice(self.topics[topic]['replies'])
                                   )
                        
        except Exception as e:
            print('\n*error*\nwoops plugin', __file__, e, '\n')
