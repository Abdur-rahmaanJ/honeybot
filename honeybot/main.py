# -*- coding: utf-8 -*-
"""
@author: arj
"""
import configparser
from core import Bot_core

config = configparser.ConfigParser()
config.read('settings.cfg')

pswd = config['BOT_SETTINGS']['password']

x = Bot_core(password=pswd)
x.registered_run()
# x.unregistered_run
