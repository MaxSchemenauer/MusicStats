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
    num_songs = len(track_id)
    similarity_scores = num_songs * [0]

    print("Track ID:")

    for i in range(num_songs):

        ''' track_id '''
        this_id = track_id[song_index]
        temp_id = track_id[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_name '''
        this_name = track_name[song_index]
        temp_name = track_name[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_artist '''
        this_artist = track_artist[song_index]
        temp_artist = track_artist[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_popularity '''
        this_popularity = track_popularity[song_index]
        temp_popularity = track_popularity[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        '''track_album_id '''
        this_album_id = track_album_id[song_index]
        temp_album_id = track_album_id[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_album_name '''
        this_album_name = track_album_name[song_index]
        temp_album_name = track_album_name[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_album_release_date '''
        this_album_release_date = track_album_release_date[song_index]
        temp_album_release_date = track_album_release_date[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' playlist_name '''
        this_playlist_name = playlist_name[song_index]
        temp_playlist_name = playlist_name[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' playlist_id '''
        this_playlist_id = playlist_id[song_index]
        temp_playlist_id = playlist_id[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' playlist_genre '''

        this_playlist_genre = playlist_genre[song_index]
        temp_playlist_genre = playlist_genre[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' playlist_subgenre '''
        this_playlist_subgenre = playlist_subgenre[song_index]
        temp_playlist_subgenre = playlist_subgenre[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' danceability '''
        this_danceability = danceability[song_index]
        temp_danceability = danceability[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' energy '''
        this_energy = energy[song_index]
        temp_energy = energy[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' key '''
        this_key = key[song_index]
        temp_key = key[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' loudness '''
        this_loudness = loudness[song_index]
        temp_loudness = loudness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' mode '''
        this_mode = mode[song_index]
        temp_mode = mode[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' speechiness '''
        this_speechiness = speechiness[song_index]
        temp_speechiness = speechiness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' acousticness '''
        this_acousticness = acousticness[song_index]
        temp_acousticness = acousticness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' instrumentalness '''
        this_instrumentalness = instrumentalness[song_index]
        temp_instrumentalness = instrumentalness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' liveliness '''
        this_liveness = liveness[song_index]
        temp_liveness = liveness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' valence '''
        this_valence = valence[song_index]
        temp_valence = valence[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' tempo '''
        this_tempo = tempo[song_index]
        temp_tempo = tempo[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' duration_ms '''
        this_duration_ms = duration_ms[song_index]
        temp_duration_ms = duration_ms[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0


start_time = time.time()
similar_song(6236)
end_time = time.time()
elapsed_time = end_time - start_time
print("Scanned all arrays in:", elapsed_time, "seconds")
