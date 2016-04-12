#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TP4_OS2.mock.interfaceUtilisateur import InterfaceUtilisateur


class Serveur:
	"""
	Cette classe fait l'interface avec le serveur
	"""

	def __init__(self, host, port):
		pass

	def send(self, texte):
		pass

	def receive(self):
		return "Bonjour maitre!"

	def close(self):
		pass

	# etc...