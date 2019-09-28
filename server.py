# import socket
from socket import socket

host = '10.5.0.211'
port = 9750

server_socket = socket()
server_socket.bind((host, port))
server_socket.listen()