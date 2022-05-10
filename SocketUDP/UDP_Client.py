import socket

HOST = '10.88.204.26'
PORT = 50000

# cria socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# udp_socket.connect((HOST, PORT))

for i in range (0, 10):
    udp_socket.sendto(str.encode(' '), (HOST, PORT))
    data = udp_socket.recvfrom(1024)
    print(data)
    if not data:
        pass