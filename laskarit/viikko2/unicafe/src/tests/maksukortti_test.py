import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_luodun_kortin_saldo_on_oikein_alussa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_ota_rahaa_toimii_kun_saldoa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
    
    def test_ota_rahaa_ei_tee_mitaan_jos_saldoa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_ota_rahaa_palauttaa_True_jos_on_saldoa(self):
        riittaa_output = self.maksukortti.ota_rahaa(500)

        self.assertEqual(riittaa_output, True)
    
    def test_ota_rahaa_palauttaa_False_jos_ei_saldoa(self):
        ei_riita_output = self.maksukortti.ota_rahaa(2000)

        self.assertEqual(ei_riita_output, False)

