#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""import sys"""
import socket


class Serveur:
    """Cette classe fait l'interface avec le serveur"""

    s = socket.socket()
    host = '159.203.9.85'

    MAX_RECV = 1024 * 1024 * 512

    port = None
    prompt = None

    def __init__(self, port):
        self.port = port

    def send(self, texte):
        pass

    def receive(self):
        pass

    def close(self):
        pass
