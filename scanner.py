#!/usr/bin/python3

import socket #library to use https://docs.python.org/3/library/socket.html
from ports import ports_and_services

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def getOpenPorts(target, portRange)
    openPorts = []
    #Obtener el host con socket
    target_ip = socket.gethostbyname(target)
    
    def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False
    
    #hacer un loop sobre el rango de puertos
    for port in portRange:
        if port_scan(port):
           openPorts.append(port)
        
    return openPorts

