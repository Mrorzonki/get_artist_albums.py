# get_artist_albums.py
This python script searches artist in spotify by name and return name list of its albums .

# usages:
  get_artist_albums.py 'artist name' 'export type' 'file pathname'
      'artist name' - name of the aritst in spotify"
      'export type' - avalible output formats: 'csv','excel','json' (each crates a file) or 'raw' (wites to console)"
      'file pathname' - optional pathname for output file (without file extension), when skipped artist_name is used"
      
      searches spotify artist by name and if exact match was found outputs name list of its albums in selected format
  
  get_artist_albums.py -c 'client_id' 'client_secret'
      replaces spotipy client credentials in setup.json file with ones provided
