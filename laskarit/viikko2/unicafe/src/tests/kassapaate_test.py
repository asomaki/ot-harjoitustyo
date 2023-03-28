import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kassapaate_luotu_oikein(self):
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(self.kassa.maukkaat), "0")

    def test_syo_edullisesti_kateisella(self):
        self.kassa.syo_edullisesti_kateisella(300)

        self.assertEqual(str(self.kassa.edulliset), "1")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100240")
        self.assertEqual(str(self.kassa.syo_edullisesti_kateisella(300)), "60")

    def test_syo_maukkaasti_kateisella(self):
        self.kassa.syo_maukkaasti_kateisella(500)

        self.assertEqual(str(self.kassa.maukkaat), "1")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100400")
        self.assertEqual(str(self.kassa.syo_maukkaasti_kateisella(500)), "100")

    def test_syo_edullisesti_ei_riittavasti_kateista(self):
        self.kassa.syo_edullisesti_kateisella(200)

        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassa.syo_edullisesti_kateisella(200)), "200")

    def test_syo_maukkaasti_ei_riittavasti_kateista(self):
        self.kassa.syo_maukkaasti_kateisella(300)

        self.assertEqual(str(self.kassa.maukkaat), "0")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")
        self.assertEqual(str(self.kassa.syo_maukkaasti_kateisella(300)), "300")

    def test_syo_edullisesti_kortilla(self):
        kortti = Maksukortti(300)

        self.assertEqual(str(self.kassa.syo_edullisesti_kortilla(kortti)), "True")
        self.assertEqual(str(self.kassa.edulliset), "1")
        self.assertEqual(str(kortti), "Kortilla on rahaa 0.60 euroa")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

    def test_syo_maukkaasti_kortilla(self):
        kortti = Maksukortti(500)

        self.assertEqual(str(self.kassa.syo_maukkaasti_kortilla(kortti)), "True")
        self.assertEqual(str(self.kassa.maukkaat), "1")
        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

    def test_syo_edullisesti_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(200)

        self.assertEqual(str(self.kassa.syo_edullisesti_kortilla(kortti)), "False")
        self.assertEqual(str(self.kassa.edulliset), "0")
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_syo_maukkaasti_kortilla_ei_tarpeeksi_rahaa(self):
        kortti = Maksukortti(300)

        self.assertEqual(str(self.kassa.syo_maukkaasti_kortilla(kortti)), "False")
        self.assertEqual(str(self.kassa.maukkaat), "0")
        self.assertEqual(str(kortti), "Kortilla on rahaa 3.00 euroa")

    def test_lataa_rahaa_kortille(self):
        kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(kortti, 2000)

        self.assertEqual(str(kortti), "Kortilla on rahaa 21.00 euroa")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "102000")


    def test_ei_voi_ladata_negatiivista_summaa_kortille(self):
        kortti = Maksukortti(100)
        self.kassa.lataa_rahaa_kortille(kortti, -100)

        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
        self.assertEqual(str(self.kassa.kassassa_rahaa), "100000")

