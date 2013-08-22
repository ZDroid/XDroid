#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# The most stupid IRC bot
#

import socket
import time
import feedparser

# Config
# ------

server  = "irc.freenode.net" # Server
channel = "#zdroid" # Channel
botnick = "XDroid" # Bot's name

# Stupid setup functions
# ----------------------

# Send message to the channel

def sendmsg(chan, msg):
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

# Join the channel

def joinchan(chan):
  ircsock.send("JOIN "+ chan +"\n")

# Connect to server
# -----------------

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :$\n")
ircsock.send("NICK "+ botnick +"\n")
joinchan(channel)

# Stupid functions
# ----------------

while 1:
  ircmsg = ircsock.recv(2048)
  ircmsg = ircmsg.strip("\n\r")
  print(ircmsg)

  if ircmsg.find("+hello") != -1: 
    ircsock.send("PRIVMSG "+ channel +" :Hello guys!\n")

  if ircmsg.find("+verge") != -1:
    url="http://www.theverge.com/rss/index.xml"
    feed = feedparser.parse(url)
    for i in range(1,6):
      news=feed["items"][i].link
      ircsock.send("PRIVMSG "+ channel +" :The Verge ~ " + news +"\n")

  if ircmsg.find("+place") != -1:
    ircsock.send("PRIVMSG "+ channel +" :I don't know\n")

  if ircmsg.find("+time") != -1:
    ircsock.send("PRIVMSG "+ channel +" :It's " + time.ctime() + "\n")

  if ircmsg.find("+tux") != -1:
    ircsock.send("PRIVMSG "+ channel + " :    .--.\n")
    ircsock.send("PRIVMSG "+ channel + " :   |o_o |\n")
    ircsock.send("PRIVMSG "+ channel + " :   |:_/ |\n")
    ircsock.send("PRIVMSG "+ channel + " :  //   \ \ \n")
    ircsock.send("PRIVMSG "+ channel + " : (|     | )\n")
    ircsock.send("PRIVMSG "+ channel + " :/'\_   _/`\ \n")
    ircsock.send("PRIVMSG "+ channel + " :\___)=(___/\n")

  if ircmsg.find("PING :") != -1:
    ircsock.send("PONG :pingis\n")

  # ------------------
  # *quit doesn't work
  # ------------------

  # Reconnect the bot

  if ircmsg.find("+rcn") != -1:
    try:
      ircsock.quit()
    except:
      pass

    ircsock.send("PRIVMSG "+ channel + " /quit")
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, 6667))
    ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :XDroid\n")
    ircsock.send("NICK "+ botnick +"\n")
    joinchan(channel)
