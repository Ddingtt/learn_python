#encoding:utf-8
import  socket
import threading
from queue import  Queue

#本程序在局域网上实现基本的客户与服务器通信功能
#由于传送数据的内容、格式、样例以及模块间接口定义文档还没有出来
#所以这里实现是个人制定的基本传输内容和接口定义的框架
#具体功能等相关定义文档出来后实现


sendQ = Queue()
readQ = Queue()

HOST = 'localhost'
POST = 9998

def read(s):
    while True:
        data = s.recv(1024)
        data = data.decode('utf-8')
        print('Received:',data)
        if data == 'quit':
            break

def send(s):
    while True:
        msg = input()
        s.sendall(bytes(msg,encoding="utf8"))
        if msg == 'quit':
            break



if __name__ == '__main__':
    carname = input('the car name:')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,POST))
    s.send(bytes(carname,'utf-8'))
    msg = s.recv(1024)
    msg = msg.decode('utf-8')
    print(msg)
    if msg == 'Welcome connect!':
        readThr = threading.Thread(target=read,args=(s,))
        sendThr = threading.Thread(target=send,args=(s,))
        readThr.start()
        sendThr.start()

        sendThr.join()
        readThr.join()

    s.close()
