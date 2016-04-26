#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
#pour les tests
#from TP4_OS2.src.protocole import Protocole

#pour le serveur
from protocole import Protocole


class ProtocoleJson(Protocole):
    """Interface du langage de communication JSON"""

    def __init__(self):
        pass

    def interprete(self, message_serveur):
        interpreteur = json.loads(message_serveur)
        if("salutation" in interpreteur and interpreteur["salutation"] == "bonjourClient"):
            return "oui"
        elif("nomServeur" in interpreteur):
            return interpreteur["nomServeur"]
        elif ("listeDossiers" in interpreteur):
            dossier = self.obtenirElements(interpreteur["listeDossiers"]["dossier"])
            if dossier == "":
                return "Oui"
            else:
                return dossier
        elif ("reponse" in interpreteur):
            return interpreteur["reponse"]
        elif ("listeFichiers" in interpreteur):
            fichiers = self.obtenirElements(interpreteur["listeFichiers"]["fichier"])
            if fichiers == "":
                return "oui"
            else:
                return fichiers
        elif ("fichier" in interpreteur):
            return self.obtenirElements(interpreteur["fichier"])

    def obtenirElements(self, monDict):
        retourStr = ""
        for element in monDict:
            retourStr += element + " "
        return retourStr

    def genere_bonjour(self):
        return json.dumps({"salutation":"bonjourServeur"})

    def genere_nom(self):
        return json.dumps({"action":"questionNomServeur"})

    def genere_listeDossiers(self, dossiers):
        return json.dumps({"questionListeDossiers" : dossiers})

    def genere_listeFichiers(self, fichiers):
        return json.dumps({"questionListeFichiers": fichiers})

    def genere_creerDossier(self, dossier):
        return json.dumps({"creerDossier":dossier})

    def genere_televerserFichier(self, nom, dossier, signature, contenu, date):
        return json.dumps({"televerserFichier":
                               {"nom":nom, "dossier":dossier, "signature":signature, "contenu":contenu, "date":date}})

    def genere_telechargerFichier(self, nom, dossier):
        return json.dumps({"telechargerFichier":{"nom": nom, "dossier": dossier}})

    def genere_supprimerFichier(self, nom, dossier):
        return json.dumps({"supprimerFichier":{"nom":nom, "dossier":dossier}})

    def genere_supprimerDossier(self, dossier):
        return json.dumps({"supprimerDossier":dossier})

    def genere_fichierRecent(self, nom, dossier, date):
        return json.dumps({"questionFichierRecent":
                               {"nom": nom, "dossier": dossier, "date":date}})

    def genere_fichierIdentique(self, nom, dossier, signature, date):
        return json.dumps({"questionFichierIdentique":
                               {"nom": nom, "dossier": dossier, "signature":signature, "date": date}})

    def genere_quitter(self):
        return json.dumps({"action":"quitter"})