# SLORIS

**This Is For Educational Purposes Only** 

This is a Low BandWidth DDos Attack Script

It works by creating a bunch of sockets, sending get requests with each socket. Once connected, send a keep alive from each socket.

From The Help
```
usage: sloris [-h] [-p PORT] [-a ALIVETIME]
              [-t SLEEPTIME] [-s SOCKET]
              [domain]

Slow Loris Attack Script

positional arguments:
  domain                Host

optional arguments:
  -h, --help            show this help message and
                        exit
  -p PORT, --port PORT  Port
  -a ALIVETIME, --alivetime ALIVETIME
                        Keep Alive Time
  -t SLEEPTIME, --sleeptime SLEEPTIME
                        Time to sleep
  -s SOCKET, --socket SOCKET
                        # of sockets
```
