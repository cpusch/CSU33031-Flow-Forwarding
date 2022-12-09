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
    'R1':('workerPDF',COM_PORT),
    'R2':('workerTXT',COM_PORT),
    'R3':('workerImage',COM_PORT),
    'E1':('client',COM_PORT),
    'E2':('client2',COM_PORT),
    'E3':('server',COM_PORT)
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
        destinationIP = routerMessage.decode()
        
        destinationHostname = socket.gethostbyaddr(destinationIP)
        destinationCode = HOSTNAME_TO_NODECODE[destinationHostname]
        routerHostname = socket.gethostbyaddr(routerAddress)
        routerCode = HOSTNAME_TO_NODECODE[routerHostname]
        try:
            nextHopHostname = ROUTING_TABLE[(destinationCode,routerCode)]
            UDPRouterSocket.sendto(HEADERS['tableUpdate']+nextHopHostname.encode(), routerAddress)
            print("Destination found sending next hop.")
        except KeyError:
            print("Destination not found")
            UDPRouterSocket.sendto(HEADERS['noDestination'],routerAddress)


if __name__ == "__main__":
    main()
    