import json
from unittest import TestCase
from TP4_OS2.src.protocoleJson import ProtocoleJson


class TestProtocole_json(TestCase):

    def setUp(self):
        self.protocole = ProtocoleJson()

    def test_interprete(self):
        pass

    def test_genere_bonjour(self):
        self.assertTrue(self.protocole.genere_bonjour(), json.dumps({"salutation": "bonjourServeur"}))

    def test_genere_nom(self):
        self.assertTrue(self.protocole.genere_nom(), {"action":"questionNomServeur"})

    def test_genere_listeDossiers(self):
        dossiers = "d1/d2/d3/"
        self.assertTrue(self.protocole.genere_listeDossiers(dossiers), {"questionListeDossiers":dossiers})