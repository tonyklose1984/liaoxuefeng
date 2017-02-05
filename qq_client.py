#coding:utf-8
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("127.0.0.1",8000))
print("this is client")
while True:
    sock.send(raw_input(">>>"))
    print(sock.recv(512))
sock.close()

