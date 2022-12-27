import socket
import _thread
from datetime import datetime


class Server:

    def __init__(self):
        self.users_table = {}

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 8080)
        self.socket.bind(self.server_address)
        self.socket.listen(10)
        print('Starting up on {} port {}'.format(*self.server_address))
        self.wait_for_new_connections()

    def wait_for_new_connections(self):
        while True:
            connection, _ = self.socket.accept()
            _thread.start_new_thread(self.on_new_client, (connection,))

    def on_new_client(self, connection):
        try:
            client_name = connection.recv(64).decode('utf-8')
            self.users_table[connection] = client_name
            print(f'{self.get_current_time()} {client_name} joined the room !!')

            while True:
                data = connection.recv(64).decode('utf-8')
                if data != '':
                    self.multicast(data, owner=connection)
                else:
                    return
        except:
            print(f'{self.get_current_time()} {client_name} left the room !!')
            self.users_table.pop(connection)
            connection.close()

    def get_current_time(self):
        return datetime.now().strftime("%H:%M:%S")

    def multicast(self, message, owner=None):
        for conn in self.users_table:
            data = f'{self.get_current_time()} {self.users_table[owner]}: {message}'
            conn.sendall(bytes(data, encoding='utf-8'))


if __name__ == "__main__":
    Server()
