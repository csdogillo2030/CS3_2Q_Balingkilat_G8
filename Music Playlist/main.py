from playlists import Playlist
from songs import Song

def main():
    my_playlist = Playlist()
    
    while True:
        print(" ---- Dotify ---- ")
        print(f"Total Songs In Playlist: {my_playlist.count()}")
        print("Options: add | get | get all | remove | exit")
        
        choice = input("What would you like to do?: ")
        
        if choice == "add":
            title = input("Enter song title: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            duration = input("Enter duration: ")
            
            new_song = Song(title, artist, album, duration)
            my_playlist.add(new_song)
            print(f"{title} has been added to the playlist.")
        elif choice == "get":
            search_title = input("Enter song title: ")
            find_song = my_playlist.getByTitle(search_title)
            
            if find_song:
                print(" ---- Song Details ---- ")
                print(f"Title: {find_song.title}")
                print(f"Artist: {find_song.artist}")
                print(f"Album: {find_song.album}")
                print(f"Duration:  {find_song.duration}")
            
            else:
                print("Song not in playlist.")
        
        elif choice == "get all":
            all_songs = my_playlist.getAll()
            if not all_songs:
                print("The playlist is empty.")
                
            else:
                print(" ---- All Songs ---- ")
                for song in all_songs:
                    print(song)
                    
        elif choice == "remove":
            remove_title = input("Enter song title: ")
            if my_playlist.removeByTitle(remove_title):
                print(f"{remove_title} has been removed from the playlist.")
                
            else:
                print("Song not in playlist.")
                
        elif choice == "exit":
            print("Leaving program.")
            break
        
        else:
            print("Invalid option.")
            
        if __name__ == "__main__":
            main()
