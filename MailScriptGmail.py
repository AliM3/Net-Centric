#!/usr/bin/python

import socket
import time
import sys

def send_wait(msg):
    if msg != None:
        print(msg)
        print(msg, file=sys.stderr)

    time.sleep(2)

def send(msg):
    print(msg)
    print(msg, file=sys.stderr)

if len(sys.argv) < 3:
    print ("Usage: MailScriptGmail.py username host | telnet")
    sys.exit()

serverName = 'aspmx.l.google.com' #This server only sends to gmail accounts
serverPort = 25

print ("open " + serverName + " 25")
time.sleep(2)

send_wait(None)

clientName = sys.argv[1]
userName=sys.argv[1]
userServer=sys.argv[2]
#toName="bytesizebook"
#toServer="gmail.com"
toName="amoha093"
toServer="fiu.edu"

#Send HELO command and print (server response.)
heloCommand='EHLO %s' % clientName
send_wait(heloCommand)
#Send MAIL FROM command and print (server response.)
fromCommand='MAIL FROM: <%s@%s>' % (userName, userServer)
recvFrom = send_wait(fromCommand)
#Send RCPT TO command and print (server response.)
rcptCommand='RCPT TO: <%s@%s>' % (toName, toServer)
recvRcpt = send_wait(rcptCommand)
#Send DATA command and print (server response.)
dataCommand='DATA'
dataRcpt = send_wait(dataCommand)
#Send message data.
send("Date: %s" % time.strftime("%a, %d %b %Y %H:%M:%S -0400", time.localtime()));
send("From: Tim Downey <%s@%s>" % (userName, userServer));
send("Subject: Simple Mail Message");
send("To: %s@%s" % (toName, toServer));
send(""); #End of headers
send("Hello World");
send("Hola Mundo");
send("gmail script");
#Message ends with a single period.
send_wait(".")
#Send QUIT command and get server response.
quitCommand='QUIT'
quitRcpt = send_wait(quitCommand)
