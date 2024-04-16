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


def similar_song(song_index, num_similar):
    num_songs = len(track_id)
    similarity_scores = num_songs * [0]

    print("Track ID:")

    for i in range(num_songs):

        ''' track_id '''
        this_id = track_id[song_index]
        other_id = track_id[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_name '''
        this_name = track_name[song_index]
        other_name = track_name[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_artist '''
        this_artist = track_artist[song_index]
        other_artist = track_artist[i]

        similarity_scores[i] += 5 if this_artist == other_artist else 0

        ''' track_popularity '''
        this_popularity = track_popularity[song_index]
        other_popularity = track_popularity[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        '''track_album_id '''
        this_album_id = track_album_id[song_index]
        other_album_id = track_album_id[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_album_name '''
        this_album_name = track_album_name[song_index]
        other_album_name = track_album_name[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' track_album_release_date '''
        this_album_release_date = track_album_release_date[song_index]
        other_album_release_date = track_album_release_date[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' playlist_name '''
        this_playlist_name = playlist_name[song_index]
        other_playlist_name = playlist_name[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' playlist_id '''
        this_playlist_id = playlist_id[song_index]
        other_playlist_id = playlist_id[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' playlist_genre '''

        this_playlist_genre = playlist_genre[song_index]
        other_playlist_genre = playlist_genre[i]

        similarity_scores[i] += 2 if this_playlist_genre == other_playlist_genre else 0

        ''' playlist_subgenre '''
        this_playlist_subgenre = playlist_subgenre[song_index]
        other_playlist_subgenre = playlist_subgenre[i]

        similarity_scores[i] += .5 if this_playlist_subgenre == other_playlist_subgenre else 0

        ''' danceability '''
        this_danceability = danceability[song_index]
        other_danceability = danceability[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' energy '''
        this_energy = energy[song_index]
        other_energy = energy[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' key '''
        this_key = key[song_index]
        other_key = key[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' loudness '''
        this_loudness = loudness[song_index]
        other_loudness = loudness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' mode '''
        this_mode = mode[song_index]
        other_mode = mode[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' speechiness '''
        this_speechiness = speechiness[song_index]
        other_speechiness = speechiness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' acousticness '''
        this_acousticness = acousticness[song_index]
        other_acousticness = acousticness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' instrumentalness '''
        this_instrumentalness = instrumentalness[song_index]
        other_instrumentalness = instrumentalness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' liveliness '''
        this_liveness = liveness[song_index]
        other_liveness = liveness[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' valence '''
        this_valence = valence[song_index]
        other_valence = valence[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' tempo '''
        this_tempo = tempo[song_index]
        other_tempo = tempo[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

        ''' duration_ms '''
        this_duration_ms = duration_ms[song_index]
        other_duration_ms = duration_ms[i]

        # TODO: Create method for adjusting similarity score
        similarity_scores[i] += 0

    # Zip the arrays together
    zipped_arrays = zip(similarity_scores, track_name)

    # Sort the zipped array based on the values of similarity_scores in descending order
    sorted_zipped_arrays = sorted(zipped_arrays, key=lambda x: x[0], reverse=True)

    # Unzip the sorted array
    sorted_similarity_scores, similar_tracks = zip(*sorted_zipped_arrays)

    print("sorted_similarity_scores:", sorted_similarity_scores[:10])
    print("similar_tracks:")
    for i in range(num_similar):
        print(sorted_similarity_scores[i], similar_tracks[i])

    return similarity_scores


start_time = time.time()
similarity_scores = similar_song(6236, 50)
end_time = time.time()
elapsed_time = end_time - start_time
print("Scanned all arrays in:", elapsed_time, "seconds")
