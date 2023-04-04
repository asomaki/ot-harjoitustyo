import unittest
from peli2048 import Peli2048

class TestPeli2048(unittest.TestCase):
    def setUp(self):
        self.game = Peli2048()

    def test_game_loop(self):
        self.assertEqual(str(self.game.loop), "True")
