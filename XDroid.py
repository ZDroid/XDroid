#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# The most stupid IRC bot
#

import socket
from time import ctime
import feedparser

# Configuration
# -------------

server = "irc.freenode.net"
channel = "#zdroid"
nick = "XDroid"

# Connect to server
# -----------------

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, 6667))
irc.send("USER " + nick + " " + nick + " " + nick + " :" + nick + "\n")
irc.send("NICK :" + nick + "\n")
irc.send("JOIN :" + channel + "\n")

# Commands
# --------

while 1:
  msg = irc.recv(2048).strip("\n\r")
  print(msg)

  if msg.find("PING :") != -1:
    irc.send("PONG :pingis\n")

  if msg.find("+hi") != -1:
    irc.send("PRIVMSG " + channel + " :Hi!\n")

  if msg.find("+time") != -1:
    irc.send("PRIVMSG " + channel + " :It's " + ctime() + ".\n")

  if msg.find("+channel") != -1:
    irc.send("PRIVMSG " + channel + " :We're on " + channel + ".\n")

  if msg.find("+pi") != -1:
    irc.send("PRIVMSG " + channel + " :The value of pi is 3.14159265359.\n")

  if msg.find("+note") != -1:
    irc.send("NOTICE " + channel + " :Something failed. Sorry.\n")

  if msg.find("+tux") != -1:
    irc.send("PRIVMSG " + channel + " :    .--.\n")
    irc.send("PRIVMSG " + channel + " :   |o o |\n")
    irc.send("PRIVMSG " + channel + " :   |:_/ |\n")
    irc.send("PRIVMSG " + channel + " :  //   \ \ \n")
    irc.send("PRIVMSG " + channel + " : (|     | )\n")
    irc.send("PRIVMSG " + channel + " :/^\     /^\ \n")
    irc.send("PRIVMSG " + channel + " :\___)-(___/\n")

  if msg.find("+feed") != -1:
    url = "http://zdroid.roon.io/feed"
    for i in range(1,5):
      irc.send("PRIVMSG " + channel + " :" +
               feedparser.parse(url)["items"][i].title + " " +
               feedparser.parse(url)["items"][i].link + "\n")

  if msg.find("+quit") != -1:
    irc.send("QUIT\n")
    exit()

  if msg.find("+rcn") != -1:
    irc.send("QUIT\n")
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, 6667))
    irc.send("USER " + nick + " " + nick + " " + nick + " :" + nick + "\n")
    irc.send("NICK :" + nick + "\n")
    irc.send("JOIN :" + channel + "\n")