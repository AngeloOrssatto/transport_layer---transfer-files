import socket
import time

HOST = 'localhost'
PORT = 50000

# cria socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST, PORT))

# inicia escuta para conexoes
tcp_socket.listen()
print('Aguardando conexão')

conn, addr = tcp_socket.accept()
print('Conectado em', addr)

data = 'Enviando uma mensagem '

# for i in range (0, 10):
#     print(data + str(i))
mean = 0

for i in range (0, 10):
    # data = conn.recv(1024) # 1024 bytes serao recebidos na conexao 
    begin = time.perf_counter_ns()
    h = conn.recv(1024)
    conn.sendall(str.encode(data + str(i)))
    end = time.perf_counter_ns()
    print('Duração', i, (end-begin), 'ns')
    mean += (end-begin)
# conn.send(str.encode(data + str(1)))
# conn.send(str.encode(data + str(2)))

print('Media:', mean/10, 'ns')
conn.close()