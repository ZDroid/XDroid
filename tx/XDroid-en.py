#/usr/bin/env python
# -*- coding:utf-8 -*-

import socket, time, feedparser

server = "irc.freenode.net" # Server
channel = "#botwar" # Channel
botnick = "XDroid" # Bot name
def ping():
  ircsock.send("PONG :pingis\n")

def sendmsg(chan , msg):
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan):
  ircsock.send("JOIN "+ chan +"\n")

def hello():
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def time():
  current_time = time.ctime()
  ircsock.send("PRIVMSG "+ channel + " :It's true: " + current_time + "\n")

def place():
  ircsock.send("PRIVMSG "+ channel + " :You are in GNU/Linux galaxy \n")

def chrv():
  ircsock.send("PRIVMSG "+ channel + " :Latest version od Chrome/Chromium is 25 \n")

def ffv():
  ircsock.send("PRIVMSG "+ channel + " :Latest version of Firefox is 19 \n")

def ubuntuv():
  ircsock.send("PRIVMSG "+ channel + " :Latest version of Ubuntu is 12.10 - Quantal Quetzal \n")

def slackv():
  ircsock.send("PRIVMSG "+ channel + " :Latest version of Slackware is 14.00 \n")

def root():
  ircsock.send("PRIVMSG "+ channel + " :Super Linux (and Unix) account \n")

def tux():
  ircsock.send("PRIVMSG "+ channel + " :    .--. \n")
  ircsock.send("PRIVMSG "+ channel + " :   |o_o | \n")
  ircsock.send("PRIVMSG "+ channel + " :   |:_/ | \n")
  ircsock.send("PRIVMSG "+ channel + " :  //   \ \ \n")
  ircsock.send("PRIVMSG "+ channel + " : (|     | ) \n")
  ircsock.send("PRIVMSG "+ channel + " :/'\_   _/`\ \n")
  ircsock.send("PRIVMSG "+ channel + " :\___)=(___/ \n")

def phone():
  ircsock.send("PRIVMSG "+ channel + " : _ _ _ _ _ _  \n")
  ircsock.send("PRIVMSG "+ channel + " :| _________ | \n")
  ircsock.send("PRIVMSG "+ channel + " :||         || \n")
  ircsock.send("PRIVMSG "+ channel + " :||  PHONE  || \n")
  ircsock.send("PRIVMSG "+ channel + " :||         || \n")
  ircsock.send("PRIVMSG "+ channel + " :| ¯¯¯¯¯¯¯¯¯ | \n")
  ircsock.send("PRIVMSG "+ channel + " :| 1   2   3 | \n")
  ircsock.send("PRIVMSG "+ channel + " :| 4   5   6 | \n")
  ircsock.send("PRIVMSG "+ channel + " :| 7   8   9 | \n")
  ircsock.send("PRIVMSG "+ channel + " :| *   0   # | \n")
  ircsock.send("PRIVMSG "+ channel + " :|           | \n")
  ircsock.send("PRIVMSG "+ channel + " : ¯ ¯ ¯ ¯ ¯ ¯   \n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :#\n")
ircsock.send("NICK "+ botnick +"\n") 

joinchan(channel)


while 1:
  ircmsg = ircsock.recv(2048)
  ircmsg = ircmsg.strip('\n\r')
  print(ircmsg)

  if ircmsg.find(":Hello "+ botnick) != -1: 
    hello()

  elif ircmsg.find("#shell-fu") != -1:
        url="http://feeds.feedburner.com/Shell-fu"
        feed = feedparser.parse(url)
        for i in range(1,6):
                news=feed['items'][i].title + ' Link: ' + feed['items'][i].link
                ircsock.send("PRIVMSG "+ channel + " :~Shell-fu: " + news + "\n")

  elif ircmsg.find("#chrv") != -1:
    chrv()

  elif ircmsg.find("#tux") != -1:
    tux()
    
  elif ircmsg.find("#phone") != -1:
    phone()

  elif ircmsg.find("#root") != -1:
    root()

  elif ircmsg.find("#slackv") != -1:
    slackv()

  elif ircmsg.find("#ffv") != -1:
    ffv()

  elif ircmsg.find("#place") != -1:
    mesto()

  if ircmsg.find("#time") != -1:
    vreme()

  if ircmsg.find("PING :") != -1:
    ping()

  if ircmsg.find("!quit " + botnick) != -1:
    try:
        ircsock.quit()
    except:
        print("XDroid left")

  if ircmsg.find("!reconnect " + botnick) != -1:
    try:
        ircsock.quit()
    except:
        pass
    
    ircsock.send("PRIVMSG "+ channel + " /quit")
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, 8001))
    ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :XDroid\n")
    ircsock.send("NICK "+ botnick +"\n")
    joinchan(channel)
