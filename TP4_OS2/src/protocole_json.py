#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TP4_OS2.src.protocole import Protocole

class Protocole_json(Protocole):
    """Interface du langage de communication JSON"""
    def __init__(self):
        super(Protocole_json, self).__init__()
        pass

    def interprete(self, message_serveur):
        pass

    def genere_bonjour(self):
        pass

    def genere_nom(self):
        pass

    # etc...