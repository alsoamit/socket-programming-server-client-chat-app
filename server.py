from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(200000)
print("PRIVATE CHAT STARTED WITH YOUR MOBILE")
while 1:
    connectionSocket, addr = serverSocket.accept()
    msg = connectionSocket.recv(1024)
    msg = msg.decode('utf8')
    print("INBOX: ", msg)
    reply = bytes(input("Reply: "), encoding= 'utf8')
    connectionSocket.send(reply)
connectionSocket.close()


