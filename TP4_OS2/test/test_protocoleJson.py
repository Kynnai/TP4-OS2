import json
from unittest import TestCase
from TP4_OS2.src.protocoleJson import ProtocoleJson


class TestProtocole_json(TestCase):
    nom = "a1"
    dossier = "b2"
    dossiers = "d1/d2/d3/"
    fichiers = "d1"
    signature = "c3"
    contenu = "d4"
    date = "2016/04/19"

    def setUp(self):
        self.protocole = ProtocoleJson()

    def test_interprete(self):
        pass

    def test_genere_bonjour(self):
        self.assertTrue(self.protocole.genere_bonjour(), json.dumps({"salutation": "bonjourServeur"}))

    def test_genere_nom(self):
        self.assertTrue(self.protocole.genere_nom(), json.dumps({"action":"questionNomServeur"}))

    def test_genere_listeDossiers(self):
        self.assertTrue(self.protocole.genere_listeDossiers(self.dossiers), json.dumps({"questionListeDossiers":self.dossiers}))

    def test_genere_listeFichiers(self):
        self.assertTrue(self.protocole.genere_listeFichiers(self.fichiers), json.dumps({"questionListeFichiers":self.fichiers}))

    def test_genere_creerDossier(self):
        self.assertTrue(self.protocole.genere_creerDossier(self.dossier), json.dumps({"creerDossier":self.dossier}))

    def test_genere_televerserFichier(self):


        self.assertTrue(self.protocole.genere_televerserFichier(self.nom, self.dossier, self.signature, self.contenu, self.date),
                        json.dumps({"televerserFichier":
                                        {"nom":self.nom, "dossier":self.dossier, "signature":self.signature, "contenu":self.contenu, "date":self.date}}))

    def test_genere_telechargerFichier(self):
        self.assertTrue(self.protocole.genere_telechargerFichier(self.nom, self.dossier),
                        json.dumps({"telechargerFichier": {"nom":self.nom, "dossier":self.dossier}}))

    def test_genere_supprimerFichier(self):
        self.assertTrue(self.protocole.genere_supprimerFichier(self.nom, self.dossier),
                        json.dumps({"supprimerFichier": {"nom":self.nom, "dossier":self.dossier}}))

    def test_genere_supprimerDossier(self):
        self.assertTrue(self.protocole.genere_supprimerDossier(self.dossier),
                        json.dumps({"supprimerDossier":self.dossier}))

    def test_genere_fichierRecent(self):
        self.assertTrue(self.protocole.genere_fichierRecent(self.nom, self.dossier, self.date),
                        json.dumps({"questionFichierRecent":
                                        {"nom": self.nom, "dossier": self.dossier, "date": self.date}}))

    def test_genere_fichierIdentique(self):
        self.assertTrue(self.protocole.genere_fichierIdentique(self.nom, self.dossier, self.signature, self.date),
                        json.dumps({"questionFichierIdentique":
                                        {"nom":self.nom, "dossier":self.dossier, "signature":self.signature, "date":self.date}}))

    def test_genere_quitter(self):
        self.assertTrue(self.protocole.genere_quitter(),json.dumps({"action": "quitter"}))