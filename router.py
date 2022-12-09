import socket
from sys import argv
from constants import *
from controller import NODECODE_TO_HOSTNAME




def main():
    # routing table with have format of 'nodeCode of dest':IP
    ROUTING_TABLE = {}
    localIP = NODECODE_TO_HOSTNAME[argv[1]][0]
    localPort   = COM_PORT
    bufferSize  = 1024
    destinationIP = None

    UDPForwardSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPForwardSocket.bind((localIP, localPort))
    print("Forwarder up and listening")

    # always true and waiting for new packets to com in
    while(True):
        bytesAddressPair = UDPForwardSocket.recvfrom(bufferSize)
        # encoded message
        encMessage = bytesAddressPair[0]
        header = encMessage[:4]

        if header == HEADERS['message']:
            destinationCode = encMessage[4:7]
            payload = encMessage[7:]
        elif header == HEADERS['tableUpdate']:
            pass
        elif header == HEADERS['noDestination']:
            print("Destination not found dropping packet")



if __name__ == "__main__":
    main()


    