import socket
import sys
from constants import *

localIP = sys.argv[1]
localPort   = 54321
bufferSize  = 1024
serverIP = ('server', 54321)

UDPForwardSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPForwardSocket.bind((localIP, localPort))
print("Forwarder up and listening")

while(True):
    bytesAddressPair = UDPForwardSocket.recvfrom(bufferSize)
    clientMessage = bytesAddressPair[0]
    clientAddress = bytesAddressPair[1]

    header = clientMessage[:4]
    print(header)
    clientMessage = clientMessage[4:]
    print(f"packet received. Destination is node code: 2 [server]")
    if localIP == FORWARDER_IPS['pdf'][0]:
        UDPForwardSocket.sendto(DESTINATION_HEADER+NODE_CODES['server']+clientMessage, FORWARDER_IPS['txt'])
        print(f"Packet received forwarding...")
    elif localIP == FORWARDER_IPS['txt'][0]:
        print(f"Packet received last forwarder, sending to server")
        UDPForwardSocket.sendto(DESTINATION_HEADER+NODE_CODES['server']+clientMessage, serverIP)


    