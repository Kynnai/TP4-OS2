#!/usr/bin/python3
# -*- coding: utf-8 -*-

from TP4_OS2.src.interfaceUtilisateur import InterfaceUtilisateur


class Serveur:
	"""
	Cette classe fait l'interface avec le serveur
	"""

	def __init__(self, host, port):
		pass

	def send(self, texte):
		pass

	def receive(self, texte):
		return texte

	def close(self):
		pass

	# etc...