import socket
import time

HOST = '10.88.204.26'
PORT = 50000
BUFFERSIZE = 1024

# cria socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((HOST, PORT))

# inicia escuta para conexoes
# udp_socket.listen()
print('Aguardando conexão')

# conn, addr = udp_socket.accept()
# print('Conectado em', addr)

data = 'Enviando uma mensagem '

# for i in range (0, 10):
#     print(data + str(i))
mean = 0

bytesAddressPair = udp_socket.recvfrom(BUFFERSIZE)
address = bytesAddressPair[1]

for i in range (0, 10):
    # data = conn.recv(1024) # 1024 bytes serao recebidos na conexao 
    begin = time.perf_counter_ns()
    
    udp_socket.sendto(str.encode(data + str(i)), address)
    end = time.perf_counter_ns()
    print('Duração', i, (end-begin), 'ns')
    mean += (end-begin)
# conn.send(str.encode(data + str(1)))
# conn.send(str.encode(data + str(2)))

print('Media:', mean/10, 'ns')
