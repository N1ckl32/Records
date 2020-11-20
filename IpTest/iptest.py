#! /usr/bin/python
# coding:utf-8
# Author: Cui Guangxu

import socket
import threading
from thread import *

# 2020.9.8 modified: Add IPv6 Support
# Remaining problem: Ctrl + C to terminate process

HOSTv4 = '0.0.0.0'
PORT = 80
HOSTv6 = '::'

listen_socket_v4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket_v4.bind((HOSTv4, PORT))
listen_socket_v4.listen(10)

listen_socket_v6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
listen_socket_v6.bind((HOSTv6, PORT))
listen_socket_v6.listen(10)


def clientthread(conn):
    request = conn.recv(10240)
    if not request:
        conn.close()
    else:
        REMOTE_ADDR = conn.getpeername()[0]
        res_head = 'HTTP/1.2 200 OK\r\nServer: IPTest\r\nRemote IP: ' + REMOTE_ADDR + '\r\n\r\n'
        res = res_head + 'Remote IP: ' + REMOTE_ADDR + '\r\n'
        conn.sendall(res)
    conn.close()


# Change solution to multithread to deal IPv4 and IPv6 connection separately
def threadv4():
    try:
        while True:
            client_connection_v4, client_address_v4 = listen_socket_v4.accept()
            start_new_thread(clientthread, (client_connection_v4,))
    finally:
        listen_socket_v4.close()


def threadv6():
    try:
        while True:
            client_connection_v6, client_address_v6 = listen_socket_v6.accept()
            start_new_thread(client_address_v6, (client_connection_v6), )
    except Exception as e:
        listen_socket_v6.close()


if __name__ == '__main__':
    tv4 = threading.Thread(target=threadv4)
    tv4.start()

    tv6 = threading.Thread(target=threadv6)
    tv6.start()
