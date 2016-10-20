import time
import socket
import RPi.GPIO as GPIO
from struct import *
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

p23 = GPIO.PWM(23, 1500)  # channel=25 frequency=50Hz
p24 = GPIO.PWM(24, 1500)  # channel=25 frequency=50Hz
p23.start(0)
p24.start(0)

UDP_IP = "192.168.1.145"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

try:
    while True:
        data, addr = sock.recvfrom(1024)
	print("data is:", data)
	#command,value  = unpack('2I4L',data)
	(command, value) = struct.unpack('!BH', data)
	print("command: ", command)
	print("value is: ", value)
	#dc = int(data)
	#print("dc= ",dc)
        #p23.ChangeDutyCycle(dc)
       	#p24.ChangeDutyCycle(dc)
except KeyboardInterrupt:
    pass
p23.stop()
p24.stop()
GPIO.cleanup()
sock.close()
