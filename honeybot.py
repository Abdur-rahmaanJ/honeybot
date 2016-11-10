

__author__ = 'me'

#mute removed
#My first messing-up with python. Code in progress. Here only for checking. 
#Honeybot's disparities in code style is because of a trying out of Python
#see the features in the honeybotfeatures.txt 
from tkinter import*


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

import _thread
import socket
import time
import os

import urllib.request
import json

import random
import math

localtime = time.asctime( time.localtime(time.time()) )
key='65d4b4eabf8b06d5'

BOT_IRC_SERVER ="chat.freenode.net"
BOT_IRC_CHANNEL = "##bottestingmu"
BOT_IRC_PORT = 6667
BOT_NICKNAME = "appinventormuBot"
BOT_OWNER = "appinventormu"
BOT_PASSWORD = ""

BOT_IRC_CHANNEL2 = "#python"

CHANNELN = "##bottestingmu"
CHANNELPY = "##bottestingmu"

def pingChecker(pingLine):
    if pingLine.find(bytes('PING'  ,'utf8')) != -1:
        pingLine = pingLine.rstrip().split()
        if pingLine[0] == bytes("PING"  ,'utf8'):
            irc.send(bytes("PONG "  ,'utf8') + pingLine[1] + bytes("\r\n"  ,'utf8')  )
            
#................................................................
            

chjcmd = ['joinpy']

brandf = ['.rand']

jpycmd = 'mmm'

PRIV = 'PRIVMSG '

#.........main func..................................................
def messagechecker(msgLine):
	global mute
	mute=False
	completeLine = str(msgLine[1:]).replace("'b",'').split(':', 1)
	info = completeLine[0].split()
	message = (completeLine[1].split("\\r")[0]).replace("'b",'')
	sender = info[0][2:].split("!", 1)[0]
	print("Complete Line-->" + str(completeLine))
	print("Info-->" + str(info))
	print("Message-->" + str(message))
	print("Sender-->" + str(sender) + "\n")

