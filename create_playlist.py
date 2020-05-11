# 1. Log into YouTube
# 2. Grab liked videos
# 3. Create a new playlist on spotify
# 4. Search for the song
# 5. Add this song to the new spotify playlist

class CreatePlaylist:

# 1. Log into YouTube
  def __init__(self):
    pass

# 2. Grab liked videos
  def get_youtube_client(self):
    pass

# 3. Create a new playlist on spotify
  def create_playlist(self):
    request_body = json.dumps({
      "name": "YouTube Liked Videos",
      "description": "All likes YouTube Videos",
      "public": True,
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format()

# 4. Search for the song
  def get_spotify_uri(self):
    pass

# 5. Add this song to the new spotify playlist
  def add_song_to_playlist(self):
    pass
