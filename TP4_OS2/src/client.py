#!/usr/bin/python3
# -*- coding: utf-8 -*-

from serveur import Serveur
from protocoleJson import ProtocoleJson
from protocoleXml import ProtocoleXml
from interfaceUtilisateur import InterfaceUtilisateur
import sys


class Client:
    """Classe représentant le client"""

    serveur = None
    protocole = None
    interface = None

    def __init__(self, protocole, port, prompt):
        self.protocole = protocole
        self.serveur = Serveur(port)
        self.interface = InterfaceUtilisateur()
        if prompt:
            self.communication()
        else:
            self.synchroniser()

    def communication(self):
        r = input("Commande:").split(" ")
        while r[0] != "quitter":
            envoie = None
            message = "Commande invalide"
            if r[0] == "connecter?":
                envoie = self.protocole.genere_bonjour(self)
            elif r[0] == "nomServeur?":
                envoie = self.protocole.genere_nom(self)
            elif r[0] == "listeDossier?":
                if len(r) != 1:
                    envoie = self.protocole.genere_listeDossiers(self, r[1])
                else:
                    message = "Élément manquant!"
            elif r[0] == "dossier?":
                if len(r) != 1:
                    envoie = self.protocole.genere_listeFichiers(self, r[1])
                else:
                    message = "Élément manquant!"
            elif r[0] == "creerDossier?":
                if len(r) != 1:
                    envoie = self.protocole.genere_creerDossier(self, r[1])
                else:
                    message = "Élément manquant!"
            elif r[0]  == "televerser?":
                """envoie = self.protocole.genere_televerserFichier(self)"""
            elif r[0] == "telecharger?":
                """envoie = self.protocole.genere_telechargerFichier(self)"""
            elif r[0] == "supprimerDossier?":
                """envoie = self.protocole.genere_supprimerDossier(self)"""
            elif r[0] == "supprimerFichier?":
                """envoie = self.protocole.genere_supprimerFichier(self)"""
            elif r[0] == "fichier?":
                """TODO:Demander au prof c'est quoi la commande..."""
            elif r[0] == "identiqueFichier?":
                """envoie = self.protocole.genere_fichierIdentique(self)"""
            elif r[0] == "fichierRecent?":
                """envoie = self.protocole.genere_fichierRecent(self)"""
            elif r[0] == "miseAjour":
                if len(r) != 1:
                    self.miseAjour(r[1])
                else:
                    message = "Élément manquant!"
            elif r[0] == "quitter":
                envoie = self.protocole.genere_quitter(self)

            if envoie != None:
                self.serveur.send(envoie)
                message_serveur = self.serveur.receive()
                self.interface.retourMessageServeur(self.protocole.interprete(self, message_serveur))
            else:
                self.interface.retourMessageServeur(message)
            r = input("Commande:").split(" ")

    def synchroniser(self):
        pass

    def miseAjour(self, dossier):
        pass

if __name__ == '__main__':
    prompt = False
    if  sys.argv[3] == "prompt":
        prompt = True

    if sys.argv[2] == "json":
        Client(ProtocoleJson, int(sys.argv[1]), prompt)

    elif sys.argv[2] == "xml":
        Client(ProtocoleXml, int(sys.argv[1]), prompt)
