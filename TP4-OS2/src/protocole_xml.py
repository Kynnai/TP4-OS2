#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import

class Protocole_xml(Protocole):
    """Interface du langage de communication XML"""
    def __init__(self):
        super(Protocole_xml, self).__init__()
        pass

    def interprete(self, message_serveur):
        pass

    def genere_bonjour(self):
        pass

    def genere_nom(self):
        pass