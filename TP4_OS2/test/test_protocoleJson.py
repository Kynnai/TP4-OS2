import json
from unittest import TestCase
from TP4_OS2.src.protocoleJson import ProtocoleJson


class TestProtocole_json(TestCase):

    def setUp(self):
        self.protocole = ProtocoleJson()

    def test_interprete(self):
        pass

    def test_genere_bonjour(self):
        retourAttendu = json.dumps({"salutation": "bonjourServeur"})

        self.assertTrue(self.protocole.genere_bonjour(), retourAttendu)

    def test_genere_nom(self):
        retourAttendu = json.dumps({"action":"questionNomServeur"})

        self.assertTrue(self.protocole.genere_nom(), retourAttendu)

    def test_genere_listeDossiers(self):
        dossiers = "d1/d2/d3/"

        retourAttendu = json.dumps({"questionListeDossiers":dossiers})

        self.assertTrue(self.protocole.genere_listeDossiers(dossiers), retourAttendu)

    def test_genere_listeFichiers(self):
        fichiers = "d1"

        retourAttendu = json.dumps({"questionListeFichiers": fichiers})

        self.assertTrue(self.protocole.genere_listeFichiers(fichiers), retourAttendu)

    def genere_creerDossier(self):
        dossier = "d1"

        retourAttendu = json.dumps({"creerDossier": dossier})

        self.assertTrue(self.protocole.genere_creerDossier(dossier), retourAttendu)

    def genere_televerserFichier(self):
        nom = "a1"
        dossier = "b2"
        signature = "c3"
        contenu = "d4"
        date = "2016/04/19"

        retourAttendu = json.dumps({"televerserFichier": {"nom": nom, "dossier": dossier, "signature": signature, "contenu": contenu, "date": date}})

        self.assertTrue(self.protocole.genere_televerserFichier(nom, dossier, signature, contenu, date), retourAttendu)

    def genere_supprimerFichier(self):
        nom = "a1"
        dossier = "b2"

        retourAttendu = json.dumps({"supprimerFichier": {"nom": nom, "dossier": dossier}})

        self.assertTrue(self.protocole.genere_supprimerFichier(nom, dossier), retourAttendu)