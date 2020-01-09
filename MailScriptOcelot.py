#!/usr/bin/python

#pipe the output of this command into telnet

import socket
import time, sys

#for scripting, the socket is not used. Telnet controls the socket.
def send_recv(socket, msg, code):
    if msg != None:
        print(msg)
        print(msg, file=sys.stderr)

    time.sleep(2)

    return 1

def send(socket, msg):
    print(msg)
    print(msg, file=sys.stderr)

print ("open smtp.cs.fiu.edu 25")
time.sleep(2)


serverName = 'smtp.cs.fiu.edu' #This server only works from ocelot
serverPort = 8888

clientSocket = 0;
recv=send_recv(clientSocket, None, '220')

clientName = 'ali'
userName="amoha093"
userServer="cs.fiu.edu"
toName="amoha093"
toServer="fiu.edu"
#Send HELO command and print (server response.)
heloCommand='EHLO %s' % clientName
recvFrom = send_recv(clientSocket, heloCommand, '250')
#Send MAIL FROM command and print (server response.)
fromCommand='MAIL FROM: <%s@%s>' % (userName, userServer)
recvFrom = send_recv(clientSocket, fromCommand, '250')
#Send RCPT TO command and print (server response.)
rcptCommand='RCPT TO: <%s@%s>' % (toName, toServer)
recvRcpt = send_recv(clientSocket, rcptCommand, '250')
#Send DATA command and print (server response.)
dataCommand='DATA'
dataRcpt = send_recv(clientSocket, dataCommand, '354')
#Send message data.
send(clientSocket, "Date: %s" % time.strftime("%a, %d %b %Y %H:%M:%S -0400", time.localtime()));
send(clientSocket, "From: Ali Mohammad <%s@%s>" % (userName, userServer));
send(clientSocket, "Subject: Simple Mail Message");
send(clientSocket, "To: %s@%s" % (toName, toServer));
send(clientSocket, ""); #End of headers
send(clientSocket, "Hello World");
send(clientSocket, "Hola Mundo");
send(clientSocket, "ocelot script");
#Message ends with a single period.
send_recv(clientSocket, ".", '250');
#Send QUIT command and get server response.
quitCommand='QUIT'
quitRcpt = send_recv(clientSocket, quitCommand, '221')
