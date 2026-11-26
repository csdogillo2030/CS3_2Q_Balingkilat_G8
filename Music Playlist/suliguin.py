# Suliguin, Jose Santiago T.

class Playlist:
    def __init__(self):
        self.song = []
    def add(self, song):
        self.song.append(song)
    def getByTitle(self, title):
        for i in self.song:
            if i.title == title:
                return i
    def getAll(self):
        return self.song
    def removeByTitle(self, title):
        for i in self.song:
            if i.title == title:
                self.song.remove(i)
                return True
        else:
            return False
    def count(self):
        return len(self.song)
