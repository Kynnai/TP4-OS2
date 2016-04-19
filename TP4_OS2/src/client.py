#!/usr/bin/python3
# -*- coding: utf-8 -*-

from serveur import Serveur
from protocoleJson import ProtocoleJson
from protocoleXml import ProtocoleXml
import sys


class Client:
    """Classe représentant le client"""

    serveur = None
    protocole = None

    def __init__(self, protocole, port, prompt):
        self.protocole = protocole
        self.serveur = Serveur(port)
        if prompt:
            self.nom()
        else:
            self.synchroniser()

    def bonjour(self):
        envoie = self.protocole.genere_bonjour(self)
        self.serveur.send(envoie)
        message_serveur = self.serveur.receive()
        print(self.protocole.interprete(self, message_serveur))

    def nom(self):
        envoie = self.protocole.genere_nom(self)
        self.serveur.send(envoie)
        message_serveur = self.serveur.receive()
        print(self.protocole.interprete(self, message_serveur))


    def listeDossiers(self, dossier):
        envoie = self.protocole.genere_listeDossiers(self, dossier)
        self.serveur.send(envoie)
        message_serveur = self.serveur.receive()
        print(self.protocole.interprete(self, message_serveur))

    def listeFichiers(self, fichier):
        pass

    def synchroniser(self):
        pass

if __name__ == '__main__':
    prompt = False
    if  sys.argv[3] == "prompt":
        prompt = True

    if sys.argv[2] == "json":
        Client(ProtocoleJson, int(sys.argv[1]), prompt)

    elif sys.argv[2] == "xml":
        Client(ProtocoleXml, int(sys.argv[1]), prompt)
