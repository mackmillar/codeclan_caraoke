import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.super_cube = Room('Super Cube')

        self.guest_1 = Guest("James Brown")

        self.song_1 = Song("papa's got a brand new bag")

    def test_we_have_a_place_to_sing(self):
        self.assertEqual('Super Cube', self.super_cube.name)

    def test_check_in_guest_to_room(self):
        self.super_cube.allow_entry_to_room(self.guest_1)
        self.assertEqual(1, len(self.super_cube.guests))

    def test_kick_out_guest_from_room(self):
        self.super_cube.allow_entry_to_room(self.guest_1)
        self.super_cube.kick_out_guest_from_room(self.guest_1)
        self.assertEqual(0, len(self.super_cube.guests))

    def test_song_added_to_room(self):
        self.super_cube.song_added_to_room(self.song_1)
        self.assertEqual(1, len(self.super_cube.songs))

    