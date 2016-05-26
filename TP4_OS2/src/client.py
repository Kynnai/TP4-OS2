#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TP4_OS2.mock.serveur import Serveur
from TP4_OS2.src.protocoleJson import ProtocoleJson
from TP4_OS2.src.protocoleXml import ProtocoleXml
#from TP4_OS2.src.interfaceUtilisateur import InterfaceUtilisateur
from TP4_OS2.mock.interfaceUtilisateur import InterfaceUtilisateur

"""
from serveur import Serveur
from protocoleJson import ProtocoleJson
from protocoleXml import ProtocoleXml
from interfaceUtilisateur import InterfaceUtilisateur"""
import sys
import hashlib
import os
import binascii
import xmltodict
import json


class Client:
    """Classe représentant le client"""

    PREFIXE_XML = "<?xml version=\"1.0\" ?>"
    serveur = None
    protocole = None
    interface = None
    nom = None
    dossier = None
    signature = None
    contenu = None
    date = None
    path = None
    rep = "DropBox"

    def __init__(self, protocole, port, prompt):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.protocole = protocole
        self.serveur = Serveur(port)
        self.interface = InterfaceUtilisateur()
        if prompt:
            self.communication()
        else:
            self.synchroniser(self.rep, "./")

    def communication(self):
        r = self.interface.lecteur()
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
                    envoie = self.protocole.genere_listeDossiers(self, "./")
            elif len(r)!= 1:
                if r[0] == "dossier?":
                    self.interface.retourMessageServeur(self.dossierExist(r[1]))
                elif r[0] == "creerDossier?":
                    envoie = self.protocole.genere_creerDossier(self, r[1])
                elif r[0]  == "televerser?":
                    self.initialiserInformationComplexe(r[1])
                    envoie = self.protocole.genere_televerserFichier(self, self.nom, self.dossier, self.signature, self.contenu, self.date)
                elif r[0] == "telecharger?":
                    self.telecharger(r[1])
                    self.interface.retourMessageServeur("OK")
                elif r[0] == "supprimerDossier?":
                    envoie = self.protocole.genere_supprimerDossier(self, r[1])
                elif r[0] == "supprimerFichier?":
                    self.initialiserInformationDeBase(r[1])
                    envoie = self.protocole.genere_supprimerFichier(self, self.nom, self.dossier)
                elif r[0] == "fichier?":
                    self.initialiserInformationDeBase(r[1])
                    envoie = self.protocole.genere_listeFichiers(self, self.dossier)
                    if self.nom != self.dossier:
                        self.serveur.send(envoie)
                        message_serveur = self.serveur.receive()
                        retourInterprete = (self.protocole.interprete(self, message_serveur)).split(" ")
                        if self.nom in retourInterprete:
                            self.interface.retourMessageServeur("oui")
                        else:
                            self.interface.retourMessageServeur("non")
                elif r[0] == "identiqueFichier?" or r[0] == "fichierIdentique?" or r[0] == "telecharger?":
                    self.initialiserInformationComplexe(r[1])
                    envoie = self.protocole.genere_fichierIdentique(self, self.nom, self.dossier, self.signature, self.date)
                elif r[0] == "fichierRecent?":
                    self.initialiserInformationComplexe(r[1])
                    envoie = self.protocole.genere_fichierRecent(self, self.nom, self.dossier, self.date)
                elif r[0] == "miseAjour":
                    self.miseAjour(r[1])
            elif r[0] == "quitter":
                envoie = self.protocole.genere_quitter(self)
            else:
                message = "Élément manquant!"

            if envoie != None and r[0] != "telecharger?" and r[0] != "miseAjour" and r[0] != "dossier?":
                self.serveur.send(envoie)
                message_serveur = self.serveur.receive()
                self.interface.retourMessageServeur(self.protocole.interprete(self, message_serveur))
            elif r[0] == "telecharger?" or r[0] == "fichier?" or r[0] == "miseAjour" or r[0] == "dossier?":
                pass
            else:
                self.interface.retourMessageServeur(message)

            r = input("Commande:").split(" ")
        self.interface.retourMessageServeur("bye")

    def dossierExist(self, dossier):
        envoie = self.protocole.genere_listeDossiers(self, dossier)
        self.serveur.send(envoie)
        message_serveur = self.serveur.receive()
        if "listeDossier" in message_serveur:
            return "oui"
        else:
            return "non"
    def synchroniser(self, pathLocal, pathServeur):
        if self.dossierExist(pathLocal) == "non":
            self.serveur.send(self.protocole.genere_creerDossier(self,pathLocal))
            self.serveur.receive()
            self.miseAjour(pathLocal)

        self.serveur.send(self.protocole.genere_listeDossiers(self,pathServeur))
        message_serveur = self.serveur.receive()
        listDossierServeur = None
        if message_serveur[0:22] == '<?xml version="1.0" ?>':
            listDossierServeur = xmltodict.parse(message_serveur[22:len(message_serveur)])
        else:
            listDossierServeur = json.loads(message_serveur)

        for dossier in listDossierServeur['listeDossiers']['dossier']:
            if not os.path.isdir(dossier):
                os.mkdir(pathLocal+dossier)
                self.miseAjour(dossier)
                self.synchroniser(pathLocal +"/"+ dossier, pathServeur+"/"+ dossier)

        listDossierLocal = next(os.walk(pathLocal))[1]
        for dossierLocal in listDossierLocal:
            if pathServeur != "./":
                self.miseAjour(pathLocal + "/" + dossierLocal)
                self.synchroniser(pathLocal + "/" + dossierLocal, pathServeur + "/" + dossierLocal)
            else:
                self.miseAjour(pathLocal +"/"+ dossierLocal)
                self.synchroniser(pathLocal +"/"+ dossierLocal, pathLocal +"/" + dossierLocal)

    def miseAjour(self, dossier):
        listeFichierLocal = os.listdir(dossier)
        envoie = self.protocole.genere_listeFichiers(self, dossier)
        self.serveur.send(envoie)
        message_serveur = self.serveur.receive()
        monDict = None
        if message_serveur[0:22] == '<?xml version="1.0" ?>':
            monDict = xmltodict.parse(message_serveur[22:len(message_serveur)])
        else:
            monDict = json.loads(message_serveur)
        for fichier in monDict['listeFichiers']['fichier']:
            if not fichier in listeFichierLocal:
                self.telecharger(dossier + "/" + fichier)
            #fichierLocal = (os.path.dirname(os.path.abspath(__doc__)) + "/" + self.dossier)
            self.initialiserInformationComplexe(dossier + "/" + fichier)
            self.serveur.send(self.protocole.genere_fichierIdentique(self, self.nom, self.dossier, self.signature, self.date))
            message_serveur = self.serveur.receive()
            if message_serveur[0:22] == '<?xml version="1.0" ?>':
                reponse = message_serveur[22:len(message_serveur)]
            else:
                reponse = json.loads(message_serveur)['reponse']
            if reponse == "non" or reponse == "<non/>":
                self.serveur.send(self.protocole.genere_fichierRecent(self, self.nom, self.dossier, self.date))
                message_serveur = self.serveur.receive()
                if message_serveur[0:22] == '<?xml version="1.0" ?>':
                    reponse = message_serveur[22:len(message_serveur)]
                else:
                    reponse = json.loads(message_serveur)['reponse']

                if reponse == "oui" or reponse == "<oui/>":
                    self.serveur.send(self.protocole.genere_supprimerFichier(self, self.nom, self.dossier))
                    self.serveur.receive()
                    self.serveur.send(self.protocole.genere_televerserFichier(self, self.nom, self.dossier, self.signature, self.contenu, self.date))
                    self.serveur.receive()
                else:
                    self.telecharger(dossier+"/"+fichier)
                    self.interface.retourMessageServeur(fichier + " MAJ")

        for element in listeFichierLocal:
            if not os.path.isdir(element):
                self.initialiserInformationComplexe(dossier +"/"+ element)
                self.serveur.send(self.protocole.genere_fichierRecent(self, self.nom, self.dossier, self.date))
                message_serveur = self.serveur.receive()
                if message_serveur[0:22] == '<?xml version="1.0" ?>':
                    reponse = message_serveur[22:len(message_serveur)]
                else:
                    reponse = json.loads(message_serveur)['reponse']

                if reponse == "oui" or reponse == "<oui/>":
                    self.serveur.send(self.protocole.genere_supprimerFichier(self, self.nom, self.dossier))
                    self.serveur.receive()
                    self.serveur.send(self.protocole.genere_televerserFichier(self, self.nom, self.dossier, self.signature, self.contenu, self.date))
                    self.serveur.receive()
        self.interface.retourMessageServeur("Mise à jour réussis")

    def telecharger(self, chemin):
        self.initialiserInformationDeBase(chemin)
        envoie = self.protocole.genere_telechargerFichier(self, self.nom, self.dossier)
        self.serveur.send(envoie)
        message_serveur = self.serveur.receive()
        monDict = None
        if message_serveur[0:22] == '<?xml version="1.0" ?>':
            monDict = xmltodict.parse(message_serveur[22:len(message_serveur)])
        else:
            monDict = json.loads(message_serveur)
        fd = open(self.path +"/" + self.dossier + "/" + self.nom, 'wb')
        if monDict['fichier']['contenu'] != None:
            fd.write(binascii.a2b_base64(monDict['fichier']['contenu'].encode(encoding='UTF-8')))
        os.utime(self.path + "/" + self.dossier + "/" + self.nom, (0, int(float(monDict['fichier']['date']))))
        fd.close()

    def initialiserInformationDeBase(self, ligne):
        self.nom = self.obtenirNomFichier(ligne)
        self.dossier = self.obtenirDossier(ligne)

    def initialiserInformationComplexe(self, ligne):
        chemin = self.path + "\ ".strip() + ligne
        self.nom = self.obtenirNomFichier(ligne)
        self.dossier = self.obtenirDossier(ligne)
        self.signature = self.obtenirSignature(chemin)
        self.contenu = self.obtenirContenu(chemin)
        self.date = self.obtenirDateFichier(chemin)

    def obtenirNomFichier(self, ligne):
        dossier = ligne.split("/")
        fichier = dossier[len(dossier) - 1]
        return fichier

    def obtenirDossier(self, ligne):
        dossiers = ligne.split("/")
        retour = ""
        for dossier in dossiers:
            if dossier != dossiers[len(dossiers) - 1]:
                retour = retour + dossier +"/"
        return retour

    def obtenirElements(self, monDict):
        return self.protocole.obtenirElements(self, monDict)

    def obtenirSignature(self, fichier):
        try:
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
            contenu = open(fichier).read()
        except:
            print("Impossible de lire le fichier " + fichier)
            sys.exit(1)
        contenu_utf_8 = contenu.encode(encoding='UTF-8')
        contenu_encode = binascii.b2a_base64(contenu_utf_8)

        contenu_ascii = contenu_encode.decode(encoding='ascii')
        return contenu_ascii

if __name__ == '__main__':
    if not os.path.isdir("DropBox"):
        os.mkdir("DropBox")
    prompt = False
    if  "prompt" in sys.argv:
        prompt = True

    if sys.argv[2] == "json":
        Client(ProtocoleJson, int(sys.argv[1]), prompt)

    elif sys.argv[2] == "xml":
        Client(ProtocoleXml, int(sys.argv[1]), prompt)
