class Room():

    def __init__(self, name):
        self.name = name
        self.guests = []
        self.songs = []


 
    def allow_entry_to_room(self, guest_to_enter):
        self.guests.append(guest_to_enter)

    def kick_out_guest_from_room(self, guest_to_remove):
        self.guests.remove(guest_to_remove)

    def song_added_to_room(self, song_to_add):
        self.songs.append(song_to_add)
