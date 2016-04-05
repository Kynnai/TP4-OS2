#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys


class Protocole:
    """
    Classe représentant le langage de communication avec le serveur.
    """

    def __init__(self):
        pass

    """
    s = socket.socket()
    host = '159.203.9.85'

    MAX_RECV = 1024 * 1024 * 512

    #estJson est un boolean
    def __init__(self, estJson):
        if estJson:
            Protocole.json(self)
        elif not estJson:
            Protocole.xml(self)

    def json(self):
        global s
        global host
        global MAX_RECV

        if __name__ == '__main__':

            if len(sys.argv) < 2:
                print("Ce client prend le numéro du port.")
                sys.exit(1)

            port = int(sys.argv[1])
            s.connect((host, port))

            textes_client = []

            textes_client.append('{"salutation": "bonjourServeur" }')
            textes_client.append("{\"action\": \"questionNomServeur\" }")
            textes_client.append("{\"questionListeDossiers\": \".\" }")
            textes_client.append("{\"questionListeFichiers\": \".\" }")
            textes_client.append("{\"creerDossier\": \"./testCreerDossier\" }")
            textes_client.append('{ "action" : "quitter" }')

            for texte in textes_client:
                print("Texte envoyé au serveur: " + str(texte))
                s.send(texte.encode(encoding='UTF-8'))
                reponse = s.recv(MAX_RECV).decode('UTF-8')
                print('Serveur: ' + reponse.strip())

            s.close

    def xml(self):

        global s
        global host
        global MAX_RECV

        if __name__ == '__main__':

            if len(sys.argv) < 2:
                print("Ce client prend le numéro du port.")
                sys.exit(1)

            port = int(sys.argv[1])
            s.connect((host, port))

            textes_client = list

            textes_client.append("<bonjourServeur />")
            textes_client.append("<questionNomServeur />")
            textes_client.append("<questionListeDossiers>.</questionListeDossiers>")
            textes_client.append("<questionListeFichiers>testDossier</questionListeFichiers>")
            textes_client.append("<creerDossier>./testcreerDossier</creerDossier>")
            textes_client.append("<quitter />")

            for texte in textes_client:
                print("Texte envoyé au serveur: " + str(texte))
                s.send(texte.encode(encoding='UTF-8'))
                reponse = s.recv(MAX_RECV).decode('UTF-8')
                print('Serveur: ' + reponse.strip())

            s.close
            """