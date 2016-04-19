#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json

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
        r = {"questionListeDossiers":dossiers}
        return json.dumps({"questionListeDossiers" : dossiers})

    def genere_listeFichiers(self, fichiers):
        return json.dumps({"questionListeFichiers": fichiers})

    def genere_creerDossier(self, dossier):
        return json.dumps({"creerDossier":dossier})

    def genere_televerserFichier(self, nom, dossier, signature, contenu, date):
        return json.dumps({"televerserFichier":{"nom":nom, "dossier":dossier, "signature":signature, "contenu":contenu, "date":date}})

    def genere_supprimerFichier(self, nom, dossier):
        return json.dumps({"supprimerFichier":{"nom":nom, "dossier":dossier}})