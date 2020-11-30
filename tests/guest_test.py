import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.james_brown = Guest('James Brown')

    def test_we_have_a_singer_to_sing(self):
        self.assertEqual('James Brown', self.james_brown.name)
