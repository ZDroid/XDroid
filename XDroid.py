#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# The most stupid IRC bot
#

import socket
from time import ctime
import feedparser

# Config
# ------

server = "irc.freenode.net"
channel = "#zdroid"
nick = "XDroid"

# Connect to server
# -----------------

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
irc.send("USER " + nick + " " + nick + " " + nick + " :$\n")
irc.send("NICK " + nick + "\n")
irc.send("JOIN " + channel + "\n")

# Stupid functions
# ----------------

while 1:
  msg = irc.recv(2048).strip("\n\r")
  print(msg)

  if msg.find("PING :") != -1:
    irc.send("PONG :pingis\n")

  if msg.find("+hello") != -1:
    irc.send("PRIVMSG " + channel + " :Hello guys!\n")

  if msg.find("+time") != -1:
    irc.send("PRIVMSG " + channel + " :It's " + ctime() + "\n")

  if msg.find("+place") != -1:
    irc.send("PRIVMSG " + channel + " :Droid land\n")

  if msg.find("+pi") != -1:
    irc.send("PRIVMSG " + channel + " :3.14159265359\n")

  if msg.find("+nuke") != -1:
    irc.send("NOTICE " + channel + " :Nuclear bomb is falling down!\n")

  if msg.find("+tux") != -1:
    irc.send("PRIVMSG " + channel + " :    .--.\n")
    irc.send("PRIVMSG " + channel + " :   |o o |\n")
    irc.send("PRIVMSG " + channel + " :   |:_/ |\n")
    irc.send("PRIVMSG " + channel + " :  //   \ \ \n")
    irc.send("PRIVMSG " + channel + " : (|     | )\n")
    irc.send("PRIVMSG " + channel + " :/'\     /'\ \n")
    irc.send("PRIVMSG " + channel + " :\___)-(___/\n")

  if msg.find("+verge") != -1:
    url = "http://theverge.com/rss/index.xml"
    for i in range(1,6):
      irc.send("PRIVMSG " + channel + " :The Verge > " +
               feedparser.parse(url)["items"][i].link + "\n")

  if msg.find("+rcn") != -1:
    irc.send("PRIVMSG " + channel + " /quit")
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, 6667))
    irc.send("USER " + nick + " " + nick + " " + nick + " :$\n")
    irc.send("NICK " + nick + "\n")
    irc.send("JOIN " + channel + "\n")