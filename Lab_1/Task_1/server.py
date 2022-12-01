import socket
from datetime import datetime

host = 'localhost'
port = 16789

server = socket.socket()
server.bind((host, port))

server.listen(2)
conn, addr = server.accept()

print("Connection from: " + str(addr) + " at", datetime.now())
while True:
    # It won't accept data packet greater than 1024 bytes
    data = conn.recv(1024).decode()
    if not data:
        # if data is not received - break
        break
    print("from connected user: " + str(data))
    conn.send(data.encode())

conn.close()
