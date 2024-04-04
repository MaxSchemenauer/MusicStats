# Project conception 03/31/2024
# Project started 04/02/2024

import pandas as pd

# Read the CSV file
df = pd.read_csv("spotify_songs.csv")

# Convert each column into an array
track_id = df['track_id'].values
track_name = df['track_name'].values
track_artist = df['track_artist'].values
track_popularity = df['track_popularity'].values
track_album_id = df['track_album_id'].values
track_album_name = df['track_album_name'].values
track_album_release_date = df['track_album_release_date'].values
playlist_name = df['playlist_name'].values
playlist_id = df['playlist_id'].values
playlist_genre = df['playlist_genre'].values
playlist_subgenre = df['playlist_subgenre'].values
danceability = df['danceability'].values
energy = df['energy'].values
key = df['key'].values
loudness = df['loudness'].values
mode = df['mode'].values
speechiness = df['speechiness'].values
acousticness = df['acousticness'].values
instrumentalness = df['instrumentalness'].values
liveness = df['liveness'].values
valence = df['valence'].values
tempo = df['tempo'].values
duration_ms = df['duration_ms'].values

# Example of accessing the arrays
print("First track ID:", track_id[0])
print("First track name:", track_name[0])

