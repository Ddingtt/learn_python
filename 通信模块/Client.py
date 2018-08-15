#!/user/bin/env python
# _*_ coding:utf-8 _*_

from socket import *

from pip._vendor.distlib.compat import raw_input

def clientSocket():
    HOST = 'localhost'
    PORT = 12345
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    while True:
        data = raw_input('发出客户端指令:')
        print('waiting...')
        if not data:
            break
        tcpCliSock.send(data.encode('utf-8'))
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data)
    tcpCliSock.close()

def main():
    clientSocket()

if __name__ == '__main__':
    main()