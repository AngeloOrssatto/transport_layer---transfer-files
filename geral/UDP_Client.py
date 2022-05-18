import socket, os, time
from tqdm import tqdm

# IP = socket.gethostbyname(socket.gethostname())
IP = '192.168.202.157'
PORT = 4455
ADDR = (IP, PORT)
SIZE = 2048
FORMAT = 'utf-8'
FILENAME = 'data.txt'
FILESIZE = os.path.getsize(FILENAME)
BLOCKS = 0

def main():
    # cria socket UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.connect(ADDR)
    client.settimeout(10.0)

    data = f"{FILENAME}_{FILESIZE}"
    client.send(data.encode(FORMAT))
    msg, addr = client.recvfrom(SIZE)
    print(f"SERVER: {msg.decode(FORMAT)}")

    bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(FILENAME, 'r') as f:
        while True:
            data = f.read(SIZE)

            if not data:
                client.send('F'.encode(FORMAT))
                msg = client.recvfrom(SIZE)
                break

            client.send(data.encode(FORMAT))
            BLOCKS = BLOCKS + 1
            msg = client.recvfrom(SIZE)

            bar.update(len(data))

    client.close()
    


if __name__ == '__main__':
    begin = time.perf_counter_ns()
    main()
    end = time.perf_counter_ns()
    print('Execution time:', (end-begin), 'ns')