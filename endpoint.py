import socket
from constants import *
from controller import NODECODE_TO_HOSTNAME
from sys import argv

def getRouterIP(localIP):
    if localIP == "client":
        return ('workerPDF',COM_PORT)
    elif localIP == "client2":
        return ('workerTXT',COM_PORT)
    elif localIP == "server":
        return ('workerImage',COM_PORT)
    else:
        raise Exception("Unknown Endpoint")

def main():
    isReceiving = False
    localIP = NODECODE_TO_HOSTNAME[argv[1]][0]
    bufferSize = 1024
    print(localIP)
    return
    routerIP = getRouterIP(localIP)

    UDPEndpointSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPEndpointSocket.bind(localIP)
    while(True):
        runMode = input("Would you like to send or receive a message? ")
        if runMode.lower() == "send":
            isReceiving = True
            break
        elif runMode.lower() == "receive":
            break
        else:
            print("Please enter 'send' or 'receive'.")

    while(True):
        if(isReceiving):
            bytesAddressPair = UDPEndpointSocket.recvfrom(bufferSize)
            clientMessage = bytesAddressPair[0]
            clientAddress = bytesAddressPair[1]
            print(f"Message Received: {clientMessage.decode()}")
        else:
            message = input("Please enter the message you would like to send then hit enter: ").encode()
            destination = input("Please enter your destination Nodecode then hit enter: ").encode()
            UDPEndpointSocket.sendto(HEADERS['message']+destination+message,routerIP)
            while(True):
                userContinue = input("Would you like to wait for a response (Yes) or send another message(No)? ").lower()
                if userContinue == 'yes':
                    isReceiving = True
                    break
                elif userContinue == 'no':
                    break
                else:
                    print("Please enter yes or no. ")


if __name__ == "__main__":
    main()