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

def main(argv):

    ### Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, help = "port to listen for connections on; defaults to 15789.")
    parser.add_argument("-pr", "--protocol", type=str, help = "protocol to listen with; defaults to UDP.")
    args = parser.parse_args()

    ### Check port is valid
    if args.port is None:
        port = 15789
    elif 0 > args.port or 65535 < args.port:
        print("ERROR: Invalid port number.")
        sys.exit()
    else:
        port = args.port

    ### Check port protocol is valid
    if args.protocol is None:
        prot = "UDP"
    elif args.protocol != "UDP" and args.protocol != "TCP":
        print("ERROR: Invalid port protocol.")
        sys.exit()
    else:
        prot = args.protocol

if __name__ == "__main__":
    main(sys.argv)

### End of file