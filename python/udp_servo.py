import socket
import sys
import struct

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.1.145', 5555)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data
    
    if data:
        (command, value) = struct.unpack('!BH', data)
        print >>sys.stderr, ' %s da  to %s' % (command, value)

