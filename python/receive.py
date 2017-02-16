import socket
import sys
import struct
from RPIO import PWM
import time
import RPi.GPIO as GPIO
import math as math

p = PWM.Servo()
p.set_servo(27, 1900)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

p23 = GPIO.PWM(23, 500)  # channel=25 frequency=50Hz
p24 = GPIO.PWM(24, 500)  # channel=25 frequency=50Hz
p23.start(0)
p24.start(0)



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
#server_address = ('192.168.1.145', 5555)
server_address = ('192.168.245.1', 5555)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
while True:
    #print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(24)
    
    #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    #print >>sys.stderr, data
    
    if data:
        (command, value) = struct.unpack('!BH', data)
      #  print >>sys.stderr, ' %s da  to %s' % (command, value)
	if (command == 2) and ( 75 <= value <= 175 ): # roll: 56 - 171 
            pulse = (value - 75)*(225-155)/(175-75) + 155
            p.set_servo(27,pulse*10)
            # print('pulse = ', pulse*10)
	elif (command == 4) and (844 <= value <= 991) : # throtle: 990 - 844 
            x  = 100 * (value - 844)/(991-844) + 1 # normalize
            if (x > 2) :
                dc = (29 * math.log(x*2) + 46)/2 # apply logariphmic function
            else :
                dc = 0
            print 'X = ', x , ' :: dc = ',  dc 
	    p23.ChangeDutyCycle(dc)
            p24.ChangeDutyCycle(dc)
       
            
