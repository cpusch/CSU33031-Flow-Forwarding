import socket
from constants import *

localip = ('client',54321)
bytesToSend = b'hello endpoint'
forwarderAddress = (ROUTER_IPS['R1'])
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind(localip)

UDPClientSocket.sendto(HEADERS['dest']+ENDPOINT_IPS['E3']+bytesToSend, forwarderAddress)
print(f"Message: '{bytesToSend}' sent to server")