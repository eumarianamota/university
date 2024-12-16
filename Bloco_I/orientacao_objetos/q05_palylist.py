# Crie uma classe Playlist com:
# Atributos:
  # name (nome da playlist).
  # songs (lista de músicas, inicialmente vazia).
# Métodos:
  # add_song(song) - adiciona uma música à lista.   
  # remove_song(song) - remove uma música, se existir.
  # show_songs() - exibe todas as músicas na playlist.

class Playlist:
  def __init__(self, name, songs):
    self.name = name 
    self.songs = []
    self.songs.append(songs)

  def add_song(self, song):
    self.songs.append(song)
  
  def remove_song(self, song):
      if song in self.songs:
        self.songs.remove(song)
  
  def show_songs(self, songs):
    for song in songs:
      print(song)