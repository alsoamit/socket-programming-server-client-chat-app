from socket import *
serverName = '25.224.131.236'
serverPort = 12000
while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    reply = bytes(input("REPLY: "), encoding='utf8')
    clientSocket.send(reply)
    msg = clientSocket.recv(1024)
    msg = msg.decode("utf8")
    print("MSG: ", msg)
    clientSocket.close()
