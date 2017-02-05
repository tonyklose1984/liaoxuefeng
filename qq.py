import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("127.0.0.1",8000))
sock.listen(3)
print("this is socket_server")
con,add = sock.accept()
print("%s:%s is connent"%add)
while True:
    print(con.recv(512))
    con.send(raw_input(">>>"))
sock.close()
