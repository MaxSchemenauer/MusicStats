# Project conception 03/31/2024
# Project started 04/02/2024

import pandas as pd
import time

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


def print_info(song_index):
    print("Track ID:", track_id[song_index])
    print("Track name:", track_name[song_index])
    print("Track artist:", track_artist[song_index])
    print("Track popularity:", track_popularity[song_index])
    print("Track album ID:", track_album_id[song_index])
    print("Track album name:", track_album_name[song_index])
    print("Track album release date:", track_album_release_date[song_index])
    print("Playlist name:", playlist_name[song_index])
    print("Playlist ID:", playlist_id[song_index])
    print("Playlist genre:", playlist_genre[song_index])
    print("Playlist subgenre:", playlist_subgenre[song_index])
    print("Danceability:", danceability[song_index])
    print("Energy:", energy[song_index])
    print("Key:", key[song_index])
    print("Loudness:", loudness[song_index])
    print("Mode:", mode[song_index])
    print("Speechiness:", speechiness[song_index])
    print("Acousticness:", acousticness[song_index])
    print("Instrumentalness:", instrumentalness[song_index])
    print("Liveness:", liveness[song_index])
    print("Valence:", valence[song_index])
    print("Tempo:", tempo[song_index])
    print("Duration (ms):", duration_ms[song_index])


print_info(6236)


def similar_song(song_index):
    x = 0

    print("Track ID:")
    for element in track_id:
        x += 1
        # print(element)

    print("\nTrack Name:")
    for element in track_name:
        x += 1
        # print(element)

    print("\nTrack Artist:")
    for element in track_artist:
        x += 1
        # print(element)

    print("\nTrack Popularity:")
    for element in track_popularity:
        x += 1
        # print(element)

    print("\nTrack Album ID:")
    for element in track_album_id:
        x += 1
        # print(element)

    print("\nTrack Album Name:")
    for element in track_album_name:
        x += 1
        # print(element)

    print("\nTrack Album Release Date:")
    for element in track_album_release_date:
        x += 1
        # print(element)

    print("\nPlaylist Name:")
    for element in playlist_name:
        x += 1
        # print(element)

    print("\nPlaylist ID:")
    for element in playlist_id:
        x += 1
        # print(element)

    print("\nPlaylist Genre:")
    for element in playlist_genre:
        x += 1
        # print(element)

    print("\nPlaylist Subgenre:")
    for element in playlist_subgenre:
        x += 1
        # print(element)

    print("\nDanceability:")
    for element in danceability:
        x += 1
        # print(element)

    print("\nEnergy:")
    for element in energy:
        x += 1
        # print(element)

    print("\nKey:")
    for element in key:
        x += 1
        # print(element)

    print("\nLoudness:")
    for element in loudness:
        x += 1
        # print(element)

    print("\nMode:")
    for element in mode:
        x += 1
        # print(element)

    print("\nSpeechiness:")
    for element in speechiness:
        x += 1
        # print(element)

    print("\nAcousticness:")
    for element in acousticness:
        x += 1
        # print(element)

    print("\nInstrumentalness:")
    for element in instrumentalness:
        x += 1
        # print(element)

    print("\nLiveness:")
    for element in liveness:
        x += 1
        # print(element)

    print("\nValence:")
    for element in valence:
        x += 1
        # print(element)

    print("\nTempo:")
    for element in tempo:
        x += 1
        # print(element)

    print("\nDuration (ms):")
    for element in duration_ms:
        x += 1
        # print(element)


start_time = time.time()
similar_song(6236)
end_time = time.time()
elapsed_time = end_time - start_time
print("Scanned all arrays in:", elapsed_time, "seconds")
