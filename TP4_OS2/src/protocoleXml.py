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
        return PREFIXE_XML + "<creerDossier>" + dossier + "</creerDossier>"

    def genere_televerserFichier(self, nom, dossier, signature, contenu, date):
        global PREFIX_XML
        return PREFIX_XML + "<televerserFichier>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "<signature>" + signature + "</signature>" + \
            "<contenu>" + contenu + "</contenu>" + "<date>" + date + "</date>" + "</televerserFichier>"

    def genere_telechargerFichier(self, nom, dossier):
        global PREFIXE_XML
        return PREFIXE_XML + "<telechargerFichier>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" +  "</telechargerFichier>"

    def genere_supprimerFichier(self, nom, dossier):
        global PREFIXE_XML
        return PREFIXE_XML + "<supprimerFichier>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "</supprimerFichier>"

    def genere_supprimerDossier(self, dossier):
        global PREFIXE_XML
        return PREFIXE_XML + "<supprimerDossier>" + dossier + "</supprimerDossier>"

    def genere_questionFichierRecent(self, nom, dossier, date):
        global PREFIXE_XML
        return PREFIXE_XML + "<questionFichierRecent>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "<date>" + date + "</date>" + "</questionFichierRecent>"

    def genere_questionFichierIdentique(self, nom, dossier, signature,  date):
        global PREFIXE_XML
        return PREFIXE_XML + "<questionFichierRecent>" + "<nom>" + nom + "</nom>" + "<dossier>" + dossier + "</dossier>" + "<signature>" + signature + "</signature>" "<date>" + date + "</date>" + "</questionFichierRecent>"

    def genere_quitter(self):
        global PREFIXE_XML
        return PREFIXE_XML + "<quitter />"