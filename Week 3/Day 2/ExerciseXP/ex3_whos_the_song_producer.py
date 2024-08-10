class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def split_lyrics(self):
        for line in self.lyrics:
            parts = line.split(",")
            for part in parts:
                print(part.strip())

    def sing_me_a_song(self):
        return self.split_lyrics()


stairway_lyrics = [
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven",
]


stairway = Song(stairway_lyrics)
stairway.sing_me_a_song()
