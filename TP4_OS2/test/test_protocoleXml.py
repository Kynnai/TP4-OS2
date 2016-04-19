from unittest import TestCase
from TP4_OS2.src.protocoleXml import ProtocoleXml


class TestProtocole_xml(TestCase):
    nom = "a1"
    dossier = "b2"
    dossiers = "d1/d2/d3/"
    fichiers = "d1"
    signature = "c3"
    contenu = "d4"
    date = "2016/04/19"

    PREFIXE_XML = "<?xml version=\"1.0\" ?>"

    def setUp(self):
        self.protocole = ProtocoleXml()

    def test_interprete(self):
        pass

    def test_genere_bonjour_XML(self):
        self.assertTrue(self.protocole.genere_bonjour(), self.PREFIXE_XML + "<bonjourServeur />")

    def test_genere_nom_XML(self):
        self.assertTrue(self.protocole.genere_nom(), self.PREFIXE_XML + "<questionNomServeur />")

    def test_listeDossiers_XML(self):
        self.assertTrue(self.protocole.genere_listeDossiers(self.dossiers), self.PREFIXE_XML + "<questionListeDossiers>" + self.dossiers + "</questionListeDossiers>")

    def test_listeFichiers_XML(self):
        self.assertTrue(self.protocole.genere_listeFichiers(self.fichiers), self.PREFIXE_XML + "<questionListeFichiers>" + self.fichiers + "</questionListeFichiers>")

    def test_creerDossier_XML(self):
        self.assertTrue(self.protocole.genere_creerDossier(self.dossier), self.PREFIXE_XML + "<creerDossier>" + self.dossier + "</creerDossier>")

    def test_televerserFichier_XML(self):
        self.assertTrue(self.protocole.genere_televerserFichier(self.nom, self.dossier, self.signature, self.contenu, self.date),
                        self.PREFIXE_XML + "<televerserFichier>" + "<nom>" + self.nom + "</nom>" + "<dossier>" + self.dossier + "</dossier>" + "<signature>" + self.signature + "</signature>" + \
                         "<contenu>" + self.contenu + "</contenu>" + "<date>" + self.date + "</date>" + "</televerserFichier>")

    def test_telechargerFichier_XML(self):
        self.assertTrue(self.protocole.genere_telechargerFichier(self.nom, self.dossier),
                        self.PREFIXE_XML + "<telechargerFichier>" + "<nom>" + self.nom + "</nom>" + "<dossier>" + self.dossier + "</dossier>" +  "</telechargerFichier>")

    def test_supprimerFichier_XML(self):
        self.assertTrue(self.protocole.genere_supprimerFichier(self.nom, self.dossier),
                        self.PREFIXE_XML + "<supprimerFichier>" + "<nom>" + self.nom + "</nom>" + "<dossier>" + self.dossier + "</dossier>" + "</supprimerFichier>")

    def test_supprimerDossier_XML(self):
        self.assertTrue(self.protocole.genere_supprimerDossier(self.dossier), self.PREFIXE_XML + "<supprimerDossier>" + self.dossier + "</supprimerDossier>")

    def test_questionFichierRecent_XML(self):
        self.assertTrue(self.protocole.genere_questionFichierRecent(self.nom, self.dossier, self.date),
                        self.PREFIXE_XML + "<questionFichierRecent>" + "<nom>" + self.nom + "</nom>" + "<dossier>" + self.dossier + "</dossier>" + "<date>" + self.date + "</date>" + "</questionFichierRecent>")

    def test__questionFichierIdentique(self):
        self.assertTrue(self.protocole.genere_questionFichierIdentique(self.nom, self.dossier, self.signature, self.date),
                        self.PREFIXE_XML + "<questionFichierRecent>" + "<nom>" + self.nom + "</nom>" + "<dossier>" + self.dossier + "</dossier>" + "<signature>" + self.signature + "</signature>" "<date>" + self.date + "</date>" + "</questionFichierRecent>")

    def test_quitter_XML(self):
        self.assertTrue(self.protocole.genere_quitter(),  self.PREFIXE_XML + "<quitter />")