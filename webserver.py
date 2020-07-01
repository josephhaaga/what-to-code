"""A simple webserver implementation."""

import socket
from time import sleep


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 8081))
    sock.listen(2)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024).decode("ascii")
        if data:
            print(f"Received: {data}")
            conn.send(b"Hello!")
        sleep(1)

if __name__ == '__main__':
    main()
