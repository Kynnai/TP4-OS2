#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TP4_OS2.src.protocole import Protocole


class ProtocoleJson(Protocole):
    """Interface du langage de communication JSON"""

    def __init__(self):
        pass

    def interprete(self, message_serveur):
        pass

    def genere_bonjour(self):
        return {"salutation":"bonjourServeur"}

    def genere_nom(self):
        return {"action":"questionNomServeur"}

    def genere_listeDossiers(self, dossiers):
        return {"questionListeDossiers":dossiers}

    def genere_listeFichiers(self, fichiers):
        return {"questionListeFichiers": fichiers}

    def genere_creerDossier(self, dossier):
        return {"creerDossier":dossier}

    def genere_televerserFichier(self, nom, dossier, signature, contenu, date):
        return {"televerserFichier":{"nom":nom, "dossier":dossier, "signature":signature, "contenu":contenu, "date":date}}

    def genere_supprimerFichier(self, nom, dossier):
        return {"supprimerFichier":{"nom":nom, "dossier":dossier}}