import socket
from constantsAndFunctions import *

localIP     = "server"
localPort   = COM_PORT
bufferSize  = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("Server up and listening")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    clientMessage = bytesAddressPair[0]
    clientAddress = bytesAddressPair[1]
    header = clientMessage[:4]
    clientMessage = clientMessage[4:]
    print(f"Client sent: {clientMessage.decode()}")