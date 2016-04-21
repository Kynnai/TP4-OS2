#!/usr/bin/python3
# -*- coding: utf-8 -*-

from serveur import Serveur
from protocoleJson import ProtocoleJson
from protocoleXml import ProtocoleXml
from interfaceUtilisateur import InterfaceUtilisateur
import sys
import hashlib
import os
import binascii


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
                    envoie = self.protocole.genere_listeDossiers(self, "./")
            elif r[0] == "dossier?":
                if len(r) != 1:
                    envoie = self.protocole.genere_listeDossiers(self, r[1])
                else:
                    message = "Élément manquant!"
            elif r[0] == "creerDossier?":
                if len(r) != 1:
                    envoie = self.protocole.genere_creerDossier(self, r[1])
                else:
                    message = "Élément manquant!"
            elif r[0]  == "televerser?":
                if len(r) != 1:
                    chemin = os.path.dirname(os.path.abspath(__file__))+ "\ ".strip() + r[1]
                    nom = self.obtenirNomFichier(r[1])
                    dossier = self.obtenirDossier(r[1])
                    signature = self.obtenirSignature(chemin)
                    contenu = self.obtenirContenu(chemin)
                    date = self.obtenirDateFichier(chemin)
                    envoie = self.protocole.genere_televerserFichier(self, nom, dossier, signature, contenu, date)
                else:
                    message = "Élément manquant!"
            elif r[0] == "telecharger?":
                """envoie = self.protocole.genere_telechargerFichier(self)"""
            elif r[0] == "supprimerDossier?":
                envoie = self.protocole.genere_supprimerDossier(self, r[1])
            elif r[0] == "supprimerFichier?":
                if len(r) != 1:
                    nom = self.obtenirNomFichier(r[1])
                    dossier = self.obtenirDossier(r[1])
                    envoie = self.protocole.genere_supprimerFichier(self, nom, dossier)
                else:
                    message = "Élément manquant!"
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
        self.interface.retourMessageServeur("Méthode Sync non fonctionnel")

    def miseAjour(self, dossier):
        pass

    def obtenirNomFichier(self, ligne):
        dossier = ligne.split("/")
        fichier = dossier[len(dossier) - 1]
        return fichier

    def obtenirDossier(self, ligne):
        dossier = ligne.split("/")
        dernier = dossier[len(dossier) - 2]
        return dernier

    def obtenirElements(self, monDict):
        return self.protocole.obtenirElements(self, monDict)

    def obtenirSignature(self, fichier):
        try:
            # Voici comment lire le contenu d'un fichier
            contenu = open(fichier).read()
        except:
            print("Impossible de lire le fichier " + fichier)
            sys.exit(1)
        contenu_utf_8 = contenu.encode(encoding='UTF-8')
        objet_md5 = hashlib.md5()
        objet_md5.update(contenu_utf_8)
        signature_contenu = objet_md5.hexdigest()

        return signature_contenu

    def obtenirDateFichier(self, fichier):
        try:
            fichier_stat = os.stat(fichier)
        except:
            print("Impossible de lire le fichier " + fichier)
            sys.exit(1)

        date_modification = str(fichier_stat.st_mtime)
        return date_modification

    def obtenirContenu(self, fichier):
        try:
            # Voici comment lire le contenu d'un fichier
            contenu = open(fichier).read()
        except:
            print("Impossible de lire le fichier " + fichier)
            sys.exit(1)
        contenu_utf_8 = contenu.encode(encoding='UTF-8')
        contenu_encode = binascii.b2a_base64(contenu_utf_8)

        contenu_ascii = contenu_encode.decode(encoding='ascii')
        return contenu_ascii

if __name__ == '__main__':
    prompt = False
    if  "prompt" in sys.argv:
        prompt = True

    if sys.argv[2] == "json":
        Client(ProtocoleJson, int(sys.argv[1]), prompt)

    elif sys.argv[2] == "xml":
        Client(ProtocoleXml, int(sys.argv[1]), prompt)
