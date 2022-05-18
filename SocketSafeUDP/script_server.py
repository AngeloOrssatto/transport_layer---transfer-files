
if __name__ == "__main__":
    for i in range (0, 10):
        print(f"{i} EXEC")
        exec(open("SafeUDP_Server.py").read())
        print("================================================================")

