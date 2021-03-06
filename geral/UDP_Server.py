import socket
from tqdm import tqdm

# IP = socket.gethostbyname(socket.gethostname())
IP = '192.168.202.4'
PORT = 4455
ADDR = (IP, PORT)
SIZE = 256
FORMAT = 'utf-8'
BLOCKS = 0

def main():

    # cria socket UDP
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDR)
    server.settimeout(4.0)
    print('[+] Waiting connection...')

    data, addr = server.recvfrom(SIZE)
    print(f"Recebi {data} de {addr}")
    prev = data.decode(FORMAT)
    item = prev.split("_")
    FILENAME = item[0]
    FILESIZE = int(item[1])
    server.sendto(b'Filename received', addr)

    bar = tqdm(range(FILESIZE), f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(f'recv_{FILENAME}', 'w') as f:
        while True:
            data, addr = server.recvfrom(SIZE)
            
            if not data or data.decode(FORMAT) == 'F':
                server.sendto(b"Finish", addr)
                break

            f.write(data.decode(FORMAT))
            server.sendto(b"Data received", addr)
            BLOCKS = BLOCKS + 1
            bar.update(len(data))

    server.close()

if __name__ == '__main__':
    main()
    print(f"No Blocks received: {BLOCKS}")
