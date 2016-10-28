__author__ = 'me'

#My first messing-up with python. Code in progress. Here only for checking. use at your own risk (those indents)!
#Honeybot's disparities in code style is because of a trying out of Python
#see the features in the honeybotfeatures.txt

import socket
import time
import os

import urllib2
import json

aa='gg'
localtime = time.asctime( time.localtime(time.time()) )
#script, filename = argv
key='0def10027afaebb7'

BOT_IRC_SERVER ="chat.freenode.net"
BOT_IRC_CHANNEL = "##bottestingmu"
BOT_IRC_PORT = 6667
BOT_NICKNAME = "appinventormuBot"
BOT_OWNER = "appinventormu"
BOT_PASSWORD = "PASSWORD HERE"

def pingChecker(pingLine):
    if pingLine.find(bytes('PING'  )) != -1:
        pingLine = pingLine.rstrip().split()
        if pingLine[0] == bytes("PING"  ):
            irc.send(bytes("PONG "  ) + pingLine[1] + bytes("\r\n"  ))

def messagechecker(msgLine):
    completeLine = str(msgLine[1:]).split(':', 1)
    info = completeLine[0].split()
    message = completeLine[1].split("\\r")[0]
    sender = info[0][0:].split("!", 1)[0]
    print("Complete Line-->" + str(completeLine))
    print("Info-->" + str(info))
    print("Message-->" + str(message))
    print("Sender-->" + str(sender) + "\n")

    if (str(message) == "hi\r\n"):
        irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hi there, ' + str(sender) + '!\r\n'  ))

    if (str(message) == "quitplz\r\n" and sender =='appinventormu'):
        irc.send(bytes("QUIT\r\n"))

    if ('bad' in str(message)):
            irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' mind yourself! you said something bad!\r\n'  ))
    elif (str(message) == "sorry\r\n"):
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hi there, ' + str(sender) + ' just be careful next time!\r\n'  ))
	else:
	if (str(message) == "where do you live? \r\n"):
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Dear, ' + str(sender) + ' jwhere my master live. !master to see his name..\r\n'  ))
	#if (str(message)=="hello\r\n"):
			#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' oh hell, sorry hello!\r\n'  ))

    if ('i hate you' in str(message)):
            irc.send(bytes('KICK ' + BOT_IRC_CHANNEL + ' ' + str(sender) + ' mind yourself next time!\r\n'  ))

    if ('fuck' in str(message)):
            irc.send(bytes('KICK ' + BOT_IRC_CHANNEL + ' ' + str(sender) + ' mind yourself next time!\r\n'  ))


	#if (str(message) == "sorry\r\n"):
			#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Nice ' + str(sender) + ' but behave next time !\r\n'  ))



    list1 = ['fuck','faggot','fool','sex','buck' ,'shit']
    if any(word in str(message) for word in list1):
        irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' dont swear!\r\n'  ))
        irc.send(bytes('KICK ' + BOT_IRC_CHANNEL + ' ' + str(sender) + ' mind yourself next time!\r\n'  ))

    list2 = ['love','woman','sexy' ]
    if any(word in str(message) for word in list2):
        irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' are you in love?\r\n'  ))

    if (str(message) == "bot tiny story\r\n" and sender =='appinventormu'):
        irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :yes master ' + str(sender) + ' here it is : once upon a time . . . and thats all!\r\n'  ))

    if message[0] == '!' and sender == BOT_OWNER:
        messageCommand = message[1:].split()
        if messageCommand[0] == "master":
            irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :I was created by ' + BOT_OWNER + '\r\n'  ))


	if (str(message[0:4])==".wea\r\n"):
		try:
			aa= str(message[5:len(str(message))])
			f = urllib2.urlopen('http://api.wunderground.com/api/'+key+'/geolookup/conditions/q/'+aa+'.json')
			json_string = f.read()
			parsed_json = json.loads(json_string)
			location = parsed_json['location']['city']
			temp_f = parsed_json['current_observation']['temp_f']
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + "Current temperature in %s is: %s%" + (location, temp_f)+'\r\n'  ))
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' \/\/\/\/\/\/\/\/ !\r\n'  ))
			f.close()
		except:
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' invalid command!\r\n'  ))
			pass

def sendmessage(rcv, msg):
    print(bytes('PRIVMSG ' + rcv + ' :' + msg + '\r\n'  ))
    irc.send(bytes('PRIVMSG ' + rcv + ' :' + msg + '\r\n'  ))

irc = socket.socket()
irc.connect((BOT_IRC_SERVER, BOT_IRC_PORT))
irc.recv(4096)
irc.send(bytes('NICK ' + BOT_NICKNAME + '\r\n'  ))
pingChecker(irc.recv(4096))
irc.send(bytes('USER appinventormuBot appinventormuBot appinventormuBot : appinventormuBot IRC\r\n'  ))
pingChecker(irc.recv(4096))
irc.send(bytes('msg NickServ identify ' + BOT_PASSWORD + " \r\n"  ))
pingChecker(irc.recv(4096))
irc.send(bytes('JOIN ' + BOT_IRC_CHANNEL + '\r\n'  ))
pingChecker(irc.recv(4096))
irc.send(bytes('NICKSERV  identify ' + BOT_NICKNAME+' '+BOT_PASSWORD+ '\r\n'  ))

directory = "C:\\irc"
if not os.path.exists(directory):
	os.makedirs(directory)
target = open(os.path.join(directory,"file.txt"), 'w')
#/sdcar/folder/file.py for android remove the join etc


#.........................................python /bb.py
while 1:
    line = irc.recv(4096)
    print(line)
    pingChecker(line)
    if line.find(bytes('PRIVMSG'  )) != -1 or line.find(bytes('NOTICE'  )) != -1:
        messagechecker(line)
    target.write(line)
	
	
	#if ('wea' in str(message)):
          #  irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +str(message)+ ' ....!\r\n'  ))
		#try:
			#aa= str(message[5:len(str(message))])
			#f = urllib2.urlopen('http://api.wunderground.com/api/'+key+'/geolookup/conditions/q/'+aa+'.json')
			#json_string = f.read()
			#parsed_json = json.loads(json_string)
			#location = parsed_json['location']['city']
			#temp_f = parsed_json['current_observation']['temp_f']
			#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + "Current temperature in %s is: %s%" + (location, temp_f)+'\r\n'  ))
			#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' \/\/\/\/\/\/\/\/ !\r\n'  ))
			#f.close()
		#except:
			#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' invalid command!\r\n'  ))
			#pass		
	
