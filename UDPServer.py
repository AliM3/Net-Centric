#UDPServer.py

from socket import socket, SOCK_DGRAM, AF_INET

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print ("Waiting for connections")
while True:
    # Receive the client packet along with the address it is coming from
    raw_message, address = serverSocket.recvfrom(2048)
    message=raw_message.decode()
    # Capitalize the message from the client
    print (message, address)
    message = message.upper()
    serverSocket.sendto(message.encode(), address)
serverSocket.close()
