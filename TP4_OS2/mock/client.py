#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TP4_OS2.mock.serveur import Serveur


class Client:
	"""
	Classe représentant le client
	"""

	def __init__(self, protocole):
		pass

	def bonjour(self):
		Serveur.send(self, "Bonjour")

	def nom(self):
		pass

	def listeDossiers(self, dossier):
		pass

	def listeFichiers(self, fichier):
		pass

	# etc...