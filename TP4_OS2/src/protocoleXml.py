#!/usr/bin/python3
# -*- coding: utf-8 -*-

#TODO:lien pour installer la libraries https://github.com/martinblech/xmltodict
import xmltodict
#from protocole import Protocole
from TP4_OS2.src.protocole import Protocole


class ProtocoleXml(Protocole):
    """IPREFIXE_XML = "<?xml version=\"1.0\" ?>"nterface du langage de communication XML"""

    PREFIXE_XML = "<?xml version=\"1.0\" ?>"
    client = None
    def __init__(self):
        pass

    def interprete(self, message_serveur):
        interpreteur = xmltodict.parse(message_serveur[22:len(message_serveur)])
        if ("bonjourClient" in interpreteur):
            return "oui"
        elif ("nomServeur" in interpreteur):
            return interpreteur["nomServeur"]
        elif ("listeDossiers" in interpreteur):
            if interpreteur["listeDossiers"] == None:
                return "oui"
            else:
                dossier = self.obtenirElements(interpreteur["listeDossiers"]["dossier"])
                return dossier
        elif ("ok" in interpreteur):
            return "ok"
        elif ("erreurDossierExiste" in interpreteur):
            return "erreurDossierExiste"
        elif ("erreurDossierInexistant" in interpreteur):
            return "erreurDossierInexistant"
        elif ("erreurDossierLecture" in interpreteur):
            return "erreurDossierLecture"
        elif ("erreurFichierExiste" in interpreteur):
            return "erreurFichierExiste"
        elif ("erreurSignature" in interpreteur):
            return "erreurSignature"
        elif ("erreurFichierInexistant" in interpreteur):
            return "erreurFichierInexistant"
        elif ("erreurFichierLecture" in interpreteur):
            return "erreurFichierLecture"
        elif ("bye" in interpreteur):
            return "bye"
        elif ("oui" in interpreteur):
            return "oui"
        elif ("non" in interpreteur):
            return "non"
        elif ("listeFichiers" in interpreteur):
            fichiers = self.obtenirElements(interpreteur["listeFichiers"]["fichier"])
            return fichiers
        elif ("fichier" in interpreteur):
            test = self.obtenirElements(interpreteur["fichier"])
            print(test)
            return test

    def obtenirElements(self, monDict):
        retourStr = ""
        print(monDict)
        #for i in range(0, len(monDict)):
        for element in monDict:
            retourStr += element + " "
            print(retourStr)

        return retourStr

    def genere_bonjour(self):
        return self.PREFIXE_XML + "<bonjourServeur />"

    def genere_nom(self):
        return self.PREFIXE_XML + "<questionNomServeur />"

    def genere_listeDossiers(self, dossiers):
        return self.PREFIXE_XML + "<questionListeDossiers>" + dossiers + "</questionListeDossiers>"

    def genere_listeFichiers(self, fichiers):
        return self.PREFIXE_XML + "<questionListeFichiers>" + fichiers + "</questionListeFichiers>"

    def genere_creerDossier(self, dossier):
        return self.PREFIXE_XML + "<creerDossier>" + dossier + "</creerDossier>"

    def genere_televerserFichier(self, nom, dossier, signature, contenu, date):
        return self.PREFIXE_XML + "<televerserFichier>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "<signature>" + signature + "</signature>" + \
            "<contenu>" + contenu + "</contenu>" + "<date>" + date + "</date>" + "</televerserFichier>"

    def genere_telechargerFichier(self, nom, dossier):
        return self.PREFIXE_XML + "<telechargerFichier>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" +  "</telechargerFichier>"

    def genere_supprimerFichier(self, nom, dossier):
        return self.PREFIXE_XML + "<supprimerFichier>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "</supprimerFichier>"

    def genere_supprimerDossier(self, dossier):
        return self.PREFIXE_XML + "<supprimerDossier>" + dossier + "</supprimerDossier>"

    def genere_fichierRecent(self, nom, dossier, date):
        return self.PREFIXE_XML + "<questionFichierRecent>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "<date>" + date + "</date>" + "</questionFichierRecent>"

    def genere_fichierIdentique(self, nom, dossier, signature,  date):
        return self.PREFIXE_XML + "<questionFichierIdentique>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "<signature>" + signature + "</signature>" "<date>" + date + "</date>" + "</questionFichierIdentique>"

    def genere_quitter(self):
        return self.PREFIXE_XML + "<quitter />"