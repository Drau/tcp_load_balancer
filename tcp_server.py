# a simple tcp server
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 12345))
sock.listen(5)
print('[SERVER] listening for incoming connections')

while True:
    connection, address = sock.accept()
    buf = connection.recv(1024)
    name = socket.gethostname()
    msg = f'[SERVER] received: {buf} from {address} - sending: {name}'
    print(msg)
    connection.send(msg.encode(encoding='utf-8'))
    connection.close()
