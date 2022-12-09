from constants import *
import socket

HOSTNAME_TO_NODECODE = {
    'workerPDF':'R1',
    'workerTXT':'R2',
    'workerImage':'R3',
    'client':'E1',
    'client2':'E2',
    'server':'E3'
}

NODECODE_TO_HOSTNAME = {
    'R1':'workerPDF',
    'R2':'workerTXT',
    'R3':'workerImage',
    'E1':'client',
    'E2':'client2',
    'E3':'server'
}

ROUTING_TABLE = {
    # Dest, Router are keys and value is the next hop for the routers to take
    ('E1', 'R3'): 'R1',
    ('E1', 'R1'): 'E1',
    ('E1', 'R2'): 'R1',
    ('E2', 'R1'): 'R2',
    ('E2', 'R2'): 'E2',
    ('E2', 'R3'): 'R2',
    ('E3', 'R1'): 'R3',
    ('E3', 'R3'): 'E3',
    ('E3', 'R2'): 'R3'
}
    

def main():
    localIP = 'controller'
    localPort = COM_PORT
    bufferSize  = 1024
    UDPRouterSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPRouterSocket.bind((localIP, localPort))


    print("Controller up and listening")
    while(True):
        bytesAddressPair = UDPRouterSocket.recvfrom(bufferSize)
        routerMessage = bytesAddressPair[0]
        routerAddress = bytesAddressPair[1]

        # resolves routers ip to hostname to then find the routers code in the dict
        routerCode = HOSTNAME_TO_NODECODE[socket.gethostbyaddr(routerAddress[0])]
        header = routerMessage[:3]

        if header == HEADERS['reqTable']:
            destinationCode = routerMessage[3:].decode()
            try:
                nextHopIP = socket.gethostbyname(ROUTING_TABLE[(destinationCode,routerCode)])
                UDPRouterSocket.sendto(HEADERS['tableUpdate']+nextHopIP.encode(), routerAddress)
                print("Destination found sending next hop.")
            except KeyError:
                print("Destination not found")
                UDPRouterSocket.sendto(HEADERS['noDestination'],routerAddress)


if __name__ == "__main__":
    main()
    