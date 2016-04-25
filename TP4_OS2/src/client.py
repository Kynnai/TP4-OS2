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

    PREFIXE_XML = "<?xml version=\"1.0\" ?>"
    serveur = None
    protocole = None
    interface = None
    nom = None
    dossier = None
    signature = None
    contenu = None
    date = None

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
                    envoie = self.protocole.genere_listeDossiers(self, "./")
            elif len(r)!= 1:
                if r[0] == "dossier?":
                    envoie = self.protocole.genere_listeDossiers(self, r[1])
                elif r[0] == "creerDossier?":
                    envoie = self.protocole.genere_creerDossier(self, r[1])
                elif r[0]  == "televerser?":
                    self.initialiserInformationComplexe(r[1])
                    envoie = self.protocole.genere_televerserFichier(self, self.nom, self.dossier, self.signature, self.contenu, self.date)
                elif r[0] == "telecharger?":
                    self.initialiserInformationDeBase(r[1])
                    print(self.nom)
                    print(self.dossier)
                    envoie = self.protocole.genere_telechargerFichier(self, self.nom, self.dossier)
                    self.serveur.send(envoie)
                    message_serveur = self.serveur.receive()
                    retourInterprete = self.protocole.interprete(self, message_serveur)
                    print(retourInterprete)
                    fd = os.open(os.path.dirname(os.path.abspath(__file__))+self.dossier+"/"+self.nom, os.O_RDWR | os.CREAT)
                    os.write(fd, retourInterprete["contenu"])
                    print(os.write(fd, retourInterprete["contenu"]))
                    os.close(fd)
                    if self.nom in retourInterprete:
                        self.interface.retourMessageServeur("oui")
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
                elif r[0] == "identiqueFichier?" or r[0] == "fichierIdentique?":
                    self.initialiserInformationComplexe(r[1])
                    print(self.nom, self.dossier, self.signature, self.date)
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

            if envoie != None and (r[0] != "telecharger?" or r[0] != "fichier?"):
                self.serveur.send(envoie)
                message_serveur = self.serveur.receive()
                self.interface.retourMessageServeur(self.protocole.interprete(self, message_serveur))
            elif r[0] == "telecharger?" or r[0] == "fichier?":
                pass
            else:
                self.interface.retourMessageServeur(message)

            r = input("Commande:").split(" ")

    def synchroniser(self):
        self.miseAjour("./")

    def miseAjour(self, dossier):
        """self.serveur.send(self.protocole.genere_listeFichiers(dossier))
        listFichiers = self.protocole.interprete(self.serveur.receive()).split(" ")
        for fichier in listFichiers:
            fichierLocal = os.path.dirname(os.path.abspath(__file__)) + "\ ".strip() + dossier + "\ ".strip() + fichier
            self.initialiserInformationComplexe(fichierLocal)
            self.serveur.send(self.protocole.genere_fichierIdentique(self, self.nom, self.dossier, self.signature, self.date))
            if self.interface.retourMessageServeur(self.protocole.interprete(self, self.serveur.receive())) != "oui":
                if self.serveur.send(self.protocole.genere_fichierRecent(self, self.nom, self.dossier, self.signature, self.date)) == "oui":"""

        pass
        """self.serveur.send(self.protocole.genere_listeDossiers(dossier))
        nbDossier = self.protocole.interprete(self.serveur.receive()).split(" ")
        self.serveur.send(self.protocole.genere_listeFichiers(dossier))

        for i in range(0, len(nbDossier)):
            for j in range(0, len(nbFichier)):

    def obtenirNbDossier(self, dossier):
        listeDossier = list
        listeDossier.add(dossier)
        while listeDossier != None:"""


    def initialiserInformationDeBase(self, ligne):
        self.nom = self.obtenirNomFichier(ligne)
        self.dossier = self.obtenirDossier(ligne)

    def initialiserInformationComplexe(self, ligne):
        chemin = os.path.dirname(os.path.abspath(__file__)) + "\ ".strip() + ligne
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
        dossier = ligne.split("/")
        dernier = dossier[len(dossier) - 2]
        return dernier

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
    prompt = False
    if  "prompt" in sys.argv:
        prompt = True

    if sys.argv[2] == "json":
        Client(ProtocoleJson, int(sys.argv[1]), prompt)

    elif sys.argv[2] == "xml":
        Client(ProtocoleXml, int(sys.argv[1]), prompt)
