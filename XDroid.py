#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# The most stupid IRC bot
#

import socket
import time
from math import pi
import feedparser

# Config
# ------

server = "irc.freenode.net" # Server
channel = "#zdroid" # Channel
botnick = "XDroid" # Bot's name

# Stupid setup functions
# ----------------------

# Send message to the channel
def sendmsg(chan, msg):
  irc.send("PRIVMSG "+ chan +" :"+ msg +"\n")

# Join the channel
def joinchan(chan):
  irc.send("JOIN "+ chan +"\n")

# Connect to server
# -----------------

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :$\n")
irc.send("NICK "+ botnick +"\n")
joinchan(channel)

# Stupid functions
# ----------------

while 1:
  msg = irc.recv(2048)
  msg = msg.strip("\n\r")
  print(msg)

  if msg.find("PING :") != -1:
    irc.send("PONG :pingis\n")

  if msg.find("+hello") != -1:
    irc.send("PRIVMSG "+ channel +" :Hello guys!\n")

  if msg.find("+time") != -1:
    irc.send("PRIVMSG "+ channel +" :It's " + time.ctime() + "\n")

  if msg.find("+place") != -1:
    irc.send("PRIVMSG "+ channel +" :I don't know\n")

  if msg.find("+pi") != -1:
    irc.send("PRIVMSG "+ channel +" :3.14159265359\n")

  if msg.find("+tux") != -1:
    irc.send("PRIVMSG "+ channel + " :    .--.\n")
    irc.send("PRIVMSG "+ channel + " :   |o_o |\n")
    irc.send("PRIVMSG "+ channel + " :   |:_/ |\n")
    irc.send("PRIVMSG "+ channel + " :  //   \ \ \n")
    irc.send("PRIVMSG "+ channel + " : (|     | )\n")
    irc.send("PRIVMSG "+ channel + " :/'\_   _/`\ \n")
    irc.send("PRIVMSG "+ channel + " :\___)=(___/\n")

  if msg.find("+verge") != -1:
    url="http://theverge.com/rss/index.xml"
    feed = feedparser.parse(url)
    for i in range(1,6):
      news=feed["items"][i].link
      irc.send("PRIVMSG "+ channel +" :The Verge ~ " + news +"\n")

  if msg.find("+rcn") != -1:
    try:
      irc.quit()
    except:
      pass
    irc.send("PRIVMSG "+ channel + " /quit")
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, 6667))
    irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :$\n")
    irc.send("NICK "+ botnick +"\n")
    joinchan(channel)
