import socket, sys
import json
import time, datetime
from random import randint

SERVER_IP = '127.0.0.1'
PORT = 7555
MAX = 65535

def r():  # fungsi random nilai
 	acak = randint(1, 100)
 	return acak
incr = 0;
while True:
    t = time.time()
    waktu = datetime.datetime.fromtimestamp(t).strftime('%d-%m-%Y %H:%M:%S')
    incr = incr+ 1
    data = {'id': incr,'PH':  r() , 'DO': + r() , 'waktu':  waktu}
    datax = json.dumps(data)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(datax,(SERVER_IP, PORT))
    print "Data Sensor : ",datax,"\n"
    time.sleep(3)
s.close()
