#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import
import sl4a
import time


class InterfaceUtilisateur:

    droid = sl4a.Android()

    def __init__(self):
        pass

    def retourMessageServeur(self, texte):
        print("Réponse serveur : " + texte)

    #TODO: Puisqu'on peut exécuter plusieurs fois le script -> pour garder l'arbo précédente
    def demandeSuppArboDropbox(self):
        title = 'Attention'
        message = ("Voulez-vous supprimer l'arborescence déjà existante ?")
        self.droid.dialogCreateAlert(title, message)
        self.droid.dialogSetPositiveButtonText('Oui')
        self.droid.dialogSetNegativeButtonText('Non')
        self.droid.dialogSetNeutralButtonText('Annuler')
        self.droid.dialogShow()
        response = self.droid.dialogGetResponse().result
        return response['which'] in ('positive', 'negative', 'neutral')

    def getServerIpAlert(self):
        message = "Veuillez spécifier l'ip  du serveur."
        self.droid.dialogCreateAlert("Besoin d'information", message)
        self.droid.dialogSetPositiveButtonText('Ok')
        self.droid.dialogSetNeutralButtonText('Annuler')
        self.droid.dialogShow()
        self.droid.dialogGetResponse()
        #result = self.droid.getInput('Chat', 'Enter a message').result
        #serverIp = self.droid.dialogGetResponse('Server Ip')
       # port = self.droid.dialogGetResponse('Port')
