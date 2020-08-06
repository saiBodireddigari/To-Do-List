def tracklist(**tracks):
    for key, values in tracks.items():
        print(f'{key}')
        for album, song in values.items():
            print(f'ALBUM: {album} TRACK: {song}')

