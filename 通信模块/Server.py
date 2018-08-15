#!/user/bin/env python
# _*_ coding:utf-8 _*_

import sys
from socket import *
from time import ctime

from pip._vendor.distlib.compat import raw_input


def serverSocket():
    HOST = 'localhost'
    PORT = 12345
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print('waiting for connection...')
        tcpCliSock, address = tcpSerSock.accept()

        print('connected from', address)

        while True:
            data = raw_input('发出服务器指令:')
            print('waiting...')
            recvData = tcpCliSock.recv(BUFSIZ)
            if not recvData:
                print('no found data')
                break
            tcpCliSock.send(('[%s] (%s| %s)' % (ctime(), recvData, data)).encode('utf-8'))
        tcpCliSock.close()
    #tcpSerSock.close()

def main():
    serverSocket()

if __name__ == '__main__':
    main()