#..............msgs...............................................................................

	
	#.mail myadd youradd sub body pwd
	if(info[2]==BOT_NICKNAME):
		
		if(str(message[0:5]).strip() =='.mail'):
			mute = True
			#emsg = str(message).split('#')
			#fromaddr =str(emsg[1])
			#toaddr = str(emsg[2])
			#thesub = str(emsg[3])
			#thebody = str(emsg[4])
			#thepassword = str(emsg[5])
			try:
				emsg=str(message).split('#')
				#fromaddr='armij7@gmail.com'
				
				print('1')
				fromaddr=str(emsg[1])
				toaddr=str(emsg[2])
				thesub=str(emsg[3])
				thebody=str(emsg[4])
				thepassword=str(emsg[5])
				#toaddr='timeofsands@gmail.com'
				#thesub='subj'
				#thebody='bodyyy'
				#thepassword='apple654321'
				print('2')
				msg = MIMEMultipart('kjhkjhkj')
				print('3')
				msg.set_charset('utf8')
				print('4')
				msg['From'] = fromaddr
				print('5')
				msg['To'] = toaddr
				print('6')
				#msg['Subject'] = Header(body.getAttribute('hum').encode('utf8'),'UTF8').encode()
				msg['Subject'] = Header(thesub,'utf8')
				print('7')
				_attach = MIMEText(thebody.encode('utf8'),'html','UTF-8')
				print('8')
				msg.attach(_attach)
				print('9')
				server = smtplib.SMTP('smtp.gmail.com', 587)
				print('10')
				server.starttls()
				print('11')
				server.login(fromaddr, thepassword)
				print('12')
				text = msg.as_string()
				print('13')
				server.sendmail(fromaddr, toaddr, text)
				print('14')
				server.quit()
				print('15')
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL+' :Hi there, '+str(sender)+' !\r\n','utf8')  )
				print(mute)
				
				
			except:
				irc.send(bytes(PRIV + BOT_IRC_CHANNEL+' :oops, '+str(sender)+' !\r\n','utf8')  )
			
			mute=False
	
	if(str(message[0:5])== '.mute'):
		irc.send(bytes(PRIV+' '+BOT_IRC_CHANNEL+' :\x01ACTION'+' cries and zips his mouth shut\x01\r\n','utf8')  )
		mute=True
		print(mute)
	
	if(str(message[0:7])== '.untalk'):
		irc.send(bytes(PRIV+' '+BOT_IRC_CHANNEL+' :\x01ACTION'+' comes back and unzip his mouth\x01\r\n','utf8')  )
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL+' :mmm ah !\r\n','utf8')  )
		mute=False
		print(mute)
	if mute:
		return False
	
	if (str(message) == "quitplz" and sender =='appinventormu'):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL+' :i have to go !\r\n','utf8')  )
		irc.send(bytes("QUIT :see you soon\r\n",'utf8')  )
		
	
	if(str(message)=='hi'):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL+' :Hi there, '+str(sender)+' !\r\n','utf8')  )
	
	if(str(message) =='whereDoYouLive?'):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL+' :Hi there, '+str(sender)+'i live in my house !\r\n','utf8')  )
	
	if ( str(message) == jpycmd):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :nnn nnn, ' + str(sender) + '!\r\n','utf8'  )  )
	
	swearlist = ['fuck','faggot','fool','sex','buck' ,'shit','dick','ggt','falourmama','liki','zako','pilon','pilnn','tits']
	swearlistr = ' dont swear'
	if any(word in str(message) for word in swearlist):
		irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' dont swear!\r\n','utf8'  )  )
		irc.send(bytes('KICK ' + BOT_IRC_CHANNEL + ' ' + str(sender) +swearlistr+ ' \r\n','utf8'  )  )
	
	lovelist = ['love','sexy','marry','woman']
	lovelistr = ' love that what they think of'
	if any(word in str(message) for word in lovelist):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + lovelistr+ ' \r\n','utf8'  )  )
	
	horsemanlist = ['sword','shield','horse']
	horsemanlistm  = ' yes a spirit of horsemanship is needed'
	horsemanlistm2 = ' ah the feeling of a horse'
	horsemanlistr=''
	if any(word in str(message) for word in horsemanlist):
		hsrand = random.randint(1,2)
		if(hsrand==1):
			horsemanlistr = horsemanlistm
		if(hsrand==2):
			horsemanlistr = horsemanlistm2
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + horsemanlistr + ' \r\n','utf8'  )  )
	
	
	hatemsg = ['i','hate','you']
	hatemsgr = ' mind yourself next time!'
	if all(word in str(message) for word in hatemsg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + hatemsgr+ ' \r\n','utf8'  )  )
	
	addrmsg = ['where','do','you','live']
	addrmsgr = ' i live in my house . . .'
	if all(word in str(message) for word in addrmsg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + addrmsgr+ ' \r\n','utf8'  )  )
	
	howhmsg = ['how','are','you']
	howhmsgr = ' fine and you? . . .'
	if all(word in str(message) for word in howhmsg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + howhmsgr+ ' \r\n','utf8'  )  )
	
	statmsg = ['what','are','you','doing']
	statmsgr = ' oh i\'m talking to you . . .'
	if all(word in str(message) for word in statmsg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + statmsgr+ ' \r\n','utf8'  )  )
	
	sleepmsg = ['are','you','sleeping']
	sleepmsgr = ' if i\'m responding to you. no . . .'
	if all(word in str(message) for word in sleepmsg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + sleepmsgr+ ' \r\n','utf8'  )  )
	
	aslmmsg = ['aslm']
	aslmmsgr = ' wslm'
	if all(word in str(message) for word in aslmmsg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + aslmmsgr+ ' \r\n','utf8'  )  )
	
	aslm2msg = ['assala']
	aslm2msgr = ' wa alaikumus salaam'
	if all(word in str(message) for word in aslm2msg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + aslm2msgr+ ' \r\n','utf8'  )  )
	
	okmsg = ['ok','fine']
	okmsgr = ' good '
	if any(word in str(message) for word in okmsg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' : ' + okmsgr+ ' \r\n','utf8'  )  )
	
	alhmsg = ['alhamdulillah']
	alhmsgr = ' yes indeed praise be to allah . . . الحمد لله '
	if all(word in str(message) for word in alhmsg):
		irc.send(bytes(PRIV + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + alhmsgr+ ' \r\n','utf8'  )  )
	
	if(sender == BOT_OWNER):
		if all(word in str(message) for word in chjcmd ):
			irc.send(bytes('JOIN ' + BOT_IRC_CHANNEL2 + '\r\n','utf8'  )  )
	
	if (str(message[0:4]) == '.wea'):
			try:
				data= message[5:len(message)].strip()
				dsplit = data.split(' ',1)
				if(' ' in str(dsplit[1])):
					stri=dsplit[1]
					strok=stri.replace(' ','_')
					dp2=str(strok)
				else:
					dp2=str(dsplit[1])
				dp1 = str(dsplit[0].strip())
				f=urllib.request.urlopen('http://api.wunderground.com/api/'+key+'/geolookup/conditions/q/'+dp1+'/'+dp2+'.json').read().decode('utf8')
				json_string = f
				parsed_json = json.loads(json_string)
				location = parsed_json['location']['city']
				temp_f = parsed_json['current_observation']['temp_f']
				loca = str(location)
				tampint = float(temp_f)
				convfc1 = tampint - 32
				convfc2 = 0.5556
				convfc3 = math.floor(convfc1 * convfc2)
				tamp =str(convfc3)
				#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL +' '+ "Current temperature in %s is: %s" % (location, temp_f)+ ' \r\n','utf8'))
				irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL +" :Current temperature in "+loca+' is '+tamp+ ' C\r\n','utf8')  )
				f.close()
			except:
				#print(dp1)
				#print(dp2)
				#irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) + ' opps something is bad!\r\n','utf8'  )  )
				pass
	
	if(str(message[0:5]) == '.rand'):
		randdata = (message[6:len(message)])
		rdata = randdata.split()
		try:
			inte1 = int(rdata[0])
			inte2 = int(rdata[1])
			randinteg = random.randint(inte1,inte2)
			randst = str(randinteg)
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' the random num is ' +randst+' !\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' could not perform the rand operation !\r\n','utf8'  )  )
			pass
			
	if(str(message[0:4]) == '.sin'):
		sindata = (message[5:len(message)])
		try:
			sdata = math.sin(float(sindata))
			sdatastr = str(sdata)
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' the sine of '+sindata+' is ' +sdatastr+' !\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' could not perform the sine operation !\r\n','utf8'  )  )
			pass
			
	if(str(message[0:4]) == '.cos'):
		cosdata = (message[5:len(message)])
		try:
			cdata = math.cos(float(cosdata))
			cdatastr = str(cdata)
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' the cosine of '+cosdata+' is ' +cdatastr+' !\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' could not perform the cosine operation !\r\n','utf8'  )  )
			pass
			
	if(str(message[0:4]) == '.sqr'):
		sqrdata = (message[5:len(message)])
		try:
			sqdata = math.sqrt(float(sqrdata))
			sqdatastr = str(sqdata)
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' the square root of '+sqrdata+' is ' +sqdatastr+' !\r\n','utf8'  )  )
		except:
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' :Hey, ' + str(sender) +' could not perform the square root operation !\r\n','utf8'  )  )
			pass
	
	prhouse1 = " _______________________ "
	prhouse2 = "/                       \\"
	prhouse3 = "-------------------------"
	prhouse4 = " |                     | "
	prhouse5 = " |                     | "
	prhouse6 = " |                     | "
	prhouse7 = " |_____________________| "
	prhousem = '.pr house™'
	if(str(message[0:3]) == '.pr'):
		if(message[4:len(message)] == 'house'):
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prhouse1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prhouse2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prhouse3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prhouse4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prhouse5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prhouse6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prhouse7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prhousem+'\r\n','utf8'  )  )
			
	prcar1='   ____________      '
	prcar2='  |            |     '
	prcar3=' __________________  '
	prcar4='|                  \\   '
	prcar5=' --/   \-----/   \---'
	prcar6='    \_/       \_/    '
	prcarm = '.pr car™'
	if(str(message[0:3]) == '.pr'):
		if(message[4:len(message)] == 'car'):
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcar1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcar2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcar3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcar4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcar5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcar6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcarm+'\r\n','utf8'  )  )

		if(message[4:len(message)] == 'chequered'):
			prchboard1='▒▒▒▒▒▒▒▒▒▒'
			prchboard2='▒▀▄▀▄▀▄▀▄▒'
			prchboard3='▒▀▄▀▄▀▄▀▄▒'
			prchboard4='▒▀▄▀▄▀▄▀▄▒'
			prchboard5='▒▀▄▀▄▀▄▀▄▒'
			prchboard6='▒▒▒▒▒▒▒▒▒▒'
			prchboardm='.pr chequered™'
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prchboard1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prchboard2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prchboard3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prchboard4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prchboard5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prchboard6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prchboardm+'\r\n','utf8'  )  )
		
		if(message[4:len(message)] == 'railway'):
			prrail1= '║▒▒██▒▒▒██▒▒║'
			prrail2= '║▒█████████▒║'
			prrail3= '║▒▒██▒▒▒██▒▒║'
			prrail4= '║▒█████████▒║'
			prrail5= '║▒▒██▒▒▒██▒▒║'
			prrail6= '║▒█████████▒║'
			prrail7= '║▒▒██▒▒▒██▒▒║'
			prrail8= '║▒█████████▒║'
			prrail9= '║▒▒██▒▒▒██▒▒║'
			prrail10='║▒█████████▒║'
			prrail11='║▒▒██▒▒▒██▒▒║'
			prrail12='║▒█████████▒║'
			prrail13='║▒▒██▒▒▒██▒▒║'
			prrailm= '.pr railway™'
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail8+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail9+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail10+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail11+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail12+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrail13+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prrailm+'\r\n','utf8'  )  )
		
		if(message[4:len(message)] == 'coffee'):
			prcoffee1= '▒▒▓░▓▒░▓░▒▒▒▒▒▒▒'
			prcoffee2= '▒░▒▓░▓▓░▒░▒▒▒▒▒▒'
			prcoffee3= '▒▒▒▒▓▒▓▒▒▒▒▒▒▒▒▒'
			prcoffee4= '▒█▓▓▓▓▓▓▓▓▓█▒▒▒▒'
			prcoffee5= '▒█▓▓▓▓▓▓▓▓▓████▒'
			prcoffee6= '▒█▓▓▓▓▓▓▓▓▓█▒▒█▒'
			prcoffee7= '▒█▓▓▓▓▓▓▓▓▓█▒▒█▒'
			prcoffee8= '▒█▓▓▓▓▓▓▓▓▓█▒▒█▒'
			prcoffee9= '▒█▓▓▓▓▓▓▓▓▓████▒'
			prcoffee10='▒███████████▒▒▒▒'
			prcoffee11='▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒'
			prcoffeem= '.pr coffee™'
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee8+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee9+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee10+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffee11+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcoffeem+'\r\n','utf8'  )  )
		
		if(message[4:len(message)] == 'stop'):
			prstop1= ' ╔═════════════════╗'
			prstop2= ' ║            ██████            '
			prstop3= ' ║      ██                 ██'
			prstop4= ' ║██                             ██'
			prstop5= ' ║██    STOP   ██'
			prstop6= ' ║██                             ██'
			prstop7= ' ║      ██                 ██'
			prstop8= ' ║            ██████'
			prstop9= ' ║                  ██                ║'
			prstop10=' ║                  ██                ║'
			prstop11=' ║                  ██                '
			prstop12=' ╚═══════════             ╝'
			prstopm='.pr stop™'
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop8+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop9+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop10+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop11+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstop12+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prstopm+'\r\n','utf8'  )  )
			
		if(message[4:len(message)] == 'barchart'):
			prbar1='↑'
			prbar2='|░░|░░|░░|██|░░'
			prbar3='|░░|░░|░░|██|░░'
			prbar4='|░░|░░|░░|██|██'
			prbar5='|░░|██|░░|██|██'
			prbar6='|░░|██|██|██|██'
			prbar7='|██|██|██|██|██'
			prbar8='----------------------->'
			prbarm='.pr barchart™'
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbar1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbar2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbar3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbar4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbar5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbar6+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbar7+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbar8+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prbarm+'\r\n','utf8'  )  )
		
		if(message[4:len(message)] == 'vehicle'):
			prvehicle1='┌──┐'
			prvehicle2='└⊙─⊙┘'
			prvehiclem='.pr vehicle™'
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prvehicle1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prvehicle2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prvehiclem+'\r\n','utf8'  )  )
			
		if(message[4:len(message)] == 'cake'):
			prcake1='░░░░░░♡'
			prcake= '░░▓▓▓▓▓▓▓▓▓'
			prcake2='░████████████'
			prcake3='°°°°°°°°°°°°°°°°°°°°°°°'
			prcakem='.pr cake™'
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcake1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcake2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcake3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prcakem+'\r\n','utf8'  )  )
			
		if(message[4:len(message)] == 'tank'):
			prtank1='  ┏┓━━━━━'
			prtank2='╔╗╔╗╔╗'
			prtank3='▄▄▄▄▄▄▄▄▄▄▄▄→'
			prtank4='_________'
			prtank5='▼⊙▲⊙▲⊙▼'
			prtankm='.pr tank™'
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prtank1+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prtank2+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prtank3+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prtank4+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prtank5+'\r\n','utf8'  )  )
			irc.send(bytes('PRIVMSG ' + BOT_IRC_CHANNEL + ' : ' +prtankm+'\r\n','utf8'  )  )

