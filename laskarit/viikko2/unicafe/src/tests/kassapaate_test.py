import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self) -> None:
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luodun_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myydyt_lounaat_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_rahaoperaatiot_toimivat_oikein_kun_maksu_riittava(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(vaihtorahat, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_kasvattaa_myytyjen_lounaiden_maaraa_kun_maksu_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_rahaoperaatiot_toimivat_oikein_kun_maksu_ei_riittava(self):
        vaihtorahat = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(vaihtorahat, 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_ei_kasvata_myytyjen_lounaiden_maaraa_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_rahaoperaatiot_toimivat_oikein_kun_maksu_riittava(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(vaihtorahat, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_kasvattaa_myytyjen_lounaiden_maaraa_kun_maksu_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_rahaoperaatiot_toimivat_oikein_kun_maksu_ei_riittava(self):
        vaihtorahat = self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(vaihtorahat, 390)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_ei_kasvata_myytyjen_lounaiden_maaraa_kun_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(390)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # korttitestit alkavat tästä

    # Jos rahaa riittää:

    def test_syo_edullisesti_kortilla_kortin_veloitus_toimii_kun_saldo_riittaa(self):
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(palautus, True)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_syo_maukkaasti_kortilla_kortin_veloitus_toimii_kun_saldo_riittaa(self):
        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(palautus, True)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_syo_edullisesti_kortilla_kasvattaa_edullisia_jos_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_maukkaasti_kortilla_kasvaattaa_maukkaita_jos_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    # Jos rahaa ei riitä:

    def test_syo_edullisesti_korttia_ei_veloiteta_jos_ei_saldoa(self):
        self.maksukortti.saldo = 200
        palaute = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertFalse(palaute)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_korttia_ei_veloiteta_jos_ei_saldoa(self):
        self.maksukortti.saldo = 200
        palaute = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertFalse(palaute)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassapaatteen_rahamaara_ei_muutu_korttiostossa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_lataa_rahaa_kortille_toimii_kun_summa_positiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 1200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)

    def test_lataa_rahaa_kortille_toimii_kun_summa_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)