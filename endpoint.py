import socket
from constantsAndFunctions import *
from sys import argv


localIP = ENDPOINT_IPS[argv[1]][0]
forwarderAddress = (ROUTER_IPS['R1'])
bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.bind(localIP)

UDPClientSocket.sendto(HEADERS['dest']+ENDPOINT_IPS['E3']+bytesToSend, forwarderAddress)
print(f"Message: '{bytesToSend}' sent to server")