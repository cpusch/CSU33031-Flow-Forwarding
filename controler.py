from constantsAndFunctions import *

localIP = 'controller'

ROUTING_TABLE = [
    # COLUMES ARE : 
    # DEST, SRC, ROUTER, IN, OUT
    ['E1','E3','R3','E3','R1'],
    ['E1','E3','R1','R3','E1'],
    ['E1','E2','R2','E2','R1'],
    ['E1','E2','R1','R2','E1'],
    ['E2','E1','R1','E1','R2'],
    ['E2','E1','R2','R1','E2'],
    ['E2','E3','R3','E3','R2'],
    ['E2','E3','R2','R3','E2'],
    ['E3','E1','R1','E1','R3'],
    ['E3','E1','R3','R1','E3'],
    ['E3','E2','R2','E2','R3'],
    ['E3','E2','R3','R2','E3'],
]