import socket

host = '10.5.0.211'
port = 9750

cli_sock = socket.socket()
cli_sock.connect((host, port))

msg = input(" -> ")

while msg.lower().strip() != 'bye':
    cli_sock.send(msg.encode())
    data = cli_sock.recv(1024).decode()

    print("from server: " +str(data))

    msg = input(" => ")

cli_sock.close()                   