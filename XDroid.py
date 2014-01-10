#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Pure droid-powered IRC bot
#

import socket
from random import choice
import time
import feedparser

# Configuration
# -------------

# Server
server = "irc.freenode.net"
port = 6667

nick = "XDroid"
password = ""

channel = "#zdroid"
join_delay = 20

# Greetings
greetings = ["Hi!", "Hey!", "\o/", "Yo!", "What's up?", "Sup!"]

# URLs
site = "http://zdroid.github.io"
feed = "http://zdroid.roon.io/feed"

# Server connection
# -----------------

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send("USER " + nick + " " + nick + " " + nick + " :" + nick + "\n")
irc.send("NICK :" + nick + "\n")
if password:
  irc.send("PRIVMSG NickServ :IDENTIFY " + password + "\n")
  time.sleep(join_delay)
irc.send("JOIN :" + channel + "\n")
irc.send("PRIVMSG " + channel + " :" + choice(greetings) + "\n")

# Commands
# --------

while 1:
  msg = irc.recv(4096).strip("\n\r")
  print msg

  # Ping-pong
  if msg.find("PING :") != -1:
    irc.send("PONG :pingis\n")

  if msg.find("+time") != -1:
    irc.send("PRIVMSG " + channel + " :It's " + time.ctime() + ".\n")

  if msg.find("+channel") != -1:
    irc.send("PRIVMSG " + channel + " :We're on " + channel + ".\n")

  if msg.find("+pi") != -1:
    irc.send("PRIVMSG " + channel + " :The value of pi is 3.14159265359.\n")

  if msg.find("+note") != -1:
    irc.send("NOTICE " + channel + " :An error occurred. Sorry.\n")

  if msg.find("+tux") != -1:
    irc.send("PRIVMSG " + channel + " :    .--.\n")
    irc.send("PRIVMSG " + channel + " :   |o o |\n")
    irc.send("PRIVMSG " + channel + " :   |:_/ |\n")
    irc.send("PRIVMSG " + channel + " :  //   \ \ \n")
    irc.send("PRIVMSG " + channel + " : (|     | )\n")
    irc.send("PRIVMSG " + channel + " :/^\     /^\ \n")
    irc.send("PRIVMSG " + channel + " :\_._)-(_._/\n")

  if msg.find("+site") != -1:
    irc.send("PRIVMSG " + channel + " :Check out " + site + "!\n")

  if msg.find("+feed") != -1:
    for i in range(1,5):
        irc.send("PRIVMSG " + channel + " :" +
                 feedparser.parse(feed).entries[i].title + " " +
                 feedparser.parse(feed).entries[i].link + "\n")

  if msg.find("+quit") != -1:
    irc.send("QUIT :Bot died. RIP.\n")
    quit()

  if msg.find("+rcn") != -1:
    irc.send("QUIT :Bot died. RIP.\n")
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect((server, port))
    irc.send("USER " + nick + " " + nick + " " + nick + " :" + nick + "\n")
    irc.send("NICK :" + nick + "\n")
    if password:
      irc.send("PRIVMSG NickServ :IDENTIFY " + password + "\n")
      time.sleep(join_delay)
    irc.send("JOIN :" + channel + "\n")
    irc.send("PRIVMSG " + channel + " :" + choice(greetings) + "\n")