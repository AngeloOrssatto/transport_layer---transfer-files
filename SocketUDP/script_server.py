# import TCP_Client.py
# import TCP_Server.py

if __name__ == "__main__":
    for i in range (0, 10):
        print(f"{i} EXEC")
        exec(open("UDP_Server.py").read())
        print("================================================================")
