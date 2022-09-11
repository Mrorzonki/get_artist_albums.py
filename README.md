# get_artist_albums.py
    This python script searches artist in spotify by name and return name list of its albums
    It was written in Python 3.9.10 version

# before running
    1) Make sure pyton modules listed in next section are installed on computer or in current virtual enviroment   
    2) Set credetnials with command: get_artist_albums.py -c 'client_id' 'client_secret' 

# required modules
    'spotipy' - used to perform searches and get album list from spotify
    'pandas' and 'openpyxl' - used for exporting output file in 'csv' and 'xlsx (excel) formats

# usages
    get_artist_albums.py 'artist name' 'export type' 'file pathname'
        'artist name' - name of the aritst in spotify
        'export type' - avalible output formats: 'csv','excel','json' (each crates a file) or 'raw' (wites to console).
        'file pathname' - optional pathname for output file (without file extension), when skipped artist_name is used. If file extension was prowided it will be replaced.
        
        searches spotify artist by name and if exact match was found outputs name list of its albums in selected format
    
    get_artist_albums.py -c 'client_id' 'client_secret'
        replaces spotipy client credentials in setup.json file with ones provided
