import socket
from constants import *
from controller import NODECODE_TO_HOSTNAME
from sys import argv

def main():
    localIP = NODECODE_TO_HOSTNAME[argv[1]][0]
    bufferSize = 1024

    UDPEndpointSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPEndpointSocket.bind(localIP)
    while(True):
        runMode = input("Would you like to send or receive a message? ")
        if runMode.lower() == "send":
            break
        elif runMode.lower() == "receive":
            break
        else:
            print("Please enter 'send' or 'receive'.")

    while(True):    
        bytesAddressPair = UDPEndpointSocket.recvfrom(bufferSize)
        clientMessage = bytesAddressPair[0]
        clientAddress = bytesAddressPair[1]

if __name__ == "__main__":
    main()