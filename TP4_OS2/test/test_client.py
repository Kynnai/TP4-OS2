from unittest import TestCase
from TP4_OS2.src.client import Client


class TestClient(TestCase):

    def test_bonjour(self):
        msg = "bonjour"
        Client.bonjour(self)