#/usr/bin/env python
# -*- coding:utf-8 -*-

import socket, time, feedparser

server = "irc.freenode.net" # Server
channel = "#botwar" # Kanal
botnick = "SXDroid" # Naziv bota

def ping():
  ircsock.send("PONG :pingis\n")

def sendmsg(chan , msg):
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan):
  ircsock.send("JOIN "+ chan +"\n")

def hello():
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def vreme():
  trenutno_vreme = time.ctime()
  ircsock.send("PRIVMSG "+ channel + " :Tačno je: " + trenutno_vreme + "\n")

def mesto():
  ircsock.send("PRIVMSG "+ channel + " :Vi ste u laboratoriji \n")

def planete():
  ircsock.send("PRIVMSG "+ channel + " :Nebeska tela koja se kreću eliptičnom putanjom oko zvezda - u Sunčevom sistemu su to Merkur, Venera, Zemlja, Mars, Jupiter, Saturn, Uran i Neptun; patuljaste planete: Pluton i Ksena \n")

def mape():
  ircsock.send("PRIVMSG "+ channel + " :Najbolje mape → http://maps.google.com \n")

def carstva():
  ircsock.send("PRIVMSG "+ channel + " :Carstva živih bića - monere, protisti, gljive, biljke i životinje \n")

def komande():
  ircsock.send("PRIVMSG "+ channel + " :vreme, mesto, planete, mape, carstva, komande, scidb, phys \n")

def scidb():
  ircsock.send("PRIVMSG "+ channel + " : |==========| \n")
  ircsock.send("PRIVMSG "+ channel + " : |=#3====?s=| \n")
  ircsock.send("PRIVMSG "+ channel + " : |====nauka=| \n")
  ircsock.send("PRIVMSG "+ channel + " : |==$var====| \n")
  ircsock.send("PRIVMSG "+ channel + " : |=%h===(8)=| \n")
  ircsock.send("PRIVMSG "+ channel + " : |==========| \n")

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :SXDroid\n")
ircsock.send("NICK "+ botnick +"\n") 

joinchan(channel)

while 1:
  ircmsg = ircsock.recv(2048)
  ircmsg = ircmsg.strip('\n\r')
  print(ircmsg)

  if ircmsg.find(":Hello "+ botnick) != -1: 
    hello()

  elif ircmsg.find("#phys") != -1:
        url="http://phys.org/rss-feed/"
        feed = feedparser.parse(url)
        for i in range(1,6):
                news=feed['items'][i].title + ' Link: ' + feed['items'][i].link
                ircsock.send("PRIVMSG "+ channel + " :~Phys: " + news + "\n")

  elif ircmsg.find("#komande") != -1:
    komande()

  elif ircmsg.find("#planete") != -1:
    planete()

  elif ircmsg.find("#scidb") != -1:
    scidb()

  elif ircmsg.find("#carstva") != -1:
    carstva()

  elif ircmsg.find("#mape") != -1:
    mape()

  elif ircmsg.find("#mesto") != -1:
    mesto()

  if ircmsg.find("#vreme") != -1:
    vreme()

  if ircmsg.find("PING :") != -1:
    ping()

  if ircmsg.find("!quit " + botnick) != -1:
    try:
        ircsock.quit()
    except:
        print("Ode SXDroid")

  if ircmsg.find("!reconnect " + botnick) != -1:
    try:
        ircsock.quit()
    except:
        pass

    ircsock.send("PRIVMSG "+ channel + " /quit")
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, 8001))
    ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :SXDroid \n")
    ircsock.send("NICK "+ botnick +"\n")
    joinchan(channel)
