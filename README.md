# SLORIS

**This Is For Educational Purposes Only** 

This is a Low BandWidth DDos Attack Script

It works by creating a bunch of sockets, sending get requests with each socket. Once connected, send a keep alive from each socket.

From The Help
```
usage: sloris [-h] [-p PORT] [-a ALIVETIME] [-t SLEEPTIME] [-s SOCKET] [-5 [SOCKS5]] [-5p SOCKS5PORT] [domain]

Slow Loris Attack Script

positional arguments:
  domain                Host to test

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port
  -a ALIVETIME, --alivetime ALIVETIME
                        Keep Alive Time
  -t SLEEPTIME, --sleeptime SLEEPTIME
                        Time to sleep
  -s SOCKET, --socket SOCKET
                        # of sockets
  -5 [SOCKS5], --socks5 [SOCKS5]
                        Socks5 proxy
  -5p SOCKS5PORT, --socks5port SOCKS5PORT
                        Socks5 port
```
