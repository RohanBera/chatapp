# import socket
from socket import socket

host = '10.5.0.211' 
port = 9750

server_socket = socket()
server_socket.bind((host, port))
server_socket.listen()

conn,add = server_socket.accept()
print("Connection from",str(add))
while True:
    data = conn.recv(1024).decode()
    print("From user:",str(data))
    data = input(' -> ')
    conn.send(data.encode())
conn.close()