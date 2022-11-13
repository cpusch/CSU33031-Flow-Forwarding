import socket
from constants import *

localip = ('client',54321)
bytesToSend = b'hello server'
forwarderAddress = (FORWARDER_IPS['pdf'])
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind(localip)

UDPClientSocket.sendto(DESTINATION_HEADER+NODE_CODES['server']+bytesToSend, forwarderAddress)
print(f"Message: '{bytesToSend}' sent to server")