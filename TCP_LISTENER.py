import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('', 2012)
sock.bind(server_address)
print('starting up on %s port %s' % sock.getsockname())
sock.listen(1)

while True:
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address, file=sys.stderr, )
        while True:
            data = connection.recv(256)
            print('received "%s"' % data, file=sys.stderr)
            # decoded_str = data.decode("utf-8")
            file1 = open("c:/input.txt", "ab")
            file1.write(data)
            
    finally:
        connection.close()




