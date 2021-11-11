#!/usr/bin/python3

import socket #library to use https://docs.python.org/3/library/socket.html
from ports import ports_and_services

def getOpenPorts(target, portRange, verbose = False):
    openPorts = []
    #Obtener el host con socket
    target_ip = socket.gethostbyname(target)
    print("Host =", target_ip)
    
    def port_scan(port):
        try:
            s.connect((target_ip, port))
            return True
        except:
            return False
    
    #hacer un loop sobre el rango de puertos
    for port in range(portRange[0],portRange[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if port_scan(port):
           openPorts.append(port)
        s.close()
     
    # Primera entrega para evaluación
    # Falta poner mas verbosidad y mas robustez al programa
    # Pero el código ya no tiene errores
    
    # Modificacione se haran eventualmente
        
    return openPorts

