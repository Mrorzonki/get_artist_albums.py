#module imports
import credentials as cred
import spotipy_module as spm
import json #TODO: remove - test only

#other imports
import sys

def main(artist_name='Casting Crowns', export_type='raw', path_name='C:/Users/X/Desktop/out'):
    auth_sp = spm.get_authentication(cred.client_id, cred.client_secret) 
    
    artist = spm.get_artist_by_name(auth_sp, artist_name)
    albums = spm.get_albums_by_artist(auth_sp, artist['id'])

    print(json.dumps(albums))

if __name__ == '__main__':
    argv = sys.argv
    main()