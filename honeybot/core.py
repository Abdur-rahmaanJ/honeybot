# -*- coding: utf-8 -*-
"""

@author: arj
"""

__author__ = 'Abdur-Rahmaan Janhangeer'

import socket
import os
import importlib

plugins = []

     
class Bot_core(object):
    def __init__(self, 
                 server_url = 'chat.freenode.net',
                 port = 6667,
                 name = 'appinventormuBot',
                 owners = ['appinventorMu', 'appinv'],
                 password = '',
                 friends = ['haruno', 'keiserr', 'loganaden'],
                 autojoin_channels = ['##bottestingmu']
                 ):
        self.server_url = server_url
        self.port = port
        self.name = name
        self.owners = owners
        self.password = password
        self.autojoin_channels = autojoin_channels
        self.friends = friends
          
        '''
        NORMAL ATTRIBUTES
        '''
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.isListenOn = 1
        dom = self.server_url.split('.')
        self.domain = '.'.join(dom[-2:])
        self.sp_command = 'hbot'
        self.user_plugins = []
        self.core_plugins = []
  
    '''
    STRINGS
    '''
    def set_nick_command(self):
        return 'NICK ' + self.name + '\r\n'
    
    def present_command(self):
        return 'USER '+self.name+' '+self.name+' '+self.name+' : '+self.name+' IRC\r\n'
    
    def identify_command(self):
        return 'msg NickServ identify ' + self.password + ' \r\n'
    
    def join_channel_command(self, channel):
        return 'JOIN ' + channel + ' \r\n'
    
    def specific_send_command(self, target, msg):
        return "PRIVMSG "+ target +" :"+ msg +"\r\n"
    
    def pong_return(self):
        return 'PONG \r\n'
    
    '''
    BOT UTIL FUNCTIONS
    '''
    def send(self, msg):
        self.irc.send(bytes( msg, "UTF-8")) 
        
    def send_target(self, target, msg):
        self.send(self.specific_send_command(target, msg))
        
    def join(self, channel):
        self.send(self.join_channel_command(channel))

    def load_plugins(self, modules, list_to_add):
        for root, dirs, files in os.walk(modules+"/"):  
            #print(files)
            for file in files:
                #print('*'*7,file)
                name = file.split('.')
                #print(name[0])
                if name[0] not in plugins and name[0] != '__init__' and name[0] != 'utils' and name[1] != 'pyc':
                    plugins.append(name[0])
                    module = importlib.import_module(modules+'.'+name[0])
                    plugin = getattr(module, 'Plugin')
                    #print('*'*7,plugin)
                    obj = plugin()
                    list_to_add.append(obj)
    
    def methods(self):
        return {
                'send_raw':self.send,
                'send':self.send_target,
                'join':self.join
                }
        
    def run_plugins(self, listfrom, incoming):
        for p in listfrom:
            if isinstance(p, str) == False:
                #print(p.name)
                p.run( vars(self), incoming, self.methods())
        
    '''
    MESSAGE PARSING
    '''
    def core_commands_parse(self, incoming):
        '''
        PARSING UTILS
        '''
        
        
        '''
        PLUGINS
        '''
        self.run_plugins(self.user_plugins, incoming)
        self.run_plugins(self.core_plugins, incoming)


    '''
    BOT IRC FUNCTIONS
    '''
    def connect(self):
        self.irc.connect((self.server_url, self.port))
    
    def identify(self):
        self.send(self.identify_command())
    
    def greet(self):
        self.send(self.set_nick_command())
        self.send(self.present_command())
        for channel in self.autojoin_channels:
            self.send(self.join_channel_command(channel))
    
    def pull(self):
        while self.isListenOn:
            data = self.irc.recv(2048)
            raw_msg = data.decode("UTF-8")
            msg = raw_msg.strip('\n\r')
            self.stay_alive(msg)
            self.core_commands_parse(msg)
            print(msg)
            if len(data) == 0:
                self.irc.close()
                self.registered_run()
                

    # all in one for registered bot
    def registered_run(self):
        self.connect()
        self.identify()
        self.greet()
        self.load_plugins('user_plugins', self.user_plugins)
        self.load_plugins('core_plugins', self.core_plugins)
        self.pull()
        
    def unregistered_run(self):
        self.connect()
        self.greet()
        self.load_plugins('user_plugins', self.user_plugins)
        self.load_plugins('core_plugins', self.core_plugins)
        self.pull()
        
    '''
    ONGOING REQUIREMENT/S
    '''
    def stay_alive(self, incoming):
        if 'ping' in incoming.lower():
            part = incoming.split(':')
            if self.domain in part[1]:
                self.send(self.pong_return())
                print(''' * message *
                      ping detected from
                      ''', part[1])
                self.irc.recv(2048).decode("UTF-8")













