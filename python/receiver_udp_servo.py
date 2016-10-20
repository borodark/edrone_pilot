import socket
import sys
import struct
from RPIO import PWM
import time

p = PWM.Servo()
p.set_servo(27, 1500)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.1.145', 5555)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
while True:
    #print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
    #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    #print >>sys.stderr, data
    
    if data:
        (command, value) = struct.unpack('!BH', data)
        #print >>sys.stderr, ' %s da  to %s' % (command, value)
	if command == 2:
            pulse = value
            p.set_servo(27,pulse*10)
            print('servo  = ', pulse*10)
            #time.sleep(0.1)
	elif command == 4: # throtle 990 - 850 
            dc =  (value - 850)/1.5 # TODO normalize 
            p23.ChangeDutyCycle(dc)
            p24.ChangeDutyCycle(dc)
	    print('servo  = ', pulse*10)
