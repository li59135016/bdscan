__author__ = 'tek tengu'
from socket import *

SCAN_PROTOCOL = "Scan Protocol"
SCAN_PROTOCOL_TCP = "TCP"
SCAN_PROTOCOL_UDP = "UDP"
STATUS_OPEN = "Open"
STATUS_CLOSED = "Closed"


results = {}

def scan(args, target, ports):
    if(args.get(SCAN_PROTOCOL).equals(SCAN_PROTOCOL_TCP)):
        doTCPScan(args, target, ports)
    elif(args.get(SCAN_PROTOCOL).equals(SCAN_PROTOCOL_UDP)):
        doUDPScan(args, target, ports)

def scan(args, targets, ports):
    for target in targets:
        connScan(args, target, ports)

def doTCPScan(args, target, ports):
    for port in ports:
        try:
            # Is there something to add for the args?
            skt = socket(AF_INET, SOCK_STREAM)
            skt.connect((target, port))
            writeSuccessConnect(target, port, SCAN_PROTOCOL_TCP)
            skt.close()
        except:
            writeFailureConnect(target, port, SCAN_PROTOCOL_TCP)

def doUDPScan(args, target, ports):
    for port in ports:
        try:
            # Is there something to add for the args?
            skt = socket(AF_INET, SOCK_DGRAM)
            skt.connect((target, port))
            writeSuccessConnect(target, port, SCAN_PROTOCOL_UDP)
            skt.close()
        except:
            writeFailureConnect(target, port, SCAN_PROTOCOL_UDP)

def writeSuccessConnect(target, port, protocol):
    tstruc = results[target]
    if tstruc is None:
        tstruc = {}
        tstruc[protocol] = protocol
    portstruc = tstruc[protocol]
    if portstruc is None:
        portstruc = {}
    portstruc[port, STATUS_OPEN]
    results[target] = tstruc

def writeFailureConnect(target, port, protocol):
    tstruc = results[target]
    if tstruc is None:
        tstruc = {}
        tstruc[protocol] = protocol
    portstruc = tstruc[protocol]
    if portstruc is None:
        portstruc = {}
    portstruc[port, STATUS_CLOSED]
    results[target] = tstruc

def resetResults():
    results = {}

def getResults():
    return results

def printReadableResults():
    str = StringIO()
    for target in results.keys():
        print >> str, target
        print >> str, ":\n"
        for protocol in results[target].keys():
            print >> str, "\t"
            print >> str, protocol
            print >> str, "\n"
            for port in results[target][protocol].keys():
                print >> str, "\t\t\t"
                print >> str, port
                print >> str, "<<>>"
                print >> str, results[target][protocol][port]
                print >> str, "\n"
    return str.getvalue()

def printCSVResult():
    str = StringIO()
    print >> str, "target"
    print >> str, ","
    print >> str, "protocol"
    print >> str, ","
    print >> str, "port"
    print >> str, ","
    print >> str, "status"
    print >> str, "\n"
    for target in results.keys():
        for protocol in results[target].keys():
            for port in results[target][protocol].keys():
                print >> str, target
                print >> str, ","
                print >> str, protocol
                print >> str, ","
                print >> str, port
                print >> str, ","
                print >> str, results[target][protocol][port]
                print >> str, "\n"
    return str.getvalue()
