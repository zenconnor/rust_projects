import socket
import os
import pathlib
import time

if __name__ == "__main__":
    print("hello world, this is the client")
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    for i in range(0, 4):
        clientsocket.send(b'hello')
        time.sleep(5)
    clientsocket.close()