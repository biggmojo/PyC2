'''
Project: Command and Control
Author: Josiah R Kohlmeyer
'''

'''
Objective: Purely for educational purposes, create a command and control (C2) server that devices can connect back to
Arguments:
-p <port>: optional, the port to listen for connections on; defaults to 15789
-pr <protocol>: optional, TCP or UDP protocol to use; defaults to UDP
'''

#####################################################################################################################

### Beginning of file

# Required packages
import sys
import argparse
import socket

### Check Port
def check_port(port):
    if port is None:
        p = 15789
        return p
    elif 0 > port or 65535 < port:
        print("ERROR: Invalid port number.")
        sys.exit()
    else:
        p = port
        return p

### Check Protocol
def check_protocol(protocol):
    if protocol is None:
        pr = "UDP"
        return pr
    elif protocol != "UDP" and protocol != "TCP":
        print("ERROR: Invalid port protocol.")
        sys.exit()
    else:
        pr = protocol
        return pr

### Bind UDP Port
def bind_udp(port):
    print("Binding to UDP...")
    udp_ip = ''
    udp_port = port

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((udp_ip, udp_port))

    print("Awaiting connection...")
    while 1:
        data, addr = s.recvfrom(1024)
        print("Received message: %s" % data)

### Bind TCP Port
def bind_tcp(port):
    print("Binding to TCP...")
    tcp_ip = ''
    tcp_port = port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((tcp_ip, tcp_port))
    s.listen(1)

    print("Awaiting connection...")
    conn, addr = s.accept()
    print("Connection from: %s" % addr)
    while 1:
        data = conn.recv(1024)
        if not data: break
        print("Received message: " + data)
        conn.send(data) # Echo
    conn.close()

### Main Function
def main(argv):

    ### Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, help = "port to listen for connections on; defaults to 15789.")
    parser.add_argument("-pr", "--protocol", type=str, help = "protocol to listen with; defaults to UDP.")
    args = parser.parse_args()

    ### Check port is valid
    port = check_port(args.port)

    ### Check port protocol is valid
    protocol = check_protocol(args.protocol)

    ### Bind to port
    if protocol == "UDP":
        bind_udp(port)
    elif protocol == "TCP":
        bind_tcp(port)

if __name__ == "__main__":
    main(sys.argv)

### End of file