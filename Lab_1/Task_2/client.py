import sys
import socket
import threading


class Client:
    def __init__(self, client_name):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 8080)
        self.socket.connect(self.server_address)

        self.client_name = client_name
        send = threading.Thread(target=self.client_send)
        send.start()
        receive = threading.Thread(target=self.client_receive)
        receive.start()

    def client_send(self):
        self.socket.send(bytes(self.client_name, encoding='utf-8'))
        while True:
            try:
                c = input()
                sys.stdout.write("\x1b[1A\x1b[2K")
                self.socket.send(bytes(c, encoding='utf-8'))
            except:
                self.socket.close()
                return

    def client_receive(self):
        while True:
            try:
                print(self.socket.recv(1024).decode("utf-8"))
            except:
                self.socket.close()
                return


if __name__ == "__main__":
    client_name = input("Write your nickname: ")
    Client(client_name)
