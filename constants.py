COM_PORT = 54321
ROUTER_IPS =    {'R1':('workerPDF',COM_PORT),
                 'R2':('workerTXT',COM_PORT),
                 'R3':('workerImage',COM_PORT)}

ENDPOINT_IPS = {'E1':('client',COM_PORT),
                'E2':('client2',COM_PORT),
                'E3':('server',(COM_PORT))}

HEADERS =   {'dest':b'DST',
             'length':b'LEN',
             'reqTable':b'REQ'}