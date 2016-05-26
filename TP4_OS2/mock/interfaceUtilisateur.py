#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import
#import sl4a
import time
import os


class InterfaceUtilisateur:

    droid = None
    ligne = None

    def __init__(self):
        #self.droid = sl4a.Android()
        pass

    def retourMessageServeur(self, texte):
        print("Réponse serveur : " + texte)

    def mockLecteur(self, texte):
        self.ligne = texte

    def lecteur(self):
        return self.ligne

    #TODO: Puisqu'on peut exécuter plusieurs fois le script -> pour garder l'arbo précédente
    def demandeSuppArboDropbox(self):
        pass

    def demandeIpEtPortServeurAlert(self):
        pass

    def demandeCreationFichierServeurConfig(self):
        pass

    def spinnerDeMiseAJour(self):
        pass

    def messageMiseÀJourEffectue(self):
        pass

    def messageMiseÀJourErreur(self):
        pass

