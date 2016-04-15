#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TP4_OS2.src.protocole import Protocole


class ProtocoleXml(Protocole):
    """Interface du langage de communication XML"""

    PREFIXE_XML = "<?xml version=\"1.0\" ?>"

    def __init__(self):
        pass

    def interprete(self, message_serveur):
        #minidom shit
        pass

    def genere_bonjour(self):
        global PREFIXE_XML
        return PREFIXE_XML + "<bonjourServeur />"

    def genere_nom(self):
        global PREFIXE_XML
        return PREFIXE_XML + "questionNomServeur />"

    def genere_listeDossiers(self, dossiers):
        global PREFIXE_XML
        return PREFIXE_XML + "<questionListeDossiers>" + dossiers + "</questionListeDossiers>"

    def genere_listeFichiers(self, fichiers):
        global PREFIXE_XML
        return PREFIXE_XML + "<questionListeFichiers>" + fichiers + "</questionListeFichiers>"

    def genere_creerDossier(self, dossier):
        global PREFIXE_XML
        return PREFIXE_XML + "<creerDossier>" + dossier + "</creerDossier"

    def genere_televerserFichier(self, nom, dossier, signature, contenu, date):
        global PREFIX_XML
        return PREFIX_XML + "<televerserFichier>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "<signature>" + signature + "</signature>" + \
            "<contenu>" + contenu + "</contenu>" + "<date>" + date + "</date>" + "</televerserFichier>"
    