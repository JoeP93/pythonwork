def make_album(artist, album_name, song):
    # Use strings for dictionary keys with spaces
    album_info = {
        "Artist": artist,
        "Album": album_name,
        "Top Song": song
    }
    return album_info

# Call the function with strings (using quotes)
musician_info = make_album("Matchbox Twenty", "Mad Season", "Damn")

print(musician_info)
