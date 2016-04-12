from unittest import TestCase

#TODO: désactiver pour MOCK
from TP4_OS2.mock.serveur import Serveur

#TODO: désactiver pour SERVEUR
#from TP4_OS2.src.serveur import Serveur


class TestServeur(TestCase):
    def test_send(self):
        Serveur.send(self, 'Bonjour')
        expectMsg = "Bonjour maitre!"
        assert Serveur.receive(self) == expectMsg
