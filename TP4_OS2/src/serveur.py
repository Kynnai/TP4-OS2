#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""import sys"""
import socket


class Serveur:
    """Cette classe fait l'interface avec le serveur"""

    s = None
    host = '159.203.9.85'

    MAX_RECV = 1024 * 1024 * 512

    port = None
    prompt = None

    def __init__(self, port):
        self.s = socket.socket()
        self.s.connect((self.host, port))

    def send(self, texte):
        self.s.send(texte.encode(encoding='UTF-8'))

    def receive(self):
        return self.s.recv(self.MAX_RECV).decode('UTF-8')

    def close(self):
        self.s._close()
