import threading
import socket

host = 'localhost'
port = 16789

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients_list = []
nicknames_list = []


def broadcast(message):
    for client in clients_list:
        client.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients_list.index(client)
            clients_list.remove(client)
            client.close()
            nickname = nicknames_list[index]
            broadcast(f'{nickname} has left the chat room!'.encode('utf-8'))
            nicknames_list.remove(nickname)
            break


def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        client.send('nickname?'.encode('utf-8'))
        nickname = client.recv(1024)
        nicknames_list.append(nickname)
        clients_list.append(client)
        print(f'User {nickname} joined the server with {str(address)} ip/port'.encode('utf-8'))
        broadcast(f'{nickname} has connected to the chat room\n'.encode('utf-8'))
        client.send("You are now connected to the chat! (only you can see this message)".encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()
