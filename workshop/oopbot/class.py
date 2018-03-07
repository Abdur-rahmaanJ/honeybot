#######################################################
#oop bot basics. ifs not yet added . need devlopment .
#######################################################

#class NNN (object):
#	varglo = 0

#	def __init__ (self):
#		self.name='hhhh'
#		pass
#
#	def pri2(self):
#		print('nn')
#
#
#def printerb() :
#	print('test ok')
#

from tkinter import*

import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

import _thread#unused
import socket
import time
import os

import urllib.request
import json

import random
import math

#from wordpress_xmlrpc import Client, WordPressPost
#from wordpress_xmlrpc.methods import posts # NewPost

import config

class Honeybot (object):
	var = 1
	localtime = time.asctime( time.localtime(time.time()) )
	PRIV = 'PRIVMSG '
	irc = socket.socket()



	def __init__ (self):
		self.name = 'mi'

	def inflow(self):
		return Honeybot.irc.recv(4096)

	def prvar(self):
		print(Honeybot.var)
		print(config.NICKNAME)
		print(config.VARR)
		print(config.OWNERS[0])

	def connection(self):

		Honeybot.irc.connect((config.IRC_SERVER, config.IRC_PORT))
		Honeybot.inflow(self)
		Honeybot.irc.send(bytes('NICK ' + config.NICKNAME + '\r\n','utf8'  )  )
		#pingChecker(Honeybot.irc.recv(4096))
		Honeybot.irc.send(bytes('USER appinventormuBot appinventormuBot appinventormuBot : appinventormuBot IRC\r\n','utf8'  )  )
		#pingChecker(Honeybot.irc.recv(4096))
		Honeybot.irc.send(bytes('msg NickServ identify ' + config.PASSWORD + " \r\n"  ,'utf8')  )
		#pingChecker(Honeybot.irc.recv(4096))
		Honeybot.irc.send(bytes('NICKSERV  identify ' + config.NICKNAME+' '+config.PASSWORD+ '\r\n','utf8'  )  )
		#pingChecker(Honeybot.irc.recv(4096))
		time.sleep(3)
		Honeybot.irc.send(bytes('JOIN ' + config.IRC_CHANNEL + '\r\n','utf8'  )  )

	def pingChecker(self):

		pingLine=Honeybot.inflow(self)
		
		if pingLine.find(bytes('PING'  ,'utf8')) != -1:
			pingLine = pingLine.rstrip().split()
			if pingLine[0] == bytes("PING"  ,'utf8'):
				Honeybot.irc.send(bytes("PONG "  ,'utf8') + pingLine[1] + bytes("\r\n"  ,'utf8')  )


	def printer(self):
		msgLine = Honeybot.inflow(self)
		if msgLine.find(bytes('PRIVMSG' ,'utf8')) != -1 or msgLine.find(bytes('NOTICE'  ,'utf8')) != -1 :
			completeLine = str(msgLine[1:]).replace("'b",'').split(':', 1)
			info = completeLine[0].split()
			message = (completeLine[1].split("\\r")[0]).replace("'b",'')
			sender = info[0][2:].split("!", 1)[0]
			refinedmsg = str(message.lower())
			
			print("Complete Line-->" + str(completeLine))
			print("Info-->" + str(info))
			print("Message-->" + str(message))
			print("Sender-->" + str(sender) + "\n")
