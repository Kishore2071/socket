import socket

HOST=''
PORT=3074

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen()
while(True):
    conn, addr= s.accept()
    print("IP {} connected\n".format(addr[0]))
    conn.sendall(b"Hello World")
    conn.close()
s.close()