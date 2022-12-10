import socket
from sys import argv
from constants import *
from controller import NODECODE_TO_HOSTNAME


def updateRoutingTable(destinationCode,UDPForwardSocket:socket.socket,ROUTING_TABLE):
    UDPForwardSocket.sendto(HEADERS['reqTable']+destinationCode,('controller',COM_PORT))
    print("New Destination. Requesting Routing Table Update")
    while(True):
        bytesAddressPair = UDPForwardSocket.recvfrom(1024)
        encMessage = bytesAddressPair[0]
        header = encMessage[:3]
        if header == HEADERS['tableUpdate']:
            nextHopIP = encMessage[3:].decode()
            ROUTING_TABLE[destinationCode.decode()] = (nextHopIP,COM_PORT)
            return True
        elif header == HEADERS['noDestination']:
            return False

def printRoutingTable(ROUTING_TABLE):
    print("Routing Table Updated")
    print("""
    Node Code of Dest|IP to forward to
    __________________________________
    """)
    for key,data in ROUTING_TABLE.items():
        print(f"    {key}               |{data[0]}")


def main():
    # routing table with have format of 'nodeCode of dest':IP to forward to
    ROUTING_TABLE = {}
    localIP = NODECODE_TO_HOSTNAME[argv[1]]
    localPort   = COM_PORT
    bufferSize  = 1024
    destinationIP = None

    UDPForwardSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPForwardSocket.bind((localIP, localPort))
    print("Router up and listening")
    print("Current Routing Table")
    print("""
    Node Code of Dest|IP to forward to
    __________________________________
    NONE             |NONE
    """)

    # always true and waiting for new packets to com in
    while(True):
        # que to handle multiple incoming packets
        bytesAddressPair = UDPForwardSocket.recvfrom(bufferSize)

        # encoded message
        encMessage = bytesAddressPair[0]
        header = encMessage[:3]

        if header == HEADERS['message']:
            destinationCode = encMessage[4:6]
            if destinationCode.decode() in ROUTING_TABLE:
                UDPForwardSocket.sendto(encMessage,ROUTING_TABLE[destinationCode.decode()])
                print("Destination in routing table. Forwarding...")
            else:
                sendPacket = updateRoutingTable(destinationCode,UDPForwardSocket,ROUTING_TABLE)
                if sendPacket:  
                    UDPForwardSocket.sendto(encMessage,ROUTING_TABLE[destinationCode.decode()])
                    printRoutingTable(ROUTING_TABLE)
                else:
                    print("Destination Unknown to controller. Dropping Packet")



if __name__ == "__main__":
    main()


    