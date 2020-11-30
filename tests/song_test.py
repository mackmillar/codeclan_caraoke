import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.papas_got_a_brand_new_bag = Song("papa's got a brand new bag")

    def test_we_have_a_song_to_sing(self):
        self.assertEqual("papa's got a brand new bag", self.papas_got_a_brand_new_bag.name)