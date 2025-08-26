import sys
import socket
import random

def create_packet(size:int=1024) -> bytes:

if len(sys.argv) != 4:
    print("usage: python esercizio.py <ip> <porta> <numero_pacchetti")
    sys.exit(254)

ip = sys.argv[1]
porta = sys.argv [2]
npack = int(sys.argv[3])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, int(porta)))

for i in range(npack):
    packet = random.randbytes(1024) # 1KB packet
    s.send(packet)
    print(f"inviato pacchetto {i + 1}/{npack} a {ip}:{porta}")

s.close()
print("tutti i pacchetti sono stati inviati.")

