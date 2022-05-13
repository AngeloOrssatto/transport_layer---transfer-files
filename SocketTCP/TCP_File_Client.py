import socket
import time
import os
 
IP = socket.gethostbyname(socket.gethostname())
# IP = '10.88.204.26'
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
 
def main():
    begin = time.perf_counter_ns()
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    """ Connecting to the server. """
    client.connect(ADDR)
 
    """ Opening and reading the file data. """
    file = open("../data.txt", "r")
    data = file.read()
 
    """ Sending the filename to the server. """
    client.send("data.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
 
    """ Sending the file data to the server. """
    client.sendall(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    file_size = os.path.getsize('../data.txt')
    print('File size:', file_size, 'bytes')
 
    """ Closing the file. """
    file.close()
 
    """ Closing the connection from the server. """
    client.close()
    end = time.perf_counter_ns()
    print('Execution time:', (end-begin), 'ns')
 
 
if __name__ == "__main__":
    for i in range (0, 10):
        main()