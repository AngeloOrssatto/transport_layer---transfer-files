import socket

HOST = 'localhost'
PORT = 50000

# cria socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST, PORT))

for i in range (0, 10):
    tcp_socket.sendall(str.encode(' '))
    data = tcp_socket.recv(1024)
    print(data.decode())
    if not data:
        pass