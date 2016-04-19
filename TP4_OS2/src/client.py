#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TP4_OS2.src.serveur import Serveur
from TP4_OS2.src.protocoleJson import ProtocoleJson
from TP4_OS2.src.protocoleXml import ProtocoleXml
import sys


class Client:
    """Classe représentant le client"""

    serveur = None
    protocole = None

    def __init__(self, protocole, port, prompt):
        self.protocole = protocole
        self.serveur = Serveur(port)
        if prompt:
            pass
        else:
            self.synchroniser()

    def bonjour(self):
        envoie = self.protocole.genere_bonjour()
        self.serveur.send(envoie)
        print(self.protocole.interprete(self.serveur.receive()))

    def nom(self):
        pass

    def listeDossiers(self, dossier):
        pass

    def listeFichiers(self, fichier):
        pass

    def synchroniser(self):
        pass

if __name__ == '__main__':
    prompt = False
    if  sys.argv[3].toString == "prompt":
        prompt = True

    if sys.argv[2].toString == "json":
        Client(ProtocoleJson, sys.argv[1].toString, prompt)

    elif sys.argv[2].toString == "xml":
        Client(ProtocoleXml, sys.argv[1].toString, prompt)
