# -*- coding: utf-8 -*-
"""
[log.py]
Log Plugin

[Author]
Gico Carlo Evangelista, https://gicocarlo.me/

[About]
Logs the chat into a log.txt file
"""

import os
import logging

class Plugin:
    # Makes a new log dir if not existent
    # Change according to where you have honeybot dir
    #log_path = "/log"
    try:
        if not os.path.exists(log_path):
            os.makedirs('log')
    except:
        pass
    #os.chdir(log_path)

    # logging config
    logging.basicConfig(
        filename="logs.txt",
        level=logging.INFO,
        format="%(asctime)s:%(message)s"
        )

    def __init__(self):
        pass

    def run(self, incoming, methods, info):
        msgs = info['args'][1:]
        try:
            if info['command'] == 'PRIVMSG':
                # Parse the user ID from info['prefix']
                raw_user = info['prefix']
                user_index = raw_user.find('!')
                user = raw_user[0:user_index]

                # Logging the chat into logs.txt
                logging.info(' {}: {}'.format(user, msgs[0]))

        except Exception as e:
            print('woops plugin error ', e)
