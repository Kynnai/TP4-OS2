import json
from unittest import TestCase
from TP4_OS2.src.protocoleJson import ProtocoleJson


class TestProtocole_json(TestCase):
    nom = "a1"
    dossier = "b2"
    dossiers = "d1/d2/d3/"
    fichiers = "f1"
    signature = "c3"
    contenu = "d4"
    date = "2016/04/19"

    def setUp(self):
        self.protocole = ProtocoleJson()

    def test_interprete_bonjour(self):
        self.assertTrue(self.protocole.interprete('{"salutation": "bonjourClient"}'), "oui")

    def test_interprete_nomServeur(self):
        self.assertTrue(self.protocole.interprete('{"nomServeur": "Ubuntu Dropbox 1.0"}'), "Ubuntu Dropbox 1.0")

    def test_interprete_listeDossiers(self):
        self.assertTrue(self.protocole.interprete('{"listeDossiers": {"dossier":["d1/d2","d1/d3","d1/d4"] }}'),
                        "d1/d2 d1/d3 d1/d4")

    def test_interprete_listeFichiers(self):
        self.assertTrue(self.protocole.interprete('{"listeFichiers": {"fichier":["d1/f1","d1/f2","d1/f3"] }}'),
                        "d1/f1 d1/f2 d1/f3")

    def test_interprete_listeDossiers_reponseDossierInexistant(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurDossierInexistant"}'),"erreurDossierInexistant")

    def test_interprete_listeDossiers_reponseDossierLecture(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurDossierLecture"}'),"erreurDossierLecture")

    def test_interprete_creerDossier(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "ok"}'), "ok")

    def test_interprete_creerDossier_reponseDossierExiste(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurDossierExiste"}'), "erreurDossierExiste")

    def test_interprete_creerDossier_reponseDossierInexistant(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurDossierInexistant"}'), "erreurDossierInexistant")

    def test_interprete_televerserFichier(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "ok"}'), "ok")

    def test_interprete_televerserFichier_reponseDossierExiste(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurFichierExiste"}'), "erreurFichierExiste")

    def test_interprete_telechargerFichier(self):
        self.assertTrue(self.protocole.interprete('{"fichier":{"signature":"s1","contenu":"c1", "date":"2015/04/19"}}'),
                        "s1 c1 2015/04/19")

    def test_interprete_telechargerFichier_reponseFichierInexistant(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurFichierInexistant"}'), "erreurFichierInexistant")

    def test_interprete_telechargerFichier_reponseFichierLecture(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurFichierLecture"}'), "erreurFichierLecture")

    def test_interprete_supprimerFichier(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "ok"}'), "ok")

    def test_interprete_supprimerFichier_reponseDossierInexistant(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurDossierInexistant"}'), "erreurDossierInexistant")

    def test_interprete_supprimerFichier_reponseFichierLecture(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurFichierLecture"}'), "erreurFichierLecture")

    def test_interprete_supprimerDossier(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "ok"}'), "ok")

    def test_interprete_fichierRecent_oui(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "oui"}'), "oui")

    def test_interprete_fichierRecent_non(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "non"}'), "non")

    def test_interprete_fichierRecent_FichierInexistant(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurFichierInexistant"}'), "erreurFichierInexistant")

    def test_interprete_fichierRecent_FichierLecture(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "erreurFichierLecture"}'), "erreurFichierLecture")

    def test_interprete_fichierIdentique_oui(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "oui"}'), "oui")

    def test_interprete_fichierIdentique_non(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "non"}'), "non")

    def test_interprete_quitter(self):
        self.assertTrue(self.protocole.interprete('{"reponse": "bye"}'), "bye")

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