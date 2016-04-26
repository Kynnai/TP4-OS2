#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import
#import sl4a
import time
import os


class InterfaceUtilisateur:

    droid = None

    def __init__(self):
        #self.droid = sl4a.Android()
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
        return response['which']

    def demandeIpEtPortServeurAlert(self):
        if os.path.exists("/sdcard/com.hipipal.qpyplus/scripts3/serveurConfig.txt"):
            file = open("/sdcard/com.hipipal.qpyplus/scripts3/serveurConfig.txt")
            lines = file.readlines()
            return (lines[0], lines[1])
        else:
            title1 = "Adresse Ip"
            message1 = "Veuillez spécifier l'ip  du serveur."
            ip = self.droid.dialogGetInput(title1, message1).result
            title2 = "Port serveur"
            message2 = "Veuillez spécifier le port du serveur."
            port = self.droid.dialogGetInput(title2, message2).result
            if(self.demandeCreationFichierServeurConfig() == "positive"):
                file = open("/sdcard/com.hipipal.qpyplus/scripts3/serveurConfig.txt", 'w')
                file.writelines([ip + '\n', port + '\n'])
            return (ip, port)

    def demandeCreationFichierServeurConfig(self):
        title = 'Attention'
        message = ("Voulez-vous enregistrer cette information ?")
        self.droid.dialogCreateAlert(title, message)
        self.droid.dialogSetPositiveButtonText('Oui')
        self.droid.dialogSetNegativeButtonText('Non')
        self.droid.dialogSetNeutralButtonText('Annuler')
        self.droid.dialogShow()
        response = self.droid.dialogGetResponse().result
        return response['which']

    def spinnerDeMiseAJour(self):
        title = 'Mise à jour des dossiers et fichiers avec le serveur.'
        message = 'Veuillez patientez...'
        self.droid.dialogCreateSpinnerProgress(title, message)
        self.droid.dialogShow()
        time.sleep(2)
        self.droid.dialogDismiss()
        return True

    def messageMiseÀJourEffectue(self):
        title = 'Mise à jour effectuée'
        message = 'Vos dossiers et fichiers ont été synchronisés avec le serveur.'
        self.droid.dialogCreateAlert(title, message)
        self.droid.dialogSetPositiveButtonText('Continue')
        self.droid.dialogShow()
        response = self.droid.dialogGetResponse().result
        return response['which'] == 'positive'

    def messageMiseÀJourErreur(self):
        title = 'Erreur'
        message = 'Une erreur a été rencontrée lors de la mise à jour des dossiers et fichiers.'
        self.droid.dialogCreateAlert(title, message)
        self.droid.dialogSetPositiveButtonText('Continue')
        self.droid.dialogShow()
        response = self.droid.dialogGetResponse().result
        return response['which'] == 'positive'

