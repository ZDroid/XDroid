#/usr/bin/env python
# -*- coding:utf-8 -*-

# Import some necessary libraries.
import socket, time, feedparser

server = "irc.freenode.net" # Server
channel = "#test" # Channel
botnick = "testbot" # Bot name
def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def time():
  current_time = time.ctime()
  ircsock.send("PRIVMSG "+ channel + " :It is true: " + current_time + "\n")

def place():
  ircsock.send("PRIVMSG "+ channel + " :You are in Linux galaxy \n")

def chrv():
  ircsock.send("PRIVMSG "+ channel + " :Latest version od Chrome/Chromium is 24 \n")

def ffv():
  ircsock.send("PRIVMSG "+ channel + " :Latest version of Firefox is 17.0 \n")

def ubuntuv():
  ircsock.send("PRIVMSG "+ channel + " :Latest version of Ubuntu is 12.10 - Quantal Quetzal \n")

def slackv():
  ircsock.send("PRIVMSG "+ channel + " :Latest version of Slackware is 14.0 \n")

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
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Test bot\n")
ircsock.send("NICK "+ botnick +"\n") 

joinchan(channel) # Join the channel using the functions we previously defined


while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # recieve data from server
  ircmsg = ircmsg.strip('\n\r') # removes unnecessary line brakes
  print(ircmsg) # This is output from server!

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

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()

  if ircmsg.find("!quit " + botnick) != -1: # if the server pings us then we've got to respond!
    try:
        ircsock.quit()
    except:
        print("XDroid leave")

  if ircmsg.find("!reconnect " + botnick) != -1: # if the server pings us then we've got to respond!
    try:
        ircsock.quit()
    except:
        pass
    
    ircsock.send("PRIVMSG "+ channel + " /quit")
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, 8001)) # Here we connect to the server using the port 6667
    ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Test bot.\n")
    ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot
    joinchan(channel) # Join the channel using the functions we previously defined