#......connect................................................................
irc = socket.socket()

irc.connect((BOT_IRC_SERVER, BOT_IRC_PORT))
irc.recv(4096)
irc.send(bytes('NICK ' + BOT_NICKNAME + '\r\n','utf8'  )  )
pingChecker(irc.recv(4096))
irc.send(bytes('USER appinventormuBot appinventormuBot appinventormuBot : appinventormuBot IRC\r\n','utf8'  )  )
pingChecker(irc.recv(4096))
irc.send(bytes('msg NickServ identify ' + BOT_PASSWORD + " \r\n"  ,'utf8')  )
pingChecker(irc.recv(4096))
irc.send(bytes('JOIN ' + BOT_IRC_CHANNEL + '\r\n','utf8'  )  )
pingChecker(irc.recv(4096))
irc.send(bytes('NICKSERV  identify ' + BOT_NICKNAME+' '+BOT_PASSWORD+ '\r\n','utf8'  )  )


#......file..................................................
directory = "C:\\irc"
if not os.path.exists(directory):
	os.makedirs(directory)
target = open(os.path.join(directory,"file.txt"), 'w')
#/sdcar/folder/file.py for android remove the join etc

#...........................................................

#.......loop.................................................
while 1:
	pass
	line = irc.recv(4096)
	print(line)
	pingChecker(line)
	if line.find(bytes('PRIVMSG' ,'utf8')) != -1 or line.find(bytes('NOTICE'  ,'utf8')) != -1:
		messagechecker(line)
		target.write(str(line))
		target.flush()


#.find -1 means no find
#.rstrip() removes all chars at the end
#.rstr('x') removes all x at end
#.split() splits at white space 
#.split(' ',1) 1 splits at first occurance of ' '
#.count(thing) returns how many times thing occurs in list


