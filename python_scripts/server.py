import socket
import os
import pathlib
import struct

def mult(num):
    """multiplies the given number by two"""
    return None


if __name__ == "__main__":
    print("This is the server")
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.bind(('localhost', 8089))
    serversocket.listen(1) # become a server socket, maximum 1 connections
    connection, address = serversocket.accept()
    while True:
        buf = connection.recv(1024)
        if not buf:
            break
        if len(buf) > 0:
            print(buf.decode())