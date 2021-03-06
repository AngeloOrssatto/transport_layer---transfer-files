import socket, os, time
from tqdm import tqdm

# IP = socket.gethostbyname(socket.gethostname())
IP = '192.168.202.157'
PORT = 44550
ADDR = (IP, PORT)
SIZE = 100
FORMAT = 'utf-8'
FILENAME = 'data2.txt'
FILESIZE = os.path.getsize(FILENAME)
BLOCKS = 0

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    
    data = f"{FILENAME}_{FILESIZE}"
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"SERVER: {msg}")

    bar = tqdm(range(FILESIZE), f"Sending {FILENAME}", unit="B", unit_scale=True, unit_divisor=SIZE)

    with open(FILENAME, 'r') as f:
        while True:
            data = f.read(SIZE)

            if not data:
                break

            client.send(data.encode(FORMAT))
            BLOCKS = BLOCKS + 1
            msg = client.recv(SIZE).decode(FORMAT)

            bar.update(len(data))

    client.close()

if __name__ == "__main__":
    begin = time.perf_counter_ns()
    main()
    end = time.perf_counter_ns()
    print("Execution time:", (end-begin), 'ns')