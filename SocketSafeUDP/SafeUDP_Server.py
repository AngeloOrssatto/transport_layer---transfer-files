import socket
from tqdm import tqdm

# IP = socket.gethostbyname(socket.gethostname())
IP = '192.168.202.4'
PORT = 4455
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = 'utf-8'
ACK = 'ack'
NACK = 'nack'
BLOCKS = 0

def main():
    # cria socket UDP
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(ADDR)
    # server.settimeout(4.0)
    print('[+] Waiting connection...')

    data, addr = server.recvfrom(SIZE)
    print(f"Recebi {data} de {addr}")
    prev = data.decode(FORMAT)
    item = prev.split("_")
    FILENAME = item[0]
    FILESIZE = int(item[1])
    # PACK_NUM = int(item[2])
    server.sendto(b'Filename received', addr)
    # print(f"{PACK_NUM} Packages for this file")
    
    
    bar = tqdm(range(FILESIZE), f"Receiving {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(f'recv_{FILENAME}', 'w') as f:
        # send/recv first ack
        msg, addr = server.recvfrom(SIZE)
        server.sendto(ACK.encode(FORMAT), addr)
        # for i in range (PACK_NUM):
        while True:
            data, addr = server.recvfrom(SIZE)
            
            
            if data.decode(FORMAT) == 'Finish':
                server.sendto(b"Finish", addr)
                break
            if not data:
                server.sendto(NACK.encode(FORMAT), addr)

            f.write(data.decode(FORMAT))
            server.sendto(ACK.encode(FORMAT), addr)
            BLOCKS = BLOCKS + 1
            bar.update(len(data))
            
    server.close()

if __name__ == '__main__':
    main()
    print(f"No Blocks received: {BLOCKS}")
