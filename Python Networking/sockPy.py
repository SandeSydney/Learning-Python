## Sample code to send a request to get stuff from a website using sockets

import socket

# create the socket and connect to get the data
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
command = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(command)

## choose what to do when recieving data
while True:
    # Receive data in bits of 512
    data = sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
sock.close