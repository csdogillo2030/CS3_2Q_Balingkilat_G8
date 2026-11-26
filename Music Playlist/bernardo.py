class Playlist:
    def __init__(self):
        self.songs = []
    
    def add(self, song):
        self.songs.append(song)
    
    def getByTitle(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                return song
        return None
    
    def getAll(self):
        return self.songs
    
    def removeByTitle(self, title):
        song_to_remove = self.getByTitle(title)
        if song_to_remove:
            self.songs.remove(song_to_remove)
            return True
        return False
        
    def count(self):
        return len(self.songs)
