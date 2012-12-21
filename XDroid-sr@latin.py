#/usr/bin/env python
# -*- coding:utf-8 -*-

# Uvozi neke neophodne biblioteke.
import socket, time, feedparser

server = "irc.freenode.net" # Server
channel = "#test" # Kanal
botnick = "testbot" # Naziv bota
def ping(): # Ovo je naša prva funkcija! Ona će odgovoriti serverskim Ping-ovima.
  ircsock.send("PONG :pingis\n")

def sendmsg(chan , msg): # Ovo je the funkcija slanja poruka, ona jednostavno šalje poruke na kanal.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")

def joinchan(chan): # Ova funkcija se koristi za pridružavanje kanalima.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # Ova funkcija odgovara korisniku koji unosi "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def vreme():
  trenutno_vreme = time.ctime()
  ircsock.send("PRIVMSG "+ channel + " :Tačno je: " + trenutno_vreme + "\n")

def mesto():
  ircsock.send("PRIVMSG "+ channel + " :Vi ste u Linux galaksiji \n")

def chrv():
  ircsock.send("PRIVMSG "+ channel + " :Poslednja verzija Chroma/Chromiuma je 24 \n")

def ffv():
  ircsock.send("PRIVMSG "+ channel + " :Poslednja verzija Firefoxa je 17.0 \n")

def ubuntuv():
  ircsock.send("PRIVMSG "+ channel + " :Poslednja verzija Ubuntu-a je 12.10 - Quantal Quetzal \n")

def slackv():
  ircsock.send("PRIVMSG "+ channel + " :Poslednja verzija Slackware-a je 14.0 \n")

def root():
  ircsock.send("PRIVMSG "+ channel + " :Super Linux (i Unix) nalog \n")

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

joinchan(channel) # Pridruži se kanalu korišćenjem funkcija koje smo prethodno definisali


while 1: # Budite pažljivi sa ovim! To Vas može poslati u beskonačnu rutu
  ircmsg = ircsock.recv(2048) # Prima podatke sa servera
  ircmsg = ircmsg.strip('\n\r') # Sklanja nepotrebne linijske preseke
  print(ircmsg) # Ovo je output sa servera!

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

  elif ircmsg.find("#mesto") != -1:
    mesto()

  if ircmsg.find("#vreme") != -1:
    vreme()

  if ircmsg.find("PING :") != -1: # Ako server ping-uje nas onda moramo da odgovorimo!
    ping()

  if ircmsg.find("!quit " + botnick) != -1: # Ako server ping-uje nas onda moramo da odgovorimo!
    try:
        ircsock.quit()
    except:
        print("Ode XDroid")

  if ircmsg.find("!reconnect " + botnick) != -1: # Ako server ping-uje nas onda moramo da odgovorimo!
    try:
        ircsock.quit()
    except:
        pass
    
    ircsock.send("PRIVMSG "+ channel + " /quit")
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server, 8001)) # Ovde se povezujemo na server korišćenjem porta 8001
    ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :XDroid \n")
    ircsock.send("NICK "+ botnick +"\n") # Ovde ćemo stvarno dodeliti nick botu
    joinchan(channel) # Pridruži se kanalu korišćenjem funkcija koje smo prethodno definisali
