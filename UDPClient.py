#UDPClient.py

from socket import socket, SOCK_DGRAM, AF_INET

serverName = 'localhost'
serverPort = 8888
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, addr = clientSocket.recvfrom(2048)
print (modifiedMessage.decode(), addr)
clientSocket.close()
