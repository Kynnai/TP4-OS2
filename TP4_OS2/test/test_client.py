from unittest import TestCase
from TP4_OS2.src.client import Client
from TP4_OS2.src.protocoleJson import ProtocoleJson

#TODO: Ne pas oublier de remplacer serveur par son mock

class TestClient(TestCase):
    def setUp(self):
        self.protocole = ProtocoleJson()
        self.client = Client(self.protocole, "50005", True)

    def test_communication_connecter(self):
        self.client.interface.ligne = "connecter?"
        self.assertTrue(self.client.communication)