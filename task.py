import random

class MusicAlbum:

    def __init__(self, title, artist,relese,genre,tracklist):
        self.title =title
        self.artist = artist
        self.relese=relese
        self.genre=genre
        self.tracklist=tracklist

    def info(self):
        print(f'asd {self.genre}')
        print(f'aasd, {self.relese}')
        print(f'zxc, {self.title}')
        print(f'qwe, {self.artist}')
        print(f'dfg, {self.tracklist}')

    def play_random_track(self):
        return random.choice(self.tracklist)


ma = MusicAlbum('Albom', 'Artist', '2000', 'Ganre1', ['first', 'second', 'tri', ' four', 'five'])
ma.info()
print(ma.play_random_track())
