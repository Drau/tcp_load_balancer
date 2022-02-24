import socket


while True:
    data = input('Enter text:')
    if data == 'exit':
        break

    # Connect the socket to the port where the server is listening
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 11111)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    message = data.encode(encoding='utf-8')
    try:
        # Send data
        print('[CLIENT] sending "%s"' % message)
        sock.sendall(message)
        data = sock.recv(1024)
        print('[CLIENT] received "%s"' % data)
    except Exception as e:
        print(f'[CLIENT] exception occurred: {e}')
    print('[CLIENT] closing socket')
    sock.close()
