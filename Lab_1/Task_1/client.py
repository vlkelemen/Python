import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected")
    while True:
        message = input("Write your message: ")
        s.send(message.encode("utf-8"))
        data = s.recv(1024).decode("utf-8")
        print('Echoing: ', data)
