# -*- coding: utf-8 -*-
"""
[echo.py]
Echo Plugin
[Author]
Angelo Giacco
[About]
Bot will message channel what you write after '.echo'
Very simple but also useful for testing plugins that require more than one person
Created when developing monopoly plugin
[Commands]
.echo <<stuff>>
sends stuff to channel from bot
"""

class Plugin:
    def __init__(self):
        pass

    def run(self,incoming,methods,info):
        try:
            msgs = info['args'][1:][0].split(" ")
            if info["command"] == "PRIVMSG" and msgs[0] == ".echo":
                message = " ".join(msgs[1:])
                methods['send_raw'](info['address'],message)#this will get executed but not shown
                methods['send'](info['address'],message)#this will get shown but not executed
        except Exception as e:
            print("woops echo plugin error",e)
