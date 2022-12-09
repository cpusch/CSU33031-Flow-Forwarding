import socket
from sys import argv
from constantsAndFunctions import *

localIP = argv[1]
localPort   = COM_PORT
bufferSize  = 1024
destinationIP = None

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
    if localIP == FORWARDER_IPS['pdf'][0]:
        UDPForwardSocket.sendto(DESTINATION_HEADER+NODE_CODES['server']+clientMessage, FORWARDER_IPS['txt'])
        print(f"Packet received forwarding...")
    elif localIP == FORWARDER_IPS['txt'][0]:
        print(f"Packet received last forwarder, sending to server")
        UDPForwardSocket.sendto(DESTINATION_HEADER+NODE_CODES['server']+clientMessage, serverIP)


    