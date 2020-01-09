from socket import*

def main():
    # import socket module
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverHost = 'localhost'

    recvBuffer = 1024

    serverPort = 8888

    serverSocket.bind(('', serverPort))

    serverSocket.listen(1)

    while True:
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024)

            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i])
            connectionSocket.close()
        except IOError:
            serverSocket.close()
    pass
if __name__ == '__main__':
    main()