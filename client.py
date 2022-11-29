import socket

host = 'localhost'
port = 16789

client = socket.socket()
client.connect((host, port))

message = input(" -> ")

while message.lower().strip() != 'quit':
    client.send(message.encode())
    data = client.recv(1024).decode()

    print('Received from server: ' + data)

    message = input(" -> ")

client.close()
