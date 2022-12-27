import socket
import datetime
import time

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if data == "/stop":
                print("jj")
                conn.close()
            else:
                print(f"[{datetime.datetime.now()}] - {data}")
                time.sleep(5)
                try:
                    conn.send(data)
                    print("Message successfully sended")
                except:
                    print("Error